#NON-COMMERCIAL-CODE

#.py
#Calculator

import tkinter

from tkinter import*

from tkinter import ttk
import math

import re
import PIL
from PIL import ImageTk, Image

global maths
import numpy
import numpy.polynomial.polynomial as poly

maths=None
global s


global mem
mem=str(0)

root= Tk()
root.config(bg="#3D3D3D")
root.title(" ")


def Add(num):
    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) +str(num))

def Add1(num):
    global e11
    #e.delete(0,END)
    current=e11.get()
    e11.delete(0,END)
    e11.insert(0,str(current) +str(num))


def Sum():
    global s
    s=e.get()
    e.delete(0,END)
    e.insert(0, str(s) +"+")
def Sub():
    global s
    s=e.get()
    e.delete(0,END)
    e.insert(0, str(s) +"-")
def Mul():
    global s
    s=e.get()
    e.delete(0,END)
    e.insert(0, str(s) +"*")
def Did():
    global s
    s=e.get()
    e.delete(0,END)
    e.insert(0, str(s) +"/")

def POW():
    Fn=e.get()
    global fn
    global maths
    maths="pow"
    fn= eval (Fn)
    e.delete(0,END)
    e.insert(0,"("+str(fn)+")"+"**")

def DOT():
    o=e.get()
    e.delete(0,END)
    e.insert(0,str(o)+".")


def Mode():
    global mode
    mode="Deg"
    sti=str(butdis.get())
    

    if sti=="Deg":
        butdis.delete(0,END)
        butdis.insert(0,"Rad")

    elif sti=="Rad":
      
        butdis.delete(0,END)
        butdis.insert(0,"Deg")

def EQ():
    
    try:
        
        o=e.get()
        e.delete(0,END)
        e.insert(0,eval(o))
        
    except NameError as err:
        
        if maths== "sin":
            if str(butdis.get())=="Deg" and str(butalphadis.get())=="Alpha: Off":
           
           
                e.delete(0,END)
           
                s=math.sin(math.radians(fn))
                e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: Off":

                e.delete(0,END)
                s=math.sin(fn)
                e.insert(0,str(s))
            elif str(butdis.get())=="Deg" and str(butalphadis.get())=="Alpha: On":
           
           
                e.delete(0,END)
                if fn>1 or fn<-1:
                    e.insert(0,"Cannot Compute, sin y=x is 0<=x<=1")
                    raise ValueError("Cannot Compute, sin x is 0<=x<=1")
                    
                else:
                    s=math.degrees(math.asin(fn))
                    e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: On":
                

                e.delete(0,END)
                if fn>1 or fn<(-1):
                    
                    e.insert(0,"Cannot Compute, sin y=x is 0<=x<=1")
                    raise ValueError("Cannot Compute, sin x is 0<=x<=1")
                else:  
                    s=math.asin(fn)
                    e.insert(0,str(s))
            else:
                e.delete(0,END)
                e.insert(0,"Triogonometry mode Error")
            
                

        elif maths=="cos":
            if str(butdis.get())=="Deg"and str(butalphadis.get())=="Alpha: Off":
           
           
                e.delete(0,END)
           
                s=math.cos(math.radians(fn))
                e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: Off":

                e.delete(0,END)
                s=math.cos(fn)
                e.insert(0,str(s))
            elif str(butdis.get())=="Deg" and str(butalphadis.get())=="Alpha: On":
           
           
                e.delete(0,END)
                if fn>1:
                    
                    e.insert(0,"Cannot Compute, cos y=x is -1<=x<=1")
                    raise ValueError("Cannot Compute, sin x is 0<=x<=1")
                    
                else:
                    s=math.degrees(math.acos(fn))
                    e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: On":
                

                e.delete(0,END)
                if fn>1 or fn<(-1):
                    
                    e.insert(0,"Cannot Compute, cos y=x is 0<=x<=1")
                    raise ValueError("Cannot Compute, sin x is 0<=x<=1")
                else:  
                    s=math.acos(fn)
                    e.insert(0,str(s))

            else:
                e.delete(0,END)
                e.insert(0,"Triogonometry mode Error")
            
            
        elif maths=="tan":
            if str(butdis.get())=="Deg"and str(butalphadis.get())=="Alpha: Off":
           
           
                e.delete(0,END)
           
                s=math.tan(math.radians(fn))
                e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: Off":

                e.delete(0,END)
                s=math.tan(fn)
                e.insert(0,str(s))
            elif str(butdis.get())=="Deg" and str(butalphadis.get())=="Alpha: On":
           
           
                e.delete(0,END)
                
                
                s=math.degrees(math.atan(fn))
                e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: On":
                

                e.delete(0,END)
                
                s=math.atan(fn)
                e.insert(0,str(s))
            else:
                e.delete(0,END)
                e.insert(0,"Triogonometry mode Error")
            
            
        elif maths=="cot":
            if str(butdis.get())=="Deg"and str(butalphadis.get())=="Alpha: Off":
           
           
                e.delete(0,END)
           
                s=1/(math.tan(math.radians(fn)))
                e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: Off":

                e.delete(0,END)
                s=1/(math.tan(fn))
                e.insert(0,str(s))
            elif str(butdis.get())=="Deg" and str(butalphadis.get())=="Alpha: On":
           
           
                e.delete(0,END)
                
                
                s=1/math.degrees(math.atan(fn))
                e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: On":
                

                e.delete(0,END)
                
                s=1/math.atan(fn)
                e.insert(0,str(s))
            else:
                e.delete(0,END)
                e.insert(0,"Triogonometry mode Error")
           
        elif maths=="sec":
            if str(butdis.get())=="Deg"and str(butalphadis.get())=="Alpha: Off":
           
           
                e.delete(0,END)
           
                s=1/(math.cos(math.radians(fn)))
                e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: Off":

                e.delete(0,END)
                s=1/(math.cos(fn))
                e.insert(0,str(s))
            elif str(butdis.get())=="Deg" and str(butalphadis.get())=="Alpha: On":
           
           
                e.delete(0,END)
                if fn>1 or fn<-1:
                    
                    e.insert(0,"Cannot Compute, sec y=x is -1<=x<=1")
                    raise ValueError("Cannot Compute, sin x is 0<=x<=1")
                    
                else:
                    s=1/math.degrees(math.acos(fn))
                    e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: On":
                

                e.delete(0,END)
                if fn>1 or fn<(-1):
                    
                    e.insert(0,"Cannot Compute, sec y=x is 0<=x<=1")
                    raise ValueError("Cannot Compute, sin x is 0<=x<=1")
                else:  
                    s=1/math.acos(fn)
                    e.insert(0,str(s))
            else:
                e.delete(0,END)
                e.insert(0,"Triogonometry mode Error")
           
        elif maths=="csc":
            
            
            if str(butdis.get())=="Deg"and str(butalphadis.get())=="Alpha: Off":
                
           
           
                e.delete(0,END)
           
                s=1/(math.sin(math.radians(fn)))
                e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: Off":
                

                e.delete(0,END)
                s=1/(math.sin(fn))
                e.insert(0,str(s))
            elif str(butdis.get())=="Deg" and str(butalphadis.get())=="Alpha: On":
                 
           
           
                e.delete(0,END)
                if fn>1:
                    
                    e.insert(0,"Cannot Compute, csc y=x is -1<=x<=1")
                    raise ValueError("Cannot Compute, sin x is 0<=x<=1")
                    
                else:
                    s=1/math.degrees(math.asin(fn))
                    e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: On":
                

                e.delete(0,END)
                if fn>1 or fn<(-1):
                    
                    e.insert(0,"Cannot Compute, sin y=x is 0<=x<=1")
                    raise ValueError("Cannot Compute, csc x is 0<=x<=1")
                else:  
                    s=1/math.asin(fn)
                    e.insert(0,str(s))
            else:
                e.delete(0,END)
                e.insert(0,"Triogonometry mode Error")
            
        

        

        elif maths=="log":
            
            if fn<0:
                
                e.insert(1,str(math.log10(-fn))+"+1.36437635 i")
               
            else:
                
                
                e.delete(0,END)
           
                s=math.log10(fn)
                e.insert(0,str(s))

        elif maths=="log2":
            
            if fn<0:
                
                 
                e.insert(1, "Log Limit Exceeded, must not less than 0!")
            else:
                
                 
                e.delete(0,END)
           
                s=math.log2(fn)
                e.insert(0,str(s))

        elif maths =="ln":
            
            if fn<0:
                
                e.insert(1,str(math.log1p(-(fn)))+"+3.14159265 i")
               
            else:
                 
                e.delete(0,END)
           
                s=math.log1p(fn)
                e.insert(0,str(s))

        elif maths=="pow":
            sec=e.get()
            e.delete(0,END)
            e.insert(0, fn**float(sec))


        elif maths=="neg-":
            f=e.get()
            e.delete(0, END)
            e.insert(0,str(-f))

        elif maths=="%":
            
            e.delete(0,END)
            e.insert(0, str(fn*100)+"%")
            
    except ZeroDivisionError as err2:
        e.insert(0, "Undefined or Indeterminated Form")

    except SyntaxError as err3:
        
        if maths== "sin":
            if str(butdis.get())=="Deg" and str(butalphadis.get())=="Alpha: Off":
           
           
                e.delete(0,END)
           
                s=math.sin(math.radians(fn))
                e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: Off":

                e.delete(0,END)
                s=math.sin(fn)
                e.insert(0,str(s))
            elif str(butdis.get())=="Deg" and str(butalphadis.get())=="Alpha: On":
           
           
                e.delete(0,END)
                if fn>1 or fn<-1:
                    e.insert(0,"Cannot Compute, sin y=x is 0<=x<=1")
                    raise ValueError("Cannot Compute, sin x is 0<=x<=1")
                    
                else:
                    s=math.degrees(math.asin(fn))
                    e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: On":
                

                e.delete(0,END)
                if fn>1 or fn<(-1):
                    
                    e.insert(0,"Cannot Compute, sin y=x is 0<=x<=1")
                    raise ValueError("Cannot Compute, sin x is 0<=x<=1")
                else:  
                    s=math.asin(fn)
                    e.insert(0,str(s))
            else:
                e.delete(0,END)
                e.insert(0,"Triogonometry mode Error")
            
                

        elif maths=="cos":
            if str(butdis.get())=="Deg"and str(butalphadis.get())=="Alpha: Off":
           
           
                e.delete(0,END)
           
                s=math.cos(math.radians(fn))
                e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: Off":

                e.delete(0,END)
                s=math.cos(fn)
                e.insert(0,str(s))
            elif str(butdis.get())=="Deg" and str(butalphadis.get())=="Alpha: On":
           
           
                e.delete(0,END)
                if fn>1:
                    
                    e.insert(0,"Cannot Compute, cos y=x is -1<=x<=1")
                    raise ValueError("Cannot Compute, sin x is 0<=x<=1")
                    
                else:
                    s=math.degrees(math.acos(fn))
                    e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: On":
                

                e.delete(0,END)
                if fn>1 or fn<(-1):
                    
                    e.insert(0,"Cannot Compute, cos y=x is 0<=x<=1")
                    raise ValueError("Cannot Compute, sin x is 0<=x<=1")
                else:  
                    s=math.acos(fn)
                    e.insert(0,str(s))

            else:
                e.delete(0,END)
                e.insert(0,"Triogonometry mode Error")
            
            
        elif maths=="tan":
            if str(butdis.get())=="Deg"and str(butalphadis.get())=="Alpha: Off":
           
           
                e.delete(0,END)
           
                s=math.tan(math.radians(fn))
                e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: Off":

                e.delete(0,END)
                s=math.tan(fn)
                e.insert(0,str(s))
            elif str(butdis.get())=="Deg" and str(butalphadis.get())=="Alpha: On":
           
           
                e.delete(0,END)
                
                
                s=math.degrees(math.atan(fn))
                e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: On":
                

                e.delete(0,END)
                
                s=math.atan(fn)
                e.insert(0,str(s))
            else:
                e.delete(0,END)
                e.insert(0,"Triogonometry mode Error")
            
            
        elif maths=="cot":
            if str(butdis.get())=="Deg"and str(butalphadis.get())=="Alpha: Off":
           
           
                e.delete(0,END)
           
                s=1/(math.tan(math.radians(fn)))
                e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: Off":

                e.delete(0,END)
                s=1/(math.tan(fn))
                e.insert(0,str(s))
            elif str(butdis.get())=="Deg" and str(butalphadis.get())=="Alpha: On":
           
           
                e.delete(0,END)
                
                
                s=1/math.degrees(math.atan(fn))
                e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: On":
                

                e.delete(0,END)
                
                s=1/math.atan(fn)
                e.insert(0,str(s))
            else:
                e.delete(0,END)
                e.insert(0,"Triogonometry mode Error")
           
        elif maths=="sec":
            if str(butdis.get())=="Deg"and str(butalphadis.get())=="Alpha: Off":
           
           
                e.delete(0,END)
           
                s=1/(math.cos(math.radians(fn)))
                e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: Off":

                e.delete(0,END)
                s=1/(math.cos(fn))
                e.insert(0,str(s))
            elif str(butdis.get())=="Deg" and str(butalphadis.get())=="Alpha: On":
           
           
                e.delete(0,END)
                if fn>1 or fn<-1:
                    
                    e.insert(0,"Cannot Compute, sec y=x is -1<=x<=1")
                    raise ValueError("Cannot Compute, sin x is 0<=x<=1")
                    
                else:
                    s=1/math.degrees(math.acos(fn))
                    e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: On":
                

                e.delete(0,END)
                if fn>1 or fn<(-1):
                    
                    e.insert(0,"Cannot Compute, sec y=x is 0<=x<=1")
                    raise ValueError("Cannot Compute, sin x is 0<=x<=1")
                else:  
                    s=1/math.acos(fn)
                    e.insert(0,str(s))
            else:
                e.delete(0,END)
                e.insert(0,"Triogonometry mode Error")
           
        elif maths=="csc":
            
            
            if str(butdis.get())=="Deg"and str(butalphadis.get())=="Alpha: Off":
                
           
           
                e.delete(0,END)
           
                s=1/(math.sin(math.radians(fn)))
                e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: Off":
                

                e.delete(0,END)
                s=1/(math.sin(fn))
                e.insert(0,str(s))
            elif str(butdis.get())=="Deg" and str(butalphadis.get())=="Alpha: On":
                 
           
           
                e.delete(0,END)
                if fn>1:
                    
                    e.insert(0,"Cannot Compute, csc y=x is -1<=x<=1")
                    raise ValueError("Cannot Compute, sin x is 0<=x<=1")
                    
                else:
                    s=1/math.degrees(math.asin(fn))
                    e.insert(0,str(s))

            elif str(butdis.get())=="Rad"and str(butalphadis.get())=="Alpha: On":
                

                e.delete(0,END)
                if fn>1 or fn<(-1):
                    
                    e.insert(0,"Cannot Compute, sin y=x is 0<=x<=1")
                    raise ValueError("Cannot Compute, csc x is 0<=x<=1")
                else:  
                    s=1/math.asin(fn)
                    e.insert(0,str(s))
            else:
                
                e.delete(0,END)
                e.insert(0,"Triogonometry mode Error")
            
        else:
            
            
            e.insert(0,"invalid maths syntax used")

                        
    
    mem=e.get()
    opd=butmem.get()
    butmem.delete(0,END)
    butmem.insert(0,str(opd)+" , "+str(mem))
    
    
def Neg():
    Fn=e.get()
    global fn
    fn= eval(Fn)
    global maths
    maths= "neg-"
    e.delete(0,END)
    e.insert(0,str(- (fn)))
        
     
def Sin():
    Fn=e.get()
    global fn
    global maths
    maths="sin"
    fn=eval(Fn)
    
    e.delete(0,END)
    if str(butalphadis.get())=="Alpha: Off":
        e.insert(0,"sin( "+str(fn)+ " ) ")
    elif str(butalphadis.get())=="Alpha: On":
        e.insert(0,"sin\u207B\u00B9( "+str(fn)+ " ) ")
def COS():
    Fn=e.get()
    global fn
    global maths
    maths="cos"
    fn=eval(Fn)
    
    e.delete(0,END)
    if str(butalphadis.get())=="Alpha: Off":
        e.insert(0,"cos( "+str(fn)+ " ) ")
    elif str(butalphadis.get())=="Alpha: On":
        e.insert(0,"cos\u207B\u00B9( "+str(fn)+ " ) ")
def TAN():
    Fn=e.get()
    global fn
    global maths
    maths="tan"
    fn=eval(Fn)
    
    e.delete(0,END)
    if str(butalphadis.get())=="Alpha: Off":
        e.insert(0,"tan( "+str(fn)+ " ) ")
    elif str(butalphadis.get())=="Alpha: On":
        e.insert(0,"tan\u207B\u00B9( "+str(fn)+ " ) ")
    
def COT():
    Fn=e.get()
    global fn
    global maths
    maths="cot"
    fn=eval(Fn)
    
    e.delete(0,END)
    if str(butalphadis.get())=="Alpha: Off":
        e.insert(0,"cot( "+str(fn)+ " ) ")
    elif str(butalphadis.get())=="Alpha: On":
        e.insert(0,"cot\u207B\u00B9( "+str(fn)+ " ) ")
    
def SEC():
    Fn=e.get()
    global fn
    global maths
    maths="sec"
    fn=eval(Fn)
    
    e.delete(0,END)
    if str(butalphadis.get())=="Alpha: Off":
        e.insert(0,"sec( "+str(fn)+ " ) ")
    elif str(butalphadis.get())=="Alpha: On":
        e.insert(0,"sec\u207B\u00B9( "+str(fn)+ " ) ")
    
def CSC():
    Fn=e.get()
    global fn
    global maths
    maths="csc"
    fn=eval(Fn)
    
    e.delete(0,END)
    if str(butalphadis.get())=="Alpha: Off":
        e.insert(0,"csc( "+str(fn)+ " ) ")
    elif str(butalphadis.get())=="Alpha: On":
        e.insert(0,"csc\u207B\u00B9( "+str(fn)+ " ) ")
    
def LOG10():
    Fn=e.get()
    global fn
    global maths
    maths="log"
    fn=eval(Fn)
    
    e.delete(0,END)
    e.insert(0,"log( "+str(fn)+ " ) ")
    
def LN():
    Fn=e.get()
    global fn
    global maths
    maths="ln"
    fn=eval(Fn)
    
    e.delete(0,END)
    e.insert(0,"ln( "+str(fn)+ " ) ")
    
def LOG2():
    Fn=e.get()
    global fn
    global maths
    maths="log2"
    fn=eval(Fn)
    
    e.delete(0,END)
    e.insert(0,"log2( "+str(fn)+ " ) ")
def CL():
    e.delete(0,END)

def back():
    fo=e.get()
    e.delete(0,END)
    fi=str(fo)
    so=re.split("([\d\+\-\/\*\(\)])",fi)
    n=len(so)
    so.pop()
    so.pop()
    si="".join(so)
    e.insert(0,str(si))
    e.get()

def Dis():
    butdis.insert(0,"Degrees")

def Op():
    sy=e.get()
    e.delete(0,END)
    e.insert(0, str(sy)+"(")
    if sy is None:
        e.insert(0,"(")

def Clo():
    sy=e.get()
    e.delete(0,END)
    e.insert(0, str(sy)+")")
    if sy is None:
        e.insert(0,")")
def Res():

    st=e.get()
    e.delete(0,END)
    e.insert(0,str(1/(eval(st))))

def Alpha():

    sr=butalphadis.get()
    if sr=="Alpha: Off":
        butalphadis.delete(0,END)
        butalphadis.insert(0,"Alpha: On")
    elif sr=="Alpha: On":
        butalphadis.delete(0,END)
        butalphadis.insert(0,"Alpha: Off")

def Sp():
    fo=butmem.get()
    butmem.delete(0,END)
    fi=str(fo)
    so=re.split("([\d\+\-\/\*\(\)\,])",fi)
    n=len(so)
    so.pop()
    so.pop()
    si="".join(so)
    butmem.insert(0,str(si))
    butmem.get()

def All():
    fo=butmem.get()
    butmem.delete(0,END)
    butmem.get()

def Per():
    Fn=e.get()
    global fn
    global maths
    maths="%"
    fn=eval(Fn)
    e.delete(0,END)
    e.insert(0,"perc("+ str(fn)+")")

def Ans():
    d=butmem.get()
    op=re.split(", ",d)
    od=len(op)
    e.delete(0,END)
    e.insert(0,str(op[od-1]))


def eneg():
    global e11

    xoxo=eval( e11.get())
    e11.delete(0,END)
    e11.insert(1,str(-xoxo))

def resc():
    global e11
    r=eval(e11.get())
    s=1/r
    e11.delete(0,END)
    e11.insert(1,str(s))

global danGi
danGi =[]


def nexto():
    global e11
    global danGi
 
    try:
        woe= eval(e11.get())
        danGi.insert(0,woe)
        e11.delete(0,END)
    except:
        e11.delete(0,END)
        e11.insert(1, "An Error is encountered")
        danGi=[]

def Calc():
    global e11
    global danGi
    strio=e11.get()
    if strio!="":
        try:
            danGi.insert(0,eval(strio))
        except:
            e11.insert(1, "An Error is encountered")
            danGi=[]

    rt1=[]
    x=0
    q= poly.Polynomial(danGi)
    rt=poly.Polynomial.roots(q)
    for d in range(len(rt)):
        d=str(round(rt[x],4))

        rt1.append(d)
        x+=1
    hjk=" or ".join(rt1)
    e11.delete(0,END)
    e11.insert(1,str(hjk))
    danGi=[]



def e11deleter():
    global e11
    e11.delete(0,END)

def Const():
    global lbx
    r1=Toplevel()

    r1.config(bg="#1F1F1F")
    r1.title("Constants")

    r1.geometry("200x230")
    r=Frame(r1)
    r.grid(row=0,column=0)
    lbx= Listbox(r, bg="#1F1F1F", fg="#40E0D0",font="Consolas 12 ",background="#313335", foreground="#40E0D0")
    lbx.pack(side=LEFT, expand='True', anchor="e", fill=BOTH)
    xro=Scrollbar(r, activebackground="gray", bg="#1F1F1F", bd=0, highlightbackground="#313335")
    
    xro.pack(side=RIGHT, expand='True', anchor="e",fill= Y)
    xro.configure(command=lbx.yview)

    lbx.configure(yscrollcommand=xro.set)
    
    lbx.insert(END, "µ\u2091")
    lbx.insert(END, "µ\u209A")
    lbx.insert(END, "ρₐ\u1D62\u1D63")
    lbx.insert(END, "\u210F")
    lbx.insert(END, "h")
    lbx.insert(END, "m\u209A")
    lbx.insert(END, "m\u2091")
    lbx.insert(END, "mµ")
    lbx.insert(END, "m\u2099")
    lbx.insert(END, "a\u2080")
    lbx.insert(END, "g")
    lbx.insert(END, "µN")
    lbx.insert(END, "µB")
    lbx.insert(END, "α")
    lbx.insert(END, "r\u2091")
    lbx.insert(END, "λc")
    lbx.insert(END, "γp")
    lbx.insert(END, "λc,p")
    lbx.insert(END, "λc,n")
    lbx.insert(END, "R∞")
    lbx.insert(END, "u")
    lbx.insert(END, "µ\u2099")
    lbx.insert(END, "µ\u1D64")
    lbx.insert(END, "F")
    lbx.insert(END, "e(maths)")
    lbx.insert(END, "Avogadro(NA)")
    lbx.insert(END, "k")
    lbx.insert(END, "Vm")
    lbx.insert(END, "R")
    lbx.insert(END, "C\u2080")
    lbx.insert(END, "C\u2081")
    lbx.insert(END, "C\u2082")
    lbx.insert(END, "σ")
    lbx.insert(END, "µ\u2080")
    lbx.insert(END, "ϵ\u2080")
    lbx.insert(END, "φ\u2080")
    lbx.insert(END, "G\u2080")
    lbx.insert(END, "Z\u2080")
    lbx.insert(END, "t(Kelvin Sci)")    
    lbx.insert(END, "G")    
    lbx.insert(END, "atm")
    lbx.insert(END, "bar")
    lbx.insert(END, "K(Kelvin)")
    lbx.insert(END, "e(electron)")
    lbx.insert(END, "π")
    lbx.bind("<Double-Button-1>", vbind)
    app=Button(r1, bg="#313335", text="Add(+)",fg="#40E0D0",font="Consolas 12 ", border=0, command=v,padx=70)
    app.grid(row=1,column=0)

def v():
    
    global lbx
    d=lbx.get(ANCHOR)

    if d=="µ\u2091":
        e.insert(END, str(-9.2847*10**-24))
    elif d=="µ\u209A":
        e.insert(END, str(-1.4106*10**-26))
    elif d=="ρₐ\u1D62\u1D63":
        e.insert(END, str(1.2041))
    elif d=="\u210F":
        e.insert(END, str(1.05457163*10**-34))
    elif d=="h":
        e.insert(END, str(6.62606896*10**-34))
    elif d=="m\u209A":
        e.insert(END, str(1.672621637*10**-27))
    elif d=="m\u2091":
        e.insert(END, str(9.109382150*10**-31))
    elif d=="mµ":
        e.insert(END, str(1.8835313*10**-28))
    elif d=="m\u2099":
        e.insert(END, str(1.674927211*10**-27))
    elif d=="a\u2080":
        e.insert(END, str(5.291772086*10**-11))
    elif d=="g":
        e.insert(END, str(9.806650))
    elif d=="µN":
        e.insert(END, str(5.05078324*10**-27))
    elif d=="µB":
        e.insert(END, str(9.27400915*10**-24))
    elif d=="α":
        e.insert(END, str(7.297352538*10**-3))
    elif d=="r\u2091":
        e.insert(END, str(2.817940289*10**-15))
    elif d=="λc":
        e.insert(END, str(2.426310218*10**-12))
    elif d=="γp":
        e.insert(END, str(267522209.9))
    elif d=="λc,p":
        e.insert(END, str(1.321409845*10**-15))
    elif d=="λc,n":
        e.insert(END, str(1.319590895*10**-15))
    elif d=="R∞":
        e.insert(END, str(10973731.57))
    elif d=="u":
        e.insert(END, str(1.660538782*10**-27))
    elif d=="µ\u2099":
        e.insert(END, str(-9.6623641*10**-27))
    elif d=="µ\u1D64":
        e.insert(END, str(-4.49044786*10**-26))
    elif d=="F":
        e.insert(END, str(96485.3399))
    elif d=="e(maths)":
        e.insert(END, str(2.71828))
    elif d=="Avogadro(NA)":
        e.insert(END, str(6.02214179*10**23))
    elif d=="k":
        e.insert(END, str(1.3806504*10**-23))
    elif d=="Vm":
        e.insert(END, str(0.022413996))
    elif d=="R":
        e.insert(END, str(8.314472))
    elif d=="C\u2080":
        e.insert(END, str(299792458))
    elif d=="C\u2081":
        e.insert(END, str(3.74177118*10**-16))
    elif d=="C\u2082":
        e.insert(END, str(0.014387752))
    elif d=="σ":
        e.insert(END, str(5.5704*10**-8))
    elif d=="µ\u2080":
        e.insert(END, str(1.256637061*10**-34))
    elif d=="ϵ\u2080":
        e.insert(END, str(8.854187817*10**-12))
    elif d=="φ\u2080":
        e.insert(END, str(2.067833667*10**-15))
    elif d=="G\u2080":
        e.insert(END, str(7.7480917*10**-5))
    elif d=="Z\u2080":
        e.insert(END, str(376.7303135))
    elif d=="t(Kelvin Sci)":
        e.insert(END, str(273.15))
    elif d=="G":
        e.insert(END, str(6.62606896*10**-34))
    elif d=="atm":
        e.insert(END, str(1.013*10**5))
    elif d=="bar":
        e.insert(END, str(1.01325))
    elif d=="K(Kelvin)":
        e.insert(END, str(273))
    elif d=="e(electron)":
        e.insert(END, str(1.602176487*10**-19))
    elif d=="π":
        e.insert(END, str(3.141592654))
  


def vbind(self):
    global lbx
    d=lbx.get(ANCHOR)

    
    if d=="µ\u2091":
        e.insert(END, str(-9.2847*10**-24))
    elif d=="µ\u209A":
        e.insert(END, str(-1.4106*10**-26))
    elif d=="ρₐ\u1D62\u1D63":
        e.insert(END, str(1.2041))
    elif d=="\u210F":
        e.insert(END, str(1.05457163*10**-34))
    elif d=="h":
        e.insert(END, str(6.62606896*10**-34))
    elif d=="m\u209A":
        e.insert(END, str(1.672621637*10**-27))
    elif d=="m\u2091":
        e.insert(END, str(9.109382150*10**-31))
    elif d=="mµ":
        e.insert(END, str(1.8835313*10**-28))
    elif d=="m\u2099":
        e.insert(END, str(1.674927211*10**-27))
    elif d=="a\u2080":
        e.insert(END, str(5.291772086*10**-11))
    elif d=="g":
        e.insert(END, str(9.806650))
    elif d=="µN":
        e.insert(END, str(5.05078324*10**-27))
    elif d=="µB":
        e.insert(END, str(9.27400915*10**-24))
    elif d=="α":
        e.insert(END, str(7.297352538*10**-3))
    elif d=="r\u2091":
        e.insert(END, str(2.817940289*10**-15))
    elif d=="λc":
        e.insert(END, str(2.426310218*10**-12))
    elif d=="γp":
        e.insert(END, str(267522209.9))
    elif d=="λc,p":
        e.insert(END, str(1.321409845*10**-15))
    elif d=="λc,n":
        e.insert(END, str(1.319590895*10**-15))
    elif d=="R∞":
        e.insert(END, str(10973731.57))
    elif d=="u":
        e.insert(END, str(1.660538782*10**-27))
    elif d=="µ\u2099":
        e.insert(END, str(-9.6623641*10**-27))
    elif d=="µ\u1D64":
        e.insert(END, str(-4.49044786*10**-26))
    elif d=="F":
        e.insert(END, str(96485.3399))
    elif d=="e(maths)":
        e.insert(END, str(2.71828))
    elif d=="Avogadro(NA)":
        e.insert(END, str(6.02214179*10**23))
    elif d=="k":
        e.insert(END, str(1.3806504*10**-23))
    elif d=="Vm":
        e.insert(END, str(0.022413996))
    elif d=="R":
        e.insert(END, str(8.314472))
    elif d=="C\u2080":
        e.insert(END, str(299792458))
    elif d=="C\u2081":
        e.insert(END, str(3.74177118*10**-16))
    elif d=="C\u2082":
        e.insert(END, str(0.014387752))
    elif d=="σ":
        e.insert(END, str(5.5704*10**-8))
    elif d=="µ\u2080":
        e.insert(END, str(1.256637061*10**-34))
    elif d=="ϵ\u2080":
        e.insert(END, str(8.854187817*10**-12))
    elif d=="φ\u2080":
        e.insert(END, str(2.067833667*10**-15))
    elif d=="G\u2080":
        e.insert(END, str(7.7480917*10**-5))
    elif d=="Z\u2080":
        e.insert(END, str(376.7303135))
    elif d=="t(Kelvin Sci)":
        e.insert(END, str(273.15))
    elif d=="G":
        e.insert(END, str(6.62606896*10**-34))
    elif d=="atm":
        e.insert(END, str(1.013*10**5))
    elif d=="bar":
        e.insert(END, str(1.01325))
    elif d=="K(Kelvin)":
        e.insert(END, str(273))
    elif d=="e(electron)":
        e.insert(END, str(1.602176487*10**-19))
    elif d=="π":
        e.insert(END, str(3.141592654))
  
    
def e11bcck():
    global e11
    fo1=e11.get()
    e11.delete(0,END)
    fi11=str(fo1)
    so1=re.split("([\d\+\-\/\*\(\)])",fi11)
    n=len(so1)
    so1.pop()
    so1.pop()
    si1="".join(so1)
    e11.insert(0,str(si1))
    e11.get()

def dc1deleter():
    global dc1
    dc1.delete(0, END)

def dc1bcck():
    global dc1
    cfg= str(dc1.get())
    cv= re.split("([\d\+\-\/\*\(\)])", cfg )
    cv.pop()
    cv.pop()
    cd= "".join(cv)
    dc1.delete(0, END)
    dc1.insert(1, str(cd))

def Way1():
    global dc1
    dc1lover= eval(dc1.get())


    global butpo1
    e11lover=eval(e11.get())

    if butpo1.get()=="+":
        e11.delete(0,END)
        e11.insert(1,str(e11lover+dc1lover))
    elif butpo1.get()=="-":
        e11.delete(0,END)
        e11.insert(1,str(e11lover-dc1lover))
    elif butpo1.get()=="*":
        e11.delete(0,END)
        e11.insert(1,str(e11lover*dc1lover))        
    elif butpo1.get()=="/":
        e11.delete(0,END)
        e11.insert(1,str(e11lover/dc1lover))            
    elif butpo1.get()=="^":
        e11.delete(0,END)
        e11.insert(1,str(e11lover**dc1lover))            

def OPD():
    global qw1
    global dc1
    global lbvq
    global butpo1
    global r1q

    def bindow(self):

        c= lbvq.get(ANCHOR)
        try:
            if c=="sin :Deg":
                es=eval(dc1.get())
                con=math.radians(es)
                n= math.sin(con)
                dc1.delete(0,END)
                dc1.insert(1, str(n))


            elif c=="Use Func":
                qw1.destroy()
                AOF()
            
            elif c=="cos :Deg":
                es=eval(dc1.get())
                con=math.radians(es)
                n= math.cos(con)
                dc1.delete(0,END)
                dc1.insert(1, str(n))
            elif c=="tan :Deg":
                es=eval(dc1.get())
                con=math.radians(es)
                n= math.tan(con)
                dc1.delete(0,END)
                dc1.insert(1, str(n))
            elif c=="sin\u207B\u00B9 :Deg":
                es=eval(dc1.get())

                n= math.asin(es)
                n1=math.degrees(n)
                dc1.delete(0,END)
                dc1.insert(1, str(n1))
            elif c=="cos\u207B\u00B9 :Deg":
                es=eval(dc1.get())

                n= math.acos(es)
                n1=math.degrees(n)   
                dc1.delete(0,END)
                dc1.insert(1, str(n1))
            elif c=="tan\u207B\u00B9 :Deg":
                es=eval(dc1.get())

                n= math.atan(es)
                n1=math.degrees(n)
                dc1.delete(0,END)
                dc1.insert(1, str(n1))
            elif c=="sin :Rad":
                es=eval(dc1.get())
                
                n= math.sin(es)
                dc1.delete(0,END)
                dc1.insert(1, str(n))
            elif c=="cos :Rad":
                es=eval(dc1.get())

                n= math.sin(es)
                dc1.delete(0,END)
                dc1.insert(1, str(n))
            elif c=="tan :Rad":
                es=eval(dc1.get())

                n= math.sin(es)
                dc1.delete(0,END)
                dc1.insert(1, str(n))
            elif c=="sin\u207B\u00B9 :Rad":
                es=eval(dc1.get())

                n= math.asin(es)
                dc1.delete(0,END)
                dc1.insert(1, str(n
                                  ))
            elif c=="cos\u207B\u00B9 :Rad":
                es=eval(dc1.get())

                n= math.acos(es)
           
                dc1.delete(0,END)
                dc1.insert(1, str(n))
            elif c=="tan\u207B\u00B9 :Rad":
                es=eval(dc1.get())

                n= math.acos(es)

                dc1.delete(0,END)
                dc1.insert(1, str(n))

            elif c=="sinh":
                es=eval(dc1.get())

                n= math.sinh(es)
                dc1.delete(0,END)
                dc1.insert(1, str(n))
            elif c=="cosh":
                es=eval(dc1.get())
                con=math.radians(es)
                n= math.cosh(es)
                dc1.delete(0,END)
                dc1.insert(1, str(n))
            elif c=="tanh":
                es=eval(dc1.get())

                n= math.tanh(es)
                dc1.delete(0,END)
                dc1.insert(1, str(n))
            elif c=="sinh\u207B\u00B9":
                es=eval(dc1.get())

                n= math.asinh(es)
                dc1.delete(0,END)
                dc1.insert(1, str(n))
            elif c=="cosh\u207B\u00B9":
                es=eval(dc1.get())

                n= math.acosh(es)
                dc1.delete(0,END)
                dc1.insert(1, str(n))
            elif c=="tanh\u207B\u00B9":
                es=eval(dc1.get())

                n= math.atanh(es)
                dc1.delete(0,END)
                dc1.insert(1, str(n))
            elif c=="()":
                es=eval(dc1.get())
                
                dc1.delete(0,END)
                dc1.insert(1,"("+str(es)+")")

            elif c=="log":
                es=eval(dc1.get())
                n= math.log10(es)
                dc1.delete(0,END)
                dc1.inserted(1,str(n))
            elif c=="ln":
                es=eval(dc1.get())
                n= math.log1p(es)
                dc1.delete(0, END)
                dc1.insert(1,str(n))
            elif c=="log2":
                es=eval(dc1.get())
                n=math.log2(es)
                dc1.delete(0, END)
                dc1.insert(1,str(n))
            elif c=="antilog":
                es=eval(dc1.get())
                n=10**(es)
                dc1.delete(0, END)
                dc1.insert(1,str(n))
            elif c=="anti ln or e exponent":
                es=eval(dc1.get())
                n=2.71828**(es)
                dc1.delete(0, END)
                dc1.insert(1,str(n))
            elif c=="antilog2":
                es=eval(dc1.get())
                n=2**(es)
                dc1.delete(0, END)
                dc1.insert(1,str(n))
            elif c=="1/x":
                es=eval(dc1.get())
                n=1/es
                dc1.delete(0, END)
                dc1.insert(1,str(n))
            elif c=="√":
                es=eval(dc1.get())
                n=(es)**(1/2)
                dc1.delete(0, END)
                dc1.insert(1,str(n))
            elif c=="3√":
                es=eval(dc1.get())
                n=(es)**(1/3)
                dc1.delete(0, END)
                dc1.insert(1,str(n))
            elif c=="4√":
                es=eval(dc1.get())
                n=(es)**(1/4)
                dc1.delete(0, END)
                dc1.insert(1,str(n))
            elif c=="5√":
                es=eval(dc1.get())
                n=(es)**(1/5)
                dc1.delete(0, END)
                dc1.insert(1,str(n))
            elif c=="6√":
                es=eval(dc1.get())
                n=(es)**(1/6)
                dc1.delete(0, END)
                dc1.insert(1,str(n))

            elif c=="x\u00B2":
                es=eval(dc1.get())
                n=(es)**(2.0)
                dc1.delete(0, END)
                dc1.insert(1,str(n))
            elif c=="x\u00B3":
                es=eval(dc1.get())
                n=(es)**(3.0)
                dc1.delete(0, END)
                dc1.insert(1,str(n))
            elif c=="µ\u2091":
                dc1.insert(END, str(-9.2847*10**-24))
            elif c=="µ\u209A":
                dc1.insert(END, str(-1.4106*10**-26))
            elif c=="ρₐ\u1D62\u1D63":
                dc1.insert(END, str(1.2041))
            elif c=="\u210F":
                dc1.insert(END, str(1.05457163*10**-34))
            elif c=="h":
                dc1.insert(END, str(6.62606896*10**-34))
            elif c=="m\u209A":
                dc1.insert(END, str(1.672621637*10**-27))
            elif c=="m\u2091":
                dc1.insert(END, str(9.109382150*10**-31))
            elif c=="mµ":
                dc1.insert(END, str(1.8835313*10**-28))
            elif c=="m\u2099":
                dc1.insert(END, str(1.674927211*10**-27))
            elif c=="a\u2080":
                dc1.insert(END, str(5.291772086*10**-11))
            elif c=="g":
                dc1.insert(END, str(9.806650))
            elif c=="µN":
                dc1.insert(END, str(5.05078324*10**-27))
            elif c=="µB":
                dc1.insert(END, str(9.27400915*10**-24))
            elif c=="α":
                dc1.insert(END, str(7.297352538*10**-3))
            elif c=="r\u2091":
                dc1.insert(END, str(2.817940289*10**-15))
            elif c=="λc":
                dc1.insert(END, str(2.426310218*10**-12))
            elif c=="γp":
                dc1.insert(END, str(267522209.9))
            elif c=="λc,p":
                dc1.insert(END, str(1.321409845*10**-15))
            elif c=="λc,n":
                dc1.insert(END, str(1.319590895*10**-15))
            elif c=="R∞":
                dc1.insert(END, str(10973731.57))
            elif c=="u":
                dc1.insert(END, str(1.660538782*10**-27))
            elif c=="µ\u2099":
                dc1.insert(END, str(-9.6623641*10**-27))
            elif c=="µ\u1D64":
                dc1.insert(END, str(-4.49044786*10**-26))
            elif c=="F":
                dc1.insert(END, str(96485.3399))
            elif c=="e(maths)":
                dc1.insert(END, str(2.71828))
            elif c=="Avogadro(NA)":
                dc1.insert(END, str(6.02214179*10**23))
            elif c=="k":
                dc1.insert(END, str(1.3806504*10**-23))
            elif c=="Vm":
                dc1.insert(END, str(0.022413996))
            elif c=="R":
                dc1.insert(END, str(8.314472))
            elif c=="C\u2080":
                dc1.insert(END, str(299792458))
            elif c=="C\u2081":
                dc1.insert(END, str(3.74177118*10**-16))
            elif c=="C\u2082":
                dc1.insert(END, str(0.014387752))
            elif c=="σ":
                dc1.insert(END, str(5.5704*10**-8))
            elif c=="µ\u2080":
                dc1.insert(END, str(1.256637061*10**-34))
            elif c=="ϵ\u2080":
                dc1.insert(END, str(8.854187817*10**-12))
            elif c=="φ\u2080":
                dc1.insert(END, str(2.067833667*10**-15))
            elif c=="G\u2080":
                dc1.insert(END, str(7.7480917*10**-5))
            elif c=="Z\u2080":
                dc1.insert(END, str(376.7303135))
            elif c=="t(Kelvin Sci)":
                dc1.insert(END, str(273.15))
            elif c=="G":
                dc1.insert(END, str(6.62606896*10**-34))
            elif c=="atm":
                dc1.insert(END, str(1.013*10**5))
            elif c=="bar":
                dc1.insert(END, str(1.01325))
            elif c=="K(Kelvin)":
                dc1.insert(END, str(273))
            elif c=="e(electron)":
                dc1.insert(END, str(1.602176487*10**-19))
            elif c=="π":
                dc1.insert(END, str(3.141592654))
            elif c=="in -> cm":
                d=eval(dc1.get())*2.54
                dc1.delete(0, END)
                dc1.insert(1, str(d))
            elif c=="in <- cm":
                d=eval(dc1.get())/2.54
                dc1.delete(0, END)
                dc1.insert(1, str(d))

            elif c=="ft -> m":
                d=eval(dc1.get())*0.305
                dc1.delete(0, END)
                dc1.insert(1, str(d))        

            elif c=="ft <- m":
                d=eval(dc1.get())/0.305
                dc1.delete(0, END)
                dc1.insert(1, str(d))        

            elif c=="yd -> m":
                d= eval(dc1.get())*0.305*3
                dc1.delete(0,END)
                dc1.insert(1, str(d))
            
            elif c=="yd <- m":
                d= eval(dc1.get())/0.305/3
                dc1.delete(0,END)
                dc1.insert(1, str(d))
            
            elif c=="miles -> km":
                d=eval(dc1.get())*1.609
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            elif c=="miles <- km":
                d=eval(dc1.get())/1.609
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            elif c=="miles -> m":
                d=eval(dc1.get())*1609
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            elif c=="miles <- m":
                d=eval(dc1.get())/1609
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            #second slice of units convertion

            elif c=="acre -> m\u00B2":
                d= eval(dc1.get())*4046.856
                dc1.delete(0, END)
                dc1.insert(1, str(d))

            elif c=="acre <- m\u00B2":
                d= eval(dc1.get())/4046.856
                dc1.delete(0, END)
                dc1.insert(1, str(d))

            elif c=="gal(US standard) -> l":
                d= eval(dc1.get())*3.785
                dc1.delete(0, END)
                dc1.insert(1, str(d))

            elif c=="gal(US standard) <- l":
                d= eval(dc1.get())/3.785
                dc1.delete(0, END)
                dc1.insert(1, str(d))

            elif c=="gal(UK standard) -> l":
                d= eval(dc1.get())*4.546
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            elif c=="gal(UK standard) <- l":
                d= eval(dc1.get())/4.546
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            elif c=="pc -> km":
                d=eval(dc1.get())*3.086e13
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            elif c=="pc <- km":
                d=eval(dc1.get())/3.086e13
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            elif c=="m/s -> km/h":
                d= eval(dc1.get())*3.6
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            elif c=="m/s <- km/h":
                d= eval(dc1.get())/3.6
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            #3rd slice of unit conversion

            elif c=="oz -> g":
                d= eval(dc1.get())*28.35
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            elif c=="oz <- g":
                d= eval(dc1.get())/28.35
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            elif c=="lb -> kg":
                d= eval(dc1.get())*0.454
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            elif c=="lb <- kg":
                d= eval(dc1.get())/0.454
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            elif c=="atm -> Pa":
                d= eval(dc1.get())*1.01325e5
                dc1.delete(0, END)
                dc1.insert(1, str(d))

            elif c=="atm <- Pa":
                d= eval(dc1.get())/1.01325e5
                dc1.delete(0, END)
                dc1.insert(1, str(d))
                
            elif c=="mmHg -> Pa":
                d= eval(dc1.get())*133.322
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            elif c=="mmHg <- Pa":
                d= eval(dc1.get())/133.322
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            elif c=="hp -> kW":
                d= eval(dc1.get())*0.746
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            elif c=="hp <- kW":
                d= eval(dc1.get())/0.746
                dc1.delete(0,END)
                dc1.insert(1, str(d))

            #4th slice of units conversion

            elif c=="kgf/cm\u00B2 -> Pa":
                d= eval(dc1.get())*98066.5
                dc1.delete(0, END)
                dc1.insert(1, str(d))

            elif c=="kgf/cm\u00B2 <- Pa":
                d= eval(dc1.get())/98066.5
                dc1.delete(0, END)
                dc1.insert(1, str(d))

            elif c=="kgf.m -> J":
                d= eval(dc1.get())*9.81
                dc1.delete(0, END)
                dc1.insert(1, str(d))

            elif c=="kgf.m <- J":
                d= eval(dc1.get())/9.81
                dc1.delete(0, END)
                dc1.insert(1, str(d))

            elif c=="lbf/in\u00B2 -> kPa":
                d= eval(dc1.get())*6.895
                dc1.delete(0, END)
                dc1.insert(1, str(d))

            elif c=="lbf/in\u00B2 <- kPa":
                d= eval(dc1.get())/6.895
                dc1.delete(0, END)
                dc1.insert(1, str(d))

            elif c=="F\u00B0 -> C\u00B0":
                d= (eval(dc1.get())-32)*5/9
                dc1.delete(0, END)
                dc1.insert(1, str(d))

            elif c=="F\u00B0 <- C\u00B0":
                d= eval(dc1.get())*(9/5)+32
                dc1.delete(0, END)
                dc1.insert(1, str(d))

            elif c=="J -> cal":
                d= eval(dc1.get())*4.1842
                dc1.delete(0, END)
                dc1.insert(1, str(d))

            elif c=="J <- cal":
                d= eval(dc1.get())/4.1842
                dc1.delete(0, END)
                dc1.insert(1, str(d))
        except:
            dc1.insert(1,"Error")

    def addx1(oppiImaginge):
        dc1.insert(END,str(oppiImaginge))

    def eneg11():
        w=eval(dc1.get())
        e.delete(0,END)
        e.insert(1, -w)

    def Calc1():
        w=eval(dc1.get())
        dc1.delete(0,END)
        dc1.insert(1, str(w))

    qw1=Toplevel()
    
   
    qw1.config(bg="#1F1F1F")
    qw1.title("Functions")
    qw1.attributes('-topmost', 'true')


    r=Frame(qw1)
    r.grid(row=0,column=0, sticky=N)
    rs=LabelFrame(qw1,bg="#1F1F1F", fg="#40E0D0", border=0)
    rs.grid(row=0,column=1)
    rs1=LabelFrame(qw1,bg="#1F1F1F", fg="#40E0D0", border=0)
    rs1.grid(row=1,column=0,columnspan=2)
    
    lbvq= Listbox(r, bg="#1F1F1F", fg="#40E0D0",font="Consolas 12 ",background="#313335", foreground="#40E0D0")
    lbvq.pack(side=LEFT, expand='True', anchor="e", fill=BOTH)
    xro=Scrollbar(r, activebackground="gray", bg="#1F1F1F", bd=0, highlightbackground="#313335")
    
    xro.pack(side=RIGHT, expand='True', anchor="e",fill= Y)
    xro.configure(command=lbvq.yview)

    lbvq.configure(yscrollcommand=xro.set)
    lbvq.configure(height=14)

    lbvq.insert(END,"sin :Deg")
    lbvq.insert(END,"cos :Deg")
    lbvq.insert(END,"tan :Deg")
    lbvq.insert(END,"sin\u207B\u00B9 :Deg")
    lbvq.insert(END,"cos\u207B\u00B9 :Deg")
    lbvq.insert(END,"tan\u207B\u00B9 :Deg")
    lbvq.insert(END,"sin :Rad")
    lbvq.insert(END,"cos :Rad")
    lbvq.insert(END,"tan :Rad")
    lbvq.insert(END,"sin\u207B\u00B9 :Rad")
    lbvq.insert(END,"cos\u207B\u00B9 :Rad")
    lbvq.insert(END,"tan\u207B\u00B9 :Rad")

    lbvq.insert(END,"sinh")
    lbvq.insert(END,"cosh")
    lbvq.insert(END,"tanh")
    lbvq.insert(END,"sinh\u207B\u00B9")
    lbvq.insert(END,"cosh\u207B\u00B9")
    lbvq.insert(END,"tanh\u207B\u00B9")
    lbvq.insert(END,"log")
    lbvq.insert(END,"ln")
    lbvq.insert(END,"log2")
    lbvq.insert(END,"antilog")
    lbvq.insert(END,"anti ln or e exponent")
    lbvq.insert(END,"antilog2")

    lbvq.insert(END,"()")
    lbvq.insert(END,"1/x")
    lbvq.insert(END,"√")
    lbvq.insert(END,"3√")
    lbvq.insert(END,"4√")
    lbvq.insert(END,"5√")
    lbvq.insert(END,"6√")
    lbvq.insert(END,"x\u00B2")
    lbvq.insert(END,"x\u00B3")
    #The Constants
    lbvq.insert(END, "µ\u2091")
    lbvq.insert(END, "µ\u209A")
    lbvq.insert(END, "ρₐ\u1D62\u1D63")
    lbvq.insert(END, "\u210F")
    lbvq.insert(END, "h")
    lbvq.insert(END, "m\u209A")
    lbvq.insert(END, "m\u2091")
    lbvq.insert(END, "mµ")
    lbvq.insert(END, "m\u2099")
    lbvq.insert(END, "a\u2080")
    lbvq.insert(END, "g")
    lbvq.insert(END, "µN")
    lbvq.insert(END, "µB")
    lbvq.insert(END, "α")
    lbvq.insert(END, "r\u2091")
    lbvq.insert(END, "λc")
    lbvq.insert(END, "γp")
    lbvq.insert(END, "λc,p")
    lbvq.insert(END, "λc,n")
    lbvq.insert(END, "R∞")
    lbvq.insert(END, "u")
    lbvq.insert(END, "µ\u2099")
    lbvq.insert(END, "µ\u1D64")
    lbvq.insert(END, "F")
    lbvq.insert(END, "e(maths)")
    lbvq.insert(END, "Avogadro(NA)")
    lbvq.insert(END, "k")
    lbvq.insert(END, "Vm")
    lbvq.insert(END, "R")
    lbvq.insert(END, "C\u2080")
    lbvq.insert(END, "C\u2081")
    lbvq.insert(END, "C\u2082")
    lbvq.insert(END, "σ")
    lbvq.insert(END, "µ\u2080")
    lbvq.insert(END, "ϵ\u2080")
    lbvq.insert(END, "φ\u2080")
    lbvq.insert(END, "G\u2080")
    lbvq.insert(END, "Z\u2080")
    lbvq.insert(END, "t(Kelvin Sci)")    
    lbvq.insert(END, "G")    
    lbvq.insert(END, "atm")
    lbvq.insert(END, "bar")
    lbvq.insert(END, "K(Kelvin)")
    lbvq.insert(END, "e(electron)")
    lbvq.insert(END, "π")
    # Unit Chaning
    lbvq.insert(END, "in -> cm")
    lbvq.insert(END, "in <- cm")
    lbvq.insert(END, "ft -> m")
    lbvq.insert(END, "ft <- m")
    lbvq.insert(END, "yd -> m")
    lbvq.insert(END, "yd <- m")
    lbvq.insert(END, "miles -> km")
    lbvq.insert(END, "miles <- km")
    lbvq.insert(END, "miles -> km")
    lbvq.insert(END, "miles <- m")

    lbvq.insert(END, "acre -> m\u00B2")
    lbvq.insert(END, "acre <- m\u00B2")
    lbvq.insert(END, "gal(US standard) -> l")
    lbvq.insert(END, "gal(US standard) <- l")
    lbvq.insert(END, "gal(UK standard) -> l")
    lbvq.insert(END, "gal(UK standard) <- l")
    lbvq.insert(END, "pc -> km")
    lbvq.insert(END, "pc <- km")
    lbvq.insert(END, "m/s -> km/h")
    lbvq.insert(END, "m/s <- km/h")

    lbvq.insert(END, "oz -> g")
    lbvq.insert(END, "oz <- g")
    lbvq.insert(END, "lb -> kg")
    lbvq.insert(END, "lb <- kg")
    lbvq.insert(END, "atm -> Pa")
    lbvq.insert(END, "atm <- Pa")
    lbvq.insert(END, "mmHg -> Pa")
    lbvq.insert(END, "mmHg <- Pa")
    lbvq.insert(END, "hp -> kW")
    lbvq.insert(END, "hp <- kW")

    lbvq.insert(END, "kgf/cm\u00B2 -> Pa")
    lbvq.insert(END, "kgf/cm\u00B2 <- Pa")
    lbvq.insert(END, "kgf.m -> J")
    lbvq.insert(END, "kgf.m <- J")
    lbvq.insert(END, "lbf/in\u00B2 -> kPa")
    lbvq.insert(END, "lbf/in\u00B2 <- kPa")
    lbvq.insert(END, "F\u00B0 -> C\u00B0")
    lbvq.insert(END, "F\u00B0 <- C\u00B0")
    lbvq.insert(END, "J -> cal")
    lbvq.insert(END, "J <- cal")    

    # Binding the keyboard and mouse control
    lbvq.bind("<Double-Button-1>", bindow)
    


    dc1=Entry(rs , bg="#313335", fg="#40E0D0", font="Consolas 10 normal", border=0)
    dc1.grid(row=0, column=0, columnspan=4)

    but1e= Button(rs,text="1",command= lambda: addx1(1), bg="#313335",fg="#40E0D0",padx=19,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but2e= Button(rs,text="2",command= lambda: addx1(2), bg="#313335",fg="#40E0D0",padx=19,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but3e= Button(rs,text="3",command= lambda: addx1(3), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but4e= Button(rs,text="4",command= lambda: addx1(4), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but5e= Button(rs,text="5",command= lambda: addx1(5), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but6e= Button(rs,text="6",command=lambda: addx1(6), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but7e= Button(rs,text="7",command= lambda:addx1(7), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but8e= Button(rs,text="8",command= lambda:addx1(8), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but9e= Button(rs,text="9",command=lambda: addx1(9), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but0e= Button(rs,text="0",command=lambda: addx1(0), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    butde= Button(rs,text=".",command=lambda: addx1("."), bg="#313335",fg="#40E0D0",padx=21,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    butne= Button(rs,text="+/-",command=eneg11, bg="#313335",fg="#40E0D0",padx=14,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    
    
    
    but1e.grid(row=1, column=0, padx=8, pady=8)
    but2e.grid(row=1, column=1, padx=8, pady=8)
    but3e.grid(row=1, column=2, padx=8, pady=8)
    but4e.grid(row=2, column=0, padx=8, pady=8)
    but5e.grid(row=2, column=1, padx=8, pady=8)
    but6e.grid(row=2, column=2, padx=8, pady=8)
    but7e.grid(row=3, column=0, padx=8, pady=8)
    but8e.grid(row=3, column=1, padx=8, pady=8)
    but9e.grid(row=3, column=2, padx=8, pady=8)
    but0e.grid(row=4, column=1, padx=8, pady=8)
    butde.grid(row=4, column=0, padx=8, pady=8)
    butne.grid(row=4, column=2, padx=8, pady=8)

    buta= Button(rs,text="+",command=lambda: addx1("+"), bg="#3D3D3D",fg="#40E0D0",padx=19,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    buta.grid(row=1, column=3, padx=8, pady=8)
    buts= Button(rs,text="-",command=lambda: addx1("-"), bg="#3D3D3D",fg="#40E0D0",padx=20,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    buts.grid(row=2, column=3, padx=8, pady=8)
    butm= Button(rs,text="*",command=lambda: addx1("*"), bg="#3D3D3D",fg="#40E0D0",padx=21,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butm.grid(row=3, column=3, padx=8, pady=8)    
    butd= Button(rs,text="/",command=lambda: addx1("/"), bg="#3D3D3D",fg="#40E0D0",padx=22,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butd.grid(row=4, column=3, padx=8, pady=8)

    butcalc= Button(rs,text="=",command=Calc1, bg="#3D3D3D",fg="#40E0D0",padx=21,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butcalc.grid(row=1, column=4, padx=8, pady=8)
    butclr= Button(rs,text="AC",command=dc1deleter, bg="#3D3D3D",fg="#40E0D0",padx=12,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butclr.grid(row=2 ,column=4, padx=8, pady=8)
    butbcck= Button(rs,text="<-",command=dc1bcck, bg="#3D3D3D",fg="#40E0D0",padx=16,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butbcck.grid(row=3, column=4, padx=8, pady=8)
    butpoo= Button(rs,text="^",command=lambda: addx1("**"), bg="#3D3D3D",fg="#40E0D0",padx=20,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butpoo.grid(row=4, column=4, padx=8, pady=8)
    butAc= Button(rs1,text="Add to Ans",command=Way1, bg="#3D3D3D",fg="#40E0D0",padx=20,pady=13,borderwidth=4,font="Consolas 10 normal", border =0)    
    butAc.grid(row=0, column=2, padx=8, pady=8)
    butRR= Label(rs1,text="operation", bg="#1F1F1F",fg="#40E0D0",padx=20,pady=13,borderwidth=4,font="Consolas 10 normal", border =0)    
    butRR.grid(row=0, column=0, padx=8, pady=8)
    butpo1= ttk.Combobox(rs1,values=['+','-','*','/','^'],font="Consolas 10 normal")    
    butpo1.grid(row=0, column=1)
    butpo1.insert(1, "+")    

def functionsbind(self):
    global lbv
    global e11
    global r1q
    c=lbv.get(ANCHOR)
    try:
        if c=="sin :Deg":
            es=eval(e11.get())
            con=math.radians(es)
            n= math.sin(con)
            e11.delete(0,END)
            e11.insert(1, str(n))
        elif c=="Use Func":
            OPD()
            
        elif c=="cos :Deg":
            es=eval(e11.get())
            con=math.radians(es)
            n= math.cos(con)
            e11.delete(0,END)
            e11.insert(1, str(n))
        elif c=="tan :Deg":
            es=eval(e11.get())
            con=math.radians(es)
            n= math.tan(con)
            e11.delete(0,END)
            e11.insert(1, str(n))
        elif c=="sin\u207B\u00B9 :Deg":
            es=eval(e11.get())

            n= math.asin(es)
            n1=math.degrees(n)
            e11.delete(0,END)
            e11.insert(1, str(n1))
        elif c=="cos\u207B\u00B9 :Deg":
            es=eval(e11.get())

            n= math.acos(es)
            n1=math.degrees(n)   
            e11.delete(0,END)
            e11.insert(1, str(n1))
        elif c=="tan\u207B\u00B9 :Deg":
            es=eval(e11.get())

            n= math.atan(es)
            n1=math.degrees(n)
            e11.delete(0,END)
            e11.insert(1, str(n1))
        elif c=="sin :Rad":
            es=eval(e11.get())
            
            n= math.sin(es)
            e11.delete(0,END)
            e11.insert(1, str(n))
        elif c=="cos :Rad":
            es=eval(e11.get())

            n= math.sin(es)
            e11.delete(0,END)
            e11.insert(1, str(n))
        elif c=="tan :Rad":
            es=eval(e11.get())

            n= math.sin(es)
            e11.delete(0,END)
            e11.insert(1, str(n))
        elif c=="sin\u207B\u00B9 :Rad":
            es=eval(e11.get())

            n= math.asin(es)
            e11.delete(0,END)
            e11.insert(1, str(n
                              ))
        elif c=="cos\u207B\u00B9 :Rad":
            es=eval(e11.get())

            n= math.acos(es)
       
            e11.delete(0,END)
            e11.insert(1, str(n))
        elif c=="tan\u207B\u00B9 :Rad":
            es=eval(e11.get())

            n= math.acos(es)

            e11.delete(0,END)
            e11.insert(1, str(n))

        elif c=="sinh":
            es=eval(e11.get())

            n= math.sinh(es)
            e11.delete(0,END)
            e11.insert(1, str(n))
        elif c=="cosh":
            es=eval(e11.get())
            con=math.radians(es)
            n= math.cosh(es)
            e11.delete(0,END)
            e11.insert(1, str(n))
        elif c=="tanh":
            es=eval(e11.get())

            n= math.tanh(es)
            e11.delete(0,END)
            e11.insert(1, str(n))
        elif c=="sinh\u207B\u00B9":
            es=eval(e11.get())

            n= math.asinh(es)
            e11.delete(0,END)
            e11.insert(1, str(n))
        elif c=="cosh\u207B\u00B9":
            es=eval(e11.get())

            n= math.acosh(es)
            e11.delete(0,END)
            e11.insert(1, str(n))
        elif c=="tanh\u207B\u00B9":
            es=eval(e11.get())

            n= math.atanh(es)
            e11.delete(0,END)
            e11.insert(1, str(n))
        elif c=="()":
            es=eval(e11.get())
            
            e11.delete(0,END)
            e11.insert(1,"("+str(es)+")")
        elif c=="log":
            es=eval(e11.get())
            n= math.log10(es)
            e11.delete(0,END)
            e11.inserted(1,str(n))
        elif c=="ln":
            es=eval(e11.get())
            n= math.log1p(es)
            e11.delete(0, END)
            e11.insert(1,str(n))
        elif c=="log2":
            es=eval(e11.get())
            n=math.log2(es)
            e11.delete(0, END)
            e11.insert(1,str(n))
        elif c=="antilog":
            es=eval(e11.get())
            n=10**(es)
            e11.delete(0, END)
            e11.insert(1,str(n))
        elif c=="anti ln or e exponent":
            es=eval(e11.get())
            n=2.71828**(es)
            e11.delete(0, END)
            e11.insert(1,str(n))
        elif c=="antilog2":
            es=eval(e11.get())
            n=2**(es)
            e11.delete(0, END)
            e11.insert(1,str(n))
        elif c=="1/x":
            es=eval(e11.get())
            n=1/es
            e11.delete(0, END)
            e11.insert(1,str(n))
        elif c=="√":
            es=eval(e11.get())
            n=(es)**(1/2)
            e11.delete(0, END)
            e11.insert(1,str(n))
        elif c=="3√":
            es=eval(e11.get())
            n=(es)**(1/3)
            e11.delete(0, END)
            e11.insert(1,str(n))
        elif c=="4√":
            es=eval(e11.get())
            n=(es)**(1/4)
            e11.delete(0, END)
            e11insert(1,str(n))
        elif c=="5√":
            es=eval(e11.get())
            n=(es)**(1/5)
            e11.delete(0, END)
            e11.insert(1,str(n))
        elif c=="6√":
            es=eval(e11.get())
            n=(es)**(1/6)
            e11.delete(0, END)
            e11.insert(1,str(n))

        elif c=="x\u00B2":
            es=eval(e11.get())
            n=(es)**(2.0)
            e11.delete(0, END)
            e11.insert(1,str(n))
        elif c=="x\u00B3":
            es=eval(e11.get())
            n=(es)**(3.0)
            e11.delete(0, END)
            e11.insert(1,str(n))
                
        
    except:
        e11.insert(1,"Error")

    r1q.destroy()

def functions():
    global lbv
    global r1q
    r1q=Toplevel()
    
    r1q.config(bg="#1F1F1F")
    r1q.title("Constants")
    r1q.geometry("200x230")
    r=Frame(r1q)
    r.grid(row=0,column=0)
    lbv= Listbox(r, bg="#1F1F1F", fg="#40E0D0",font="Consolas 12 ",background="#313335", foreground="#40E0D0")
    lbv.pack(side=LEFT, expand='True', anchor="e", fill=BOTH)
    xro=Scrollbar(r, activebackground="gray", bg="#1F1F1F", bd=0, highlightbackground="#313335")
    
    xro.pack(side=RIGHT, expand='True', anchor="e",fill= Y)
    xro.configure(command=lbv.yview)

    lbv.configure(yscrollcommand=xro.set)

    lbv.insert(END,"sin :Deg")
    lbv.insert(END,"cos :Deg")
    lbv.insert(END,"tan :Deg")
    lbv.insert(END,"sin\u207B\u00B9 :Deg")
    lbv.insert(END,"cos\u207B\u00B9 :Deg")
    lbv.insert(END,"tan\u207B\u00B9 :Deg")
    lbv.insert(END,"sin :Rad")
    lbv.insert(END,"cos :Rad")
    lbv.insert(END,"tan :Rad")
    lbv.insert(END,"sin\u207B\u00B9 :Rad")
    lbv.insert(END,"cos\u207B\u00B9 :Rad")
    lbv.insert(END,"tan\u207B\u00B9 :Rad")

    lbv.insert(END,"sinh")
    lbv.insert(END,"cosh")
    lbv.insert(END,"tanh")
    lbv.insert(END,"sinh\u207B\u00B9")
    lbv.insert(END,"cosh\u207B\u00B9")
    lbv.insert(END,"tanh\u207B\u00B9")
    lbv.insert(END,"log")
    lbv.insert(END,"ln")
    lbv.insert(END,"log2")
    lbv.insert(END,"antilog")
    lbv.insert(END,"anti ln or e exponent")
    lbv.insert(END,"antilog2")

    lbv.insert(END,"()")
    lbv.insert(END,"1/x")
    lbv.insert(END,"√")
    lbv.insert(END,"3√")
    lbv.insert(END,"4√")
    lbv.insert(END,"5√")
    lbv.insert(END,"6√")
    lbv.insert(END,"x\u00B2")
    lbv.insert(END,"x\u00B3")
    lbv.insert(END,"Use Func")    


    lbv.bind('<Double-Button-1>', functionsbind)

    
def funct():
    global lbv1
    global r1
    r1=Toplevel()
   
    r1.config(bg="#1F1F1F")
    r1.title("Constants")
    r1.geometry("200x230")
    r=Frame(r1)
    r.grid(row=0,column=0)
    lbv1= Listbox(r, bg="#1F1F1F", fg="#40E0D0",font="Consolas 12 ",background="#313335", foreground="#40E0D0")
    lbv1.pack(side=LEFT, expand='True', anchor="e", fill=BOTH)
    xro=Scrollbar(r, activebackground="gray", bg="#1F1F1F", bd=0, highlightbackground="#313335")
    
    xro.pack(side=RIGHT, expand='True', anchor="e",fill= Y)
    xro.configure(command=lbv1.yview)

    lbv1.configure(yscrollcommand=xro.set)

    lbv1.insert(END,"sin :Deg")
    lbv1.insert(END,"cos :Deg")
    lbv1.insert(END,"tan :Deg")
    lbv1.insert(END,"sin\u207B\u00B9 :Deg")
    lbv1.insert(END,"cos\u207B\u00B9 :Deg")
    lbv1.insert(END,"tan\u207B\u00B9 :Deg")
    lbv1.insert(END,"sin :Rad")
    lbv1.insert(END,"cos :Rad")
    lbv1.insert(END,"tan :Rad")
    lbv1.insert(END,"sin\u207B\u00B9 :Rad")
    lbv1.insert(END,"cos\u207B\u00B9 :Rad")
    lbv1.insert(END,"tan\u207B\u00B9 :Rad")
 

    lbv1.insert(END,"sinh")
    lbv1.insert(END,"cosh")
    lbv1.insert(END,"tanh")
    lbv1.insert(END,"sinh\u207B\u00B9")
    lbv1.insert(END,"cosh\u207B\u00B9")
    lbv1.insert(END,"tanh\u207B\u00B9")

    lbv1.insert(END,"antilog")
    lbv1.insert(END,"anti ln or e exponent")
    lbv1.insert(END,"antilog2")    
    lbv1.insert(END,"()")
    lbv1.insert(END,"1/x")
    lbv1.insert(END,"√")
    lbv1.insert(END,"3√")
    lbv1.insert(END,"4√")
    lbv1.insert(END,"5√")
    lbv1.insert(END,"6√")
    lbv1.insert(END,"x\u00B2")
    lbv1.insert(END,"x\u00B3")
    lbv1.insert(END,"Use Func")

    lbv1.bind('<Double-Button-1>', functionsbindori)


def addx(obj):
    global dc
    dc.insert(END, str(obj))

def Calc1():
    global dc
    zx= eval(dc.get())
    dc.delete(0, END)
    dc.insert(1, str(zx))

def eneg1():
    global dc
    cv= eval(dc.get())
    dc.insert(END, str(-d))

def dcdeleter():
    global dc
    dc.delete(0, END)

def dcbcck():
    global dc
    cfg= str(dc.get())
    cv= re.split("([\d\+\-\/\*\(\)])", cfg )
    cv.pop()
    cv.pop()
    cd= "".join(cv)
    dc.delete(0, END)
    dc.insert(1, str(cd))    

def Way():
    global dc
    dclover= eval(dc.get())
    EQ()
    global lbvq
    global butpo
    elover=eval(e.get())

    if butpo.get()=="+":
        e.delete(0,END)
        e.insert(1,str(elover+dclover))
    elif butpo.get()=="-":
        e.delete(0,END)
        e.insert(1,str(elover-dclover))
    elif butpo.get()=="*":
        e.delete(0,END)
        e.insert(1,str(elover*dclover))        
    elif butpo.get()=="/":
        e.delete(0,END)
        e.insert(1,str(elover/dclover))            
    elif butpo.get()=="^":
        e.delete(0,END)
        e.insert(1,str(elover**dclover))            
    
    

def AOF():
    global qw
    global dc
    global lbvq
    global butpo

    def bindo(self):

        c= lbvq.get(ANCHOR)
        try:
            if c=="sin :Deg":
                es=eval(dc.get())
                con=math.radians(es)
                n= math.sin(con)
                dc.delete(0,END)
                dc.insert(1, str(n))

            elif c=="Use Func":
                AOF()
            
            elif c=="cos :Deg":
                es=eval(dc.get())
                con=math.radians(es)
                n= math.cos(con)
                dc.delete(0,END)
                dc.insert(1, str(n))
            elif c=="tan :Deg":
                es=eval(dc.get())
                con=math.radians(es)
                n= math.tan(con)
                dc.delete(0,END)
                dc.insert(1, str(n))
            elif c=="sin\u207B\u00B9 :Deg":
                es=eval(dc.get())

                n= math.asin(es)
                n1=math.degrees(n)
                dc.delete(0,END)
                dc.insert(1, str(n1))
            elif c=="cos\u207B\u00B9 :Deg":
                es=eval(dc.get())

                n= math.acos(es)
                n1=math.degrees(n)   
                dc.delete(0,END)
                dc.insert(1, str(n1))
            elif c=="tan\u207B\u00B9 :Deg":
                es=eval(dc.get())

                n= math.atan(es)
                n1=math.degrees(n)
                dc.delete(0,END)
                dc.insert(1, str(n1))
            elif c=="sin :Rad":
                es=eval(dc.get())
                
                n= math.sin(es)
                dc.delete(0,END)
                dc.insert(1, str(n))
            elif c=="cos :Rad":
                es=eval(dc.get())

                n= math.sin(es)
                dc.delete(0,END)
                dc.insert(1, str(n))
            elif c=="tan :Rad":
                es=eval(dc.get())

                n= math.sin(es)
                dc.delete(0,END)
                dc.insert(1, str(n))
            elif c=="sin\u207B\u00B9 :Rad":
                es=eval(dc.get())

                n= math.asin(es)
                dc.delete(0,END)
                dc.insert(1, str(n
                                  ))
            elif c=="cos\u207B\u00B9 :Rad":
                es=eval(dc.get())

                n= math.acos(es)
           
                dc.delete(0,END)
                dc.insert(1, str(n))
            elif c=="tan\u207B\u00B9 :Rad":
                es=eval(dc.get())

                n= math.acos(es)

                dc.delete(0,END)
                dc.insert(1, str(n))

            elif c=="sinh":
                es=eval(dc.get())

                n= math.sinh(es)
                dc.delete(0,END)
                dc.insert(1, str(n))
            elif c=="cosh":
                es=eval(dc.get())
                con=math.radians(es)
                n= math.cosh(es)
                dc.delete(0,END)
                dc.insert(1, str(n))
            elif c=="tanh":
                es=eval(dc.get())

                n= math.tanh(es)
                dc.delete(0,END)
                dc.insert(1, str(n))
            elif c=="sinh\u207B\u00B9":
                es=eval(dc.get())

                n= math.asinh(es)
                dc.delete(0,END)
                dc.insert(1, str(n))
            elif c=="cosh\u207B\u00B9":
                es=eval(dc.get())

                n= math.acosh(es)
                dc.delete(0,END)
                dc.insert(1, str(n))
            elif c=="tanh\u207B\u00B9":
                es=eval(dc.get())

                n= math.atanh(es)
                dc.delete(0,END)
                dc.insert(1, str(n))
            elif c=="()":
                es=eval(dc.get())
                
                dc.delete(0,END)
                dc.insert(1,"("+str(es)+")")

            elif c=="log":
                es=eval(dc.get())
                n= math.log10(es)
                dc.delete(0,END)
                dc.inserted(1,str(n))
            elif c=="ln":
                es=eval(dc.get())
                n= math.log1p(es)
                dc.delete(0, END)
                dc.insert(1,str(n))
            elif c=="log2":
                es=eval(dc.get())
                n=math.log2(es)
                dc.delete(0, END)
                dc.insert(1,str(n))
            elif c=="antilog":
                es=eval(dc.get())
                n=10**(es)
                dc.delete(0, END)
                dc.insert(1,str(n))
            elif c=="anti ln or e exponent":
                es=eval(dc.get())
                n=2.71828**(es)
                dc.delete(0, END)
                dc.insert(1,str(n))
            elif c=="antilog2":
                es=eval(dc.get())
                n=2**(es)
                dc.delete(0, END)
                dc.insert(1,str(n))
            elif c=="1/x":
                es=eval(dc.get())
                n=1/es
                dc.delete(0, END)
                dc.insert(1,str(n))
            elif c=="√":
                es=eval(dc.get())
                n=(es)**(1/2)
                dc.delete(0, END)
                dc.insert(1,str(n))
            elif c=="3√":
                es=eval(dc.get())
                n=(es)**(1/3)
                dc.delete(0, END)
                dc.insert(1,str(n))
            elif c=="4√":
                es=eval(dc.get())
                n=(es)**(1/4)
                dc.delete(0, END)
                dc.insert(1,str(n))
            elif c=="5√":
                es=eval(dc.get())
                n=(es)**(1/5)
                dc.delete(0, END)
                dc.insert(1,str(n))
            elif c=="6√":
                es=eval(dc.get())
                n=(es)**(1/6)
                dc.delete(0, END)
                dc.insert(1,str(n))

            elif c=="x\u00B2":
                es=eval(dc.get())
                n=(es)**(2.0)
                dc.delete(0, END)
                dc.insert(1,str(n))
            elif c=="x\u00B3":
                es=eval(dc.get())
                n=(es)**(3.0)
                dc.delete(0, END)
                dc.insert(1,str(n))
            
            elif c=="µ\u2091":
                dc.insert(END, str(-9.2847*10**-24))
            elif c=="µ\u209A":
                dc.insert(END, str(-1.4106*10**-26))
            elif c=="ρₐ\u1D62\u1D63":
                dc.insert(END, str(1.2041))
            elif c=="\u210F":
                dc.insert(END, str(1.05457163*10**-34))
            elif c=="h":
                dc.insert(END, str(6.62606896*10**-34))
            elif c=="m\u209A":
                dc.insert(END, str(1.672621637*10**-27))
            elif c=="m\u2091":
                dc.insert(END, str(9.109382150*10**-31))
            elif c=="mµ":
                dc.insert(END, str(1.8835313*10**-28))
            elif c=="m\u2099":
                dc.insert(END, str(1.674927211*10**-27))
            elif c=="a\u2080":
                dc.insert(END, str(5.291772086*10**-11))
            elif c=="g":
                dc.insert(END, str(9.806650))
            elif c=="µN":
                dc.insert(END, str(5.05078324*10**-27))
            elif c=="µB":
                dc.insert(END, str(9.27400915*10**-24))
            elif c=="α":
                dc.insert(END, str(7.297352538*10**-3))
            elif c=="r\u2091":
                dc.insert(END, str(2.817940289*10**-15))
            elif c=="λc":
                dc.insert(END, str(2.426310218*10**-12))
            elif c=="γp":
                dc.insert(END, str(267522209.9))
            elif c=="λc,p":
                dc.insert(END, str(1.321409845*10**-15))
            elif c=="λc,n":
                dc.insert(END, str(1.319590895*10**-15))
            elif c=="R∞":
                dc.insert(END, str(10973731.57))
            elif c=="u":
                dc.insert(END, str(1.660538782*10**-27))
            elif c=="µ\u2099":
                dc.insert(END, str(-9.6623641*10**-27))
            elif c=="µ\u1D64":
                dc.insert(END, str(-4.49044786*10**-26))
            elif c=="F":
                dc.insert(END, str(96485.3399))
            elif c=="e(maths)":
                dc.insert(END, str(2.71828))
            elif c=="Avogadro(NA)":
                dc.insert(END, str(6.02214179*10**23))
            elif c=="k":
                dc.insert(END, str(1.3806504*10**-23))
            elif c=="Vm":
                dc.insert(END, str(0.022413996))
            elif c=="R":
                dc.insert(END, str(8.314472))
            elif c=="C\u2080":
                dc.insert(END, str(299792458))
            elif c=="C\u2081":
                dc.insert(END, str(3.74177118*10**-16))
            elif c=="C\u2082":
                dc.insert(END, str(0.014387752))
            elif c=="σ":
                dc.insert(END, str(5.5704*10**-8))
            elif c=="µ\u2080":
                dc.insert(END, str(1.256637061*10**-34))
            elif c=="ϵ\u2080":
                dc.insert(END, str(8.854187817*10**-12))
            elif c=="φ\u2080":
                dc.insert(END, str(2.067833667*10**-15))
            elif c=="G\u2080":
                dc.insert(END, str(7.7480917*10**-5))
            elif c=="Z\u2080":
                dc.insert(END, str(376.7303135))
            elif c=="t(Kelvin Sci)":
                dc.insert(END, str(273.15))
            elif c=="G":
                dc.insert(END, str(6.62606896*10**-34))
            elif c=="atm":
                dc.insert(END, str(1.013*10**5))
            elif c=="bar":
                dc.insert(END, str(1.01325))
            elif c=="K(Kelvin)":
                dc.insert(END, str(273))
            elif c=="e(electron)":
                dc.insert(END, str(1.602176487*10**-19))
            elif c=="π":
                dc.insert(END, str(3.141592654))
            #1st slice of unit conversion
            elif c=="in -> cm":
                d=eval(dc.get())*2.54
                dc.delete(0, END)
                dc.insert(1, str(d))
            elif c=="in <- cm":
                d=eval(dc.get())/2.54
                dc.delete(0, END)
                dc.insert(1, str(d))

            elif c=="ft -> m":
                d=eval(dc.get())*0.305
                dc.delete(0, END)
                dc.insert(1, str(d))        

            elif c=="ft <- m":
                d=eval(dc.get())/0.305
                dc.delete(0, END)
                dc.insert(1, str(d))        

            elif c=="yd -> m":
                d= eval(dc.get())*0.305*3
                dc.delete(0,END)
                dc.insert(1, str(d))
            
            elif c=="yd <- m":
                d= eval(dc.get())/0.305/3
                dc.delete(0,END)
                dc.insert(1, str(d))
            
            elif c=="miles -> km":
                d=eval(dc.get())*1.609
                dc.delete(0,END)
                dc.insert(1, str(d))

            elif c=="miles <- km":
                d=eval(dc.get())/1.609
                dc.delete(0,END)
                dc.insert(1, str(d))

            elif c=="miles -> m":
                d=eval(dc.get())*1609
                dc.delete(0,END)
                dc.insert(1, str(d))

            elif c=="miles <- m":
                d=eval(dc.get())/1609
                dc.delete(0,END)
                dc.insert(1, str(d))

            #second slice of units convertion

            elif c=="acre -> m\u00B2":
                d= eval(dc.get())*4046.856
                dc.delete(0, END)
                dc.insert(1, str(d))

            elif c=="acre <- m\u00B2":
                d= eval(dc.get())/4046.856
                dc.delete(0, END)
                dc.insert(1, str(d))

            elif c=="gal(US standard) -> l":
                d= eval(dc.get())*3.785
                dc.delete(0, END)
                dc.insert(1, str(d))

            elif c=="gal(US standard) <- l":
                d= eval(dc.get())/3.785
                dc.delete(0, END)
                dc.insert(1, str(d))

            elif c=="gal(UK standard) -> l":
                d= eval(dc.get())*4.546
                dc.delete(0,END)
                dc.insert(1, str(d))

            elif c=="gal(UK standard) <- l":
                d= eval(dc.get())/4.546
                dc.delete(0,END)
                dc.insert(1, str(d))

            elif c=="pc -> km":
                d=eval(dc.get())*3.086e13
                dc.delete(0,END)
                dc.insert(1, str(d))

            elif c=="pc <- km":
                d=eval(dc.get())/3.086e13
                dc.delete(0,END)
                dc.insert(1, str(d))

            elif c=="m/s -> km/h":
                d= eval(dc.get())*3.6
                dc.delete(0,END)
                dc.insert(1, str(d))

            elif c=="m/s <- km/h":
                d= eval(dc.get())/3.6
                dc.delete(0,END)
                dc.insert(1, str(d))

            #3rd slice of unit conversion

            elif c=="oz -> g":
                d= eval(dc.get())*28.35
                dc.delete(0,END)
                dc.insert(1, str(d))

            elif c=="oz <- g":
                d= eval(dc.get())/28.35
                dc.delete(0,END)
                dc.insert(1, str(d))

            elif c=="lb -> kg":
                d= eval(dc.get())*0.454
                dc.delete(0,END)
                dc.insert(1, str(d))

            elif c=="lb <- kg":
                d= eval(dc.get())/0.454
                dc.delete(0,END)
                dc.insert(1, str(d))

            elif c=="atm -> Pa":
                d= eval(dc.get())*1.01325e5
                dc.delete(0, END)
                dc.insert(1, str(d))

            elif c=="atm <- Pa":
                d= eval(dc.get())/1.01325e5
                dc.delete(0, END)
                dc.insert(1, str(d))
                
            elif c=="mmHg -> Pa":
                d= eval(dc.get())*133.322
                dc.delete(0,END)
                dc.insert(1, str(d))

            elif c=="mmHg <- Pa":
                d= eval(dc.get())/133.322
                dc.delete(0,END)
                dc.insert(1, str(d))

            elif c=="hp -> kW":
                d= eval(dc.get())*0.746
                dc.delete(0,END)
                dc.insert(1, str(d))

            elif c=="hp <- kW":
                d= eval(dc.get())/0.746
                dc.delete(0,END)
                dc.insert(1, str(d))

            #4th slice of units conversion

            elif c=="kgf/cm\u00B2 -> Pa":
                d= eval(dc.get())*98066.5
                dc.delete(0, END)
                dc.insert(1, str(d))

            elif c=="kgf/cm\u00B2 <- Pa":
                d= eval(dc.get())/98066.5
                dc.delete(0, END)
                dc.insert(1, str(d))

            elif c=="kgf.m -> J":
                d= eval(dc.get())*9.81
                dc.delete(0, END)
                dc.insert(1, str(d))

            elif c=="kgf.m <- J":
                d= eval(dc.get())/9.81
                dc.delete(0, END)
                dc.insert(1, str(d))

            elif c=="lbf/in\u00B2 -> kPa":
                d= eval(dc.get())*6.895
                dc.delete(0, END)
                dc.insert(1, str(d))

            elif c=="lbf/in\u00B2 <- kPa":
                d= eval(dc.get())/6.895
                dc.delete(0, END)
                dc.insert(1, str(d))

            elif c=="F\u00B0 -> C\u00B0":
                d= (eval(dc.get())-32)*5/9
                dc.delete(0, END)
                dc.insert(1, str(d))

            elif c=="F\u00B0 <- C\u00B0":
                d= eval(dc.get())*(9/5)+32
                dc.delete(0, END)
                dc.insert(1, str(d))

            elif c=="J -> cal":
                d= eval(dc.get())*4.1842
                dc.delete(0, END)
                dc.insert(1, str(d))

            elif c=="J <- cal":
                d= eval(dc.get())/4.1842
                dc.delete(0, END)
                dc.insert(1, str(d))
                                        
        except:
            dc.insert(1,"Error")

    qw=Tk()
    
    

    qw.config(bg="#1F1F1F")
    qw.title("Functions")
    qw.attributes('-topmost', 'true')
    r=Frame(qw)
    r.grid(row=0,column=0, sticky=N)
    rs=LabelFrame(qw,bg="#1F1F1F", fg="#40E0D0", border=0)
    rs.grid(row=0,column=1)
    rs1=LabelFrame(qw,bg="#1F1F1F", fg="#40E0D0", border=0)
    rs1.grid(row=1,column=0,columnspan=2)
    
    lbvq= Listbox(r, bg="#1F1F1F", fg="#40E0D0",font="Consolas 12 ",background="#313335", foreground="#40E0D0")
    lbvq.pack(side=LEFT, expand='True', anchor="e", fill=BOTH)
    xro=Scrollbar(r, activebackground="gray", bg="#1F1F1F", bd=0, highlightbackground="#313335")
    
    xro.pack(side=RIGHT, expand='True', anchor="e",fill= Y)
    xro.configure(command=lbvq.yview)

    lbvq.configure(yscrollcommand=xro.set)
    lbvq.configure(height=14)

    lbvq.insert(END,"sin :Deg")
    lbvq.insert(END,"cos :Deg")
    lbvq.insert(END,"tan :Deg")
    lbvq.insert(END,"sin\u207B\u00B9 :Deg")
    lbvq.insert(END,"cos\u207B\u00B9 :Deg")
    lbvq.insert(END,"tan\u207B\u00B9 :Deg")
    lbvq.insert(END,"sin :Rad")
    lbvq.insert(END,"cos :Rad")
    lbvq.insert(END,"tan :Rad")
    lbvq.insert(END,"sin\u207B\u00B9 :Rad")
    lbvq.insert(END,"cos\u207B\u00B9 :Rad")
    lbvq.insert(END,"tan\u207B\u00B9 :Rad")

    lbvq.insert(END,"sinh")
    lbvq.insert(END,"cosh")
    lbvq.insert(END,"tanh")
    lbvq.insert(END,"sinh\u207B\u00B9")
    lbvq.insert(END,"cosh\u207B\u00B9")
    lbvq.insert(END,"tanh\u207B\u00B9")
    lbvq.insert(END,"log")
    lbvq.insert(END,"ln")
    lbvq.insert(END,"log2")
    lbvq.insert(END,"antilog")
    lbvq.insert(END,"anti ln or e exponent")
    lbvq.insert(END,"antilog2")

    lbvq.insert(END,"()")
    lbvq.insert(END,"1/x")
    lbvq.insert(END,"√")
    lbvq.insert(END,"3√")
    lbvq.insert(END,"4√")
    lbvq.insert(END,"5√")
    lbvq.insert(END,"6√")
    lbvq.insert(END,"x\u00B2")
    lbvq.insert(END,"x\u00B3")

    #Constant 
    lbvq.insert(END, "µ\u2091")
    lbvq.insert(END, "µ\u209A")
    lbvq.insert(END, "ρₐ\u1D62\u1D63")
    lbvq.insert(END, "\u210F")
    lbvq.insert(END, "h")
    lbvq.insert(END, "m\u209A")
    lbvq.insert(END, "m\u2091")
    lbvq.insert(END, "mµ")
    lbvq.insert(END, "m\u2099")
    lbvq.insert(END, "a\u2080")
    lbvq.insert(END, "g")
    lbvq.insert(END, "µN")
    lbvq.insert(END, "µB")
    lbvq.insert(END, "α")
    lbvq.insert(END, "r\u2091")
    lbvq.insert(END, "λc")
    lbvq.insert(END, "γp")
    lbvq.insert(END, "λc,p")
    lbvq.insert(END, "λc,n")
    lbvq.insert(END, "R∞")
    lbvq.insert(END, "u")
    lbvq.insert(END, "µ\u2099")
    lbvq.insert(END, "µ\u1D64")
    lbvq.insert(END, "F")
    lbvq.insert(END, "e(maths)")
    lbvq.insert(END, "Avogadro(NA)")
    lbvq.insert(END, "k")
    lbvq.insert(END, "Vm")
    lbvq.insert(END, "R")
    lbvq.insert(END, "C\u2080")
    lbvq.insert(END, "C\u2081")
    lbvq.insert(END, "C\u2082")
    lbvq.insert(END, "σ")
    lbvq.insert(END, "µ\u2080")
    lbvq.insert(END, "ϵ\u2080")
    lbvq.insert(END, "φ\u2080")
    lbvq.insert(END, "G\u2080")
    lbvq.insert(END, "Z\u2080")
    lbvq.insert(END, "t(Kelvin Sci)")    
    lbvq.insert(END, "G")    
    lbvq.insert(END, "atm")
    lbvq.insert(END, "bar")
    lbvq.insert(END, "K(Kelvin)")
    lbvq.insert(END, "e(electron)")
    lbvq.insert(END, "π")    
    lbvq.bind("<Double-Button-1>", bindo)
    #Unit Changing
    
    lbvq.insert(END, "in -> cm")
    lbvq.insert(END, "in <- cm")
    lbvq.insert(END, "ft -> m")
    lbvq.insert(END, "ft <- m")
    lbvq.insert(END, "yd -> m")
    lbvq.insert(END, "yd <- m")
    lbvq.insert(END, "miles -> km")
    lbvq.insert(END, "miles <- km")
    lbvq.insert(END, "miles -> km")
    lbvq.insert(END, "miles <- m")

    lbvq.insert(END, "acre -> m\u00B2")
    lbvq.insert(END, "acre <- m\u00B2")
    lbvq.insert(END, "gal(US standard) -> l")
    lbvq.insert(END, "gal(US standard) <- l")
    lbvq.insert(END, "gal(UK standard) -> l")
    lbvq.insert(END, "gal(UK standard) <- l")
    lbvq.insert(END, "pc -> km")
    lbvq.insert(END, "pc <- km")
    lbvq.insert(END, "m/s -> km/h")
    lbvq.insert(END, "m/s <- km/h")

    lbvq.insert(END, "oz -> g")
    lbvq.insert(END, "oz <- g")
    lbvq.insert(END, "lb -> kg")
    lbvq.insert(END, "lb <- kg")
    lbvq.insert(END, "atm -> Pa")
    lbvq.insert(END, "atm <- Pa")
    lbvq.insert(END, "mmHg -> Pa")
    lbvq.insert(END, "mmHg <- Pa")
    lbvq.insert(END, "hp -> kW")
    lbvq.insert(END, "hp <- kW")

    lbvq.insert(END, "kgf/cm\u00B2 -> Pa")
    lbvq.insert(END, "kgf/cm\u00B2 <- Pa")
    lbvq.insert(END, "kgf.m -> J")
    lbvq.insert(END, "kgf.m <- J")
    lbvq.insert(END, "lbf/in\u00B2 -> kPa")
    lbvq.insert(END, "lbf/in\u00B2 <- kPa")
    lbvq.insert(END, "F\u00B0 -> C\u00B0")
    lbvq.insert(END, "F\u00B0 <- C\u00B0")
    lbvq.insert(END, "J -> cal")
    lbvq.insert(END, "J <- cal")

    dc=Entry(rs , bg="#313335", fg="#40E0D0", font="Consolas 10 normal", border=0)
    dc.grid(row=0, column=0, columnspan=4)

    but1e= Button(rs,text="1",command= lambda: addx(1), bg="#313335",fg="#40E0D0",padx=19,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but2e= Button(rs,text="2",command= lambda: addx(2), bg="#313335",fg="#40E0D0",padx=19,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but3e= Button(rs,text="3",command= lambda: addx(3), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but4e= Button(rs,text="4",command= lambda: addx(4), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but5e= Button(rs,text="5",command= lambda: addx(5), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but6e= Button(rs,text="6",command=lambda: addx(6), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but7e= Button(rs,text="7",command= lambda:addx(7), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but8e= Button(rs,text="8",command= lambda:addx(8), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but9e= Button(rs,text="9",command=lambda: addx(9), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but0e= Button(rs,text="0",command=lambda: addx(0), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    butde= Button(rs,text=".",command=lambda: addx("."), bg="#313335",fg="#40E0D0",padx=21,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    butne= Button(rs,text="+/-",command=eneg1, bg="#313335",fg="#40E0D0",padx=14,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    
    
    
    but1e.grid(row=1, column=0, padx=8, pady=8)
    but2e.grid(row=1, column=1, padx=8, pady=8)
    but3e.grid(row=1, column=2, padx=8, pady=8)
    but4e.grid(row=2, column=0, padx=8, pady=8)
    but5e.grid(row=2, column=1, padx=8, pady=8)
    but6e.grid(row=2, column=2, padx=8, pady=8)
    but7e.grid(row=3, column=0, padx=8, pady=8)
    but8e.grid(row=3, column=1, padx=8, pady=8)
    but9e.grid(row=3, column=2, padx=8, pady=8)
    but0e.grid(row=4, column=1, padx=8, pady=8)
    butde.grid(row=4, column=0, padx=8, pady=8)
    butne.grid(row=4, column=2, padx=8, pady=8)

    buta= Button(rs,text="+",command=lambda: addx("+"), bg="#3D3D3D",fg="#40E0D0",padx=19,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    buta.grid(row=1, column=3, padx=8, pady=8)
    buts= Button(rs,text="-",command=lambda: addx("-"), bg="#3D3D3D",fg="#40E0D0",padx=20,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    buts.grid(row=2, column=3, padx=8, pady=8)
    butm= Button(rs,text="*",command=lambda: addx("*"), bg="#3D3D3D",fg="#40E0D0",padx=21,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butm.grid(row=3, column=3, padx=8, pady=8)    
    butd= Button(rs,text="/",command=lambda: addx("/"), bg="#3D3D3D",fg="#40E0D0",padx=22,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butd.grid(row=4, column=3, padx=8, pady=8)

    butcalc= Button(rs,text="=",command=Calc1, bg="#3D3D3D",fg="#40E0D0",padx=21,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butcalc.grid(row=1, column=4, padx=8, pady=8)
    butclr= Button(rs,text="AC",command=dcdeleter, bg="#3D3D3D",fg="#40E0D0",padx=12,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butclr.grid(row=2 ,column=4, padx=8, pady=8)
    butbcck= Button(rs,text="<-",command=dcbcck, bg="#3D3D3D",fg="#40E0D0",padx=16,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butbcck.grid(row=3, column=4, padx=8, pady=8)
    butpoo= Button(rs,text="^",command=lambda: addx("**"), bg="#3D3D3D",fg="#40E0D0",padx=20,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butpoo.grid(row=4, column=4, padx=8, pady=8)
    butAc= Button(rs1,text="Add to Ans",command=Way, bg="#3D3D3D",fg="#40E0D0",padx=20,pady=13,borderwidth=4,font="Consolas 10 normal", border =0)    
    butAc.grid(row=0, column=2, padx=8, pady=8)
    butRR= Label(rs1,text="operation", bg="#1F1F1F",fg="#40E0D0",padx=20,pady=13,borderwidth=4,font="Consolas 10 normal", border =0)    
    butRR.grid(row=0, column=0, padx=8, pady=8)
    butpo= ttk.Combobox(rs1,values=['+','-','*','/','^'],font="Consolas 10 normal")    
    butpo.grid(row=0, column=1)
    butpo.insert(1, "+")

def functionsbindori(self):
    global lbv1
    global r11

    c=lbv1.get(ANCHOR)
    try:
        if c=="sin :Deg":
            es=eval(e.get())
            con=math.radians(es)
            n= math.sin(con)
            e.delete(0,END)
            e.insert(1, str(n))

        elif c=="Use Func":
            AOF()
        
        elif c=="cos :Deg":
            es=eval(e.get())
            con=math.radians(es)
            n= math.cos(con)
            e.delete(0,END)
            e.insert(1, str(n))
        elif c=="tan :Deg":
            es=eval(e.get())
            con=math.radians(es)
            n= math.tan(con)
            e.delete(0,END)
            e.insert(1, str(n))
        elif c=="sin\u207B\u00B9 :Deg":
            es=eval(e.get())

            n= math.asin(es)
            n1=math.degrees(n)
            e.delete(0,END)
            e.insert(1, str(n1))
        elif c=="cos\u207B\u00B9 :Deg":
            es=eval(e.get())

            n= math.acos(es)
            n1=math.degrees(n)   
            e.delete(0,END)
            e.insert(1, str(n1))
        elif c=="tan\u207B\u00B9 :Deg":
            es=eval(e.get())

            n= math.atan(es)
            n1=math.degrees(n)
            e.delete(0,END)
            e.insert(1, str(n1))
        elif c=="sin :Rad":
            es=eval(e.get())
            
            n= math.sin(es)
            e.delete(0,END)
            e.insert(1, str(n))
        elif c=="cos :Rad":
            es=eval(e.get())

            n= math.sin(es)
            e.delete(0,END)
            e.insert(1, str(n))
        elif c=="tan :Rad":
            es=eval(e.get())

            n= math.sin(es)
            e.delete(0,END)
            e.insert(1, str(n))
        elif c=="sin\u207B\u00B9 :Rad":
            es=eval(e.get())

            n= math.asin(es)
            e.delete(0,END)
            e.insert(1, str(n
                              ))
        elif c=="cos\u207B\u00B9 :Rad":
            es=eval(e.get())

            n= math.acos(es)
       
            e.delete(0,END)
            e.insert(1, str(n))
        elif c=="tan\u207B\u00B9 :Rad":
            es=eval(e.get())

            n= math.acos(es)

            e.delete(0,END)
            e.insert(1, str(n))

        elif c=="sinh":
            es=eval(e.get())

            n= math.sinh(es)
            e.delete(0,END)
            e.insert(1, str(n))
        elif c=="cosh":
            es=eval(e.get())
            con=math.radians(es)
            n= math.cosh(es)
            e.delete(0,END)
            e.insert(1, str(n))
        elif c=="tanh":
            es=eval(e.get())

            n= math.tanh(es)
            e.delete(0,END)
            e.insert(1, str(n))
        elif c=="sinh\u207B\u00B9":
            es=eval(e.get())

            n= math.asinh(es)
            e.delete(0,END)
            e.insert(1, str(n))
        elif c=="cosh\u207B\u00B9":
            es=eval(e.get())

            n= math.acosh(es)
            e.delete(0,END)
            e.insert(1, str(n))
        elif c=="tanh\u207B\u00B9":
            es=eval(e.get())

            n= math.atanh(es)
            e.delete(0,END)
            e.insert(1, str(n))
        elif c=="()":
            es=eval(e.get())
            
            e.delete(0,END)
            e.insert(1,"("+str(es)+")")

        elif c=="log":
            es=eval(e.get())
            n= math.log10(es)
            e.delete(0,END)
            e.inserted(1,str(n))
        elif c=="ln":
            es=eval(e.get())
            n= math.log1p(es)
            e.delete(0, END)
            e.insert(1,str(n))
        elif c=="log2":
            es=eval(e.get())
            n=math.log2(es)
            e.delete(0, END)
            e.insert(1,str(n))
        elif c=="antilog":
            es=eval(e.get())
            n=10**(es)
            e.delete(0, END)
            e.insert(1,str(n))
        elif c=="anti ln or e exponent":
            es=eval(e.get())
            n=2.71828**(es)
            e.delete(0, END)
            e.insert(1,str(n))
        elif c=="antilog2":
            es=eval(e.get())
            n=2**(es)
            e.delete(0, END)
            e.insert(1,str(n))
        elif c=="1/x":
            es=eval(e.get())
            n=1/es
            e.delete(0, END)
            e.insert(1,str(n))
        elif c=="√":
            es=eval(e.get())
            n=(es)**(1/2)
            e.delete(0, END)
            e.insert(1,str(n))
        elif c=="3√":
            es=eval(e.get())
            n=(es)**(1/3)
            e.delete(0, END)
            e.insert(1,str(n))
        elif c=="4√":
            es=eval(e.get())
            n=(es)**(1/4)
            e.delete(0, END)
            e.insert(1,str(n))
        elif c=="5√":
            es=eval(e.get())
            n=(es)**(1/5)
            e.delete(0, END)
            e.insert(1,str(n))
        elif c=="6√":
            es=eval(e.get())
            n=(es)**(1/6)
            e.delete(0, END)
            e.insert(1,str(n))

        elif c=="x\u00B2":
            es=eval(e.get())
            n=(es)**(2.0)
            e.delete(0, END)
            e.insert(1,str(n))
        elif c=="x\u00B3":
            es=eval(e.get())
            n=(es)**(3.0)
            e.delete(0, END)
            e.insert(1,str(n))
        
        
    except:
        e.insert(1,"Error")
    
    r1.destroy()


def conn():
    global lbx1
    r1=Toplevel()
  
    r1.config(bg="#1F1F1F")
    r1.title("Constants")

    r1.geometry("200x230")
    r=Frame(r1)
    r.grid(row=0,column=0)
    lbx1= Listbox(r, bg="#1F1F1F", fg="#40E0D0",font="Consolas 12 ",background="#313335", foreground="#40E0D0")
    lbx1.pack(side=LEFT, expand='True', anchor="e", fill=BOTH)
    xro=Scrollbar(r, activebackground="gray", bg="#1F1F1F", bd=0, highlightbackground="#313335")
    
    xro.pack(side=RIGHT, expand='True', anchor="e",fill= Y)
    xro.configure(command=lbx1.yview)

    lbx1.configure(yscrollcommand=xro.set)
    
    lbx1.insert(END, "µ\u2091")
    lbx1.insert(END, "µ\u209A")
    lbx1.insert(END, "ρₐ\u1D62\u1D63")
    lbx1.insert(END, "\u210F")
    lbx1.insert(END, "h")
    lbx1.insert(END, "m\u209A")
    lbx1.insert(END, "m\u2091")
    lbx1.insert(END, "mµ")
    lbx1.insert(END, "m\u2099")
    lbx1.insert(END, "a\u2080")
    lbx1.insert(END, "g")
    lbx1.insert(END, "µN")
    lbx1.insert(END, "µB")
    lbx1.insert(END, "α")
    lbx1.insert(END, "r\u2091")
    lbx1.insert(END, "λc")
    lbx1.insert(END, "γp")
    lbx1.insert(END, "λc,p")
    lbx1.insert(END, "λc,n")
    lbx1.insert(END, "R∞")
    lbx1.insert(END, "u")
    lbx1.insert(END, "µ\u2099")
    lbx1.insert(END, "µ\u1D64")
    lbx1.insert(END, "F")
    lbx1.insert(END, "e(maths)")
    lbx1.insert(END, "Avogadro(NA)")
    lbx1.insert(END, "k")
    lbx1.insert(END, "Vm")
    lbx1.insert(END, "R")
    lbx1.insert(END, "C\u2080")
    lbx1.insert(END, "C\u2081")
    lbx1.insert(END, "C\u2082")
    lbx1.insert(END, "σ")
    lbx1.insert(END, "µ\u2080")
    lbx1.insert(END, "ϵ\u2080")
    lbx1.insert(END, "φ\u2080")
    lbx1.insert(END, "G\u2080")
    lbx1.insert(END, "Z\u2080")
    lbx1.insert(END, "t(Kelvin Sci)")    
    lbx1.insert(END, "G")    
    lbx1.insert(END, "atm")
    lbx1.insert(END, "bar")
    lbx1.insert(END, "K(Kelvin)")
    lbx1.insert(END, "e(electron)")
    lbx1.insert(END, "π")

    lbx1.bind("<Double-Button-1>", vbind1)
    app=Button(r1, bg="#313335", text="Add(+)",fg="#40E0D0",font="Consolas 12 ", border=0, command=v1,padx=70)
    app.grid(row=1,column=0)

def v1():
    global lbx1
    global e11
    d=lbx1.get(ANCHOR)

    
    if d=="µ\u2091":
        e11.insert(END, str(-9.2847*10**-24))
    elif d=="µ\u209A":
        e11.insert(END, str(-1.4106*10**-26))
    elif d=="ρₐ\u1D62\u1D63":
        e11.insert(END, str(1.2041))
    elif d=="\u210F":
        e11.insert(END, str(1.05457163*10**-34))
    elif d=="h":
        e11.insert(END, str(6.62606896*10**-34))
    elif d=="m\u209A":
        e11.insert(END, str(1.672621637*10**-27))
    elif d=="m\u2091":
        e11.insert(END, str(9.109382150*10**-31))
    elif d=="mµ":
        e11.insert(END, str(1.8835313*10**-28))
    elif d=="m\u2099":
        e11.insert(END, str(1.674927211*10**-27))
    elif d=="a\u2080":
        e11.insert(END, str(5.291772086*10**-11))
    elif d=="g":
        e11.insert(END, str(9.806650))
    elif d=="µN":
        e11.insert(END, str(5.05078324*10**-27))
    elif d=="µB":
        e11.insert(END, str(9.27400915*10**-24))
    elif d=="α":
        e11.insert(END, str(7.297352538*10**-3))
    elif d=="r\u2091":
        e11.insert(END, str(2.817940289*10**-15))
    elif d=="λc":
        e11.insert(END, str(2.426310218*10**-12))
    elif d=="γp":
        e11.insert(END, str(267522209.9))
    elif d=="λc,p":
        e11.insert(END, str(1.321409845*10**-15))
    elif d=="λc,n":
        e11.insert(END, str(1.319590895*10**-15))
    elif d=="R∞":
        e11.insert(END, str(10973731.57))
    elif d=="u":
        e11.insert(END, str(1.660538782*10**-27))
    elif d=="µ\u2099":
        e11.insert(END, str(-9.6623641*10**-27))
    elif d=="µ\u1D64":
        e11.insert(END, str(-4.49044786*10**-26))
    elif d=="F":
        e11.insert(END, str(96485.3399))
    elif d=="e(maths)":
        e11.insert(END, str(2.71828))
    elif d=="Avogadro(NA)":
        e11.insert(END, str(6.02214179*10**23))
    elif d=="k":
        e11.insert(END, str(1.3806504*10**-23))
    elif d=="Vm":
        e11.insert(END, str(0.022413996))
    elif d=="R":
        e11.insert(END, str(8.314472))
    elif d=="C\u2080":
        e11.insert(END, str(299792458))
    elif d=="C\u2081":
        e11.insert(END, str(3.74177118*10**-16))
    elif d=="C\u2082":
        e11.insert(END, str(0.014387752))
    elif d=="σ":
        e11.insert(END, str(5.5704*10**-8))
    elif d=="µ\u2080":
        e11.insert(END, str(1.256637061*10**-34))
    elif d=="ϵ\u2080":
        e11.insert(END, str(8.854187817*10**-12))
    elif d=="φ\u2080":
        e11.insert(END, str(2.067833667*10**-15))
    elif d=="G\u2080":
        e11.insert(END, str(7.7480917*10**-5))
    elif d=="Z\u2080":
        e11.insert(END, str(376.7303135))
    elif d=="t(Kelvin Sci)":
        e11.insert(END, str(273.15))
    elif d=="G":
        e11.insert(END, str(6.62606896*10**-34))
    elif d=="atm":
        e11.insert(END, str(1.013*10**5))
    elif d=="bar":
        e11.insert(END, str(1.01325))
    elif d=="K(Kelvin)":
        e11.insert(END, str(273))
    elif d=="e(electron)":
        e11.insert(END, str(1.602176487*10**-19))
    elif d=="π":
        e11.insert(END, str(3.141592654))

def vbind1(self):
    global lbx1
    global e11
    d=lbx1.get(ANCHOR)

    
    if d=="µ\u2091":
        e11.insert(END, str(-9.2847*10**-24))
    elif d=="µ\u209A":
        e11.insert(END, str(-1.4106*10**-26))
    elif d=="ρₐ\u1D62\u1D63":
        e11.insert(END, str(1.2041))
    elif d=="\u210F":
        e11.insert(END, str(1.05457163*10**-34))
    elif d=="h":
        e11.insert(END, str(6.62606896*10**-34))
    elif d=="m\u209A":
        e11.insert(END, str(1.672621637*10**-27))
    elif d=="m\u2091":
        e11.insert(END, str(9.109382150*10**-31))
    elif d=="mµ":
        e11.insert(END, str(1.8835313*10**-28))
    elif d=="m\u2099":
        e11.insert(END, str(1.674927211*10**-27))
    elif d=="a\u2080":
        e11.insert(END, str(5.291772086*10**-11))
    elif d=="g":
        e11.insert(END, str(9.806650))
    elif d=="µN":
        e11.insert(END, str(5.05078324*10**-27))
    elif d=="µB":
        e11.insert(END, str(9.27400915*10**-24))
    elif d=="α":
        e11.insert(END, str(7.297352538*10**-3))
    elif d=="r\u2091":
        e11.insert(END, str(2.817940289*10**-15))
    elif d=="λc":
        e11.insert(END, str(2.426310218*10**-12))
    elif d=="γp":
        e11.insert(END, str(267522209.9))
    elif d=="λc,p":
        e11.insert(END, str(1.321409845*10**-15))
    elif d=="λc,n":
        e11.insert(END, str(1.319590895*10**-15))
    elif d=="R∞":
        e11.insert(END, str(10973731.57))
    elif d=="u":
        e11.insert(END, str(1.660538782*10**-27))
    elif d=="µ\u2099":
        e11.insert(END, str(-9.6623641*10**-27))
    elif d=="µ\u1D64":
        e11.insert(END, str(-4.49044786*10**-26))
    elif d=="F":
        e11.insert(END, str(96485.3399))
    elif d=="e(maths)":
        e11.insert(END, str(2.71828))
    elif d=="Avogadro(NA)":
        e11.insert(END, str(6.02214179*10**23))
    elif d=="k":
        e11.insert(END, str(1.3806504*10**-23))
    elif d=="Vm":
        e11.insert(END, str(0.022413996))
    elif d=="R":
        e11.insert(END, str(8.314472))
    elif d=="C\u2080":
        e11.insert(END, str(299792458))
    elif d=="C\u2081":
        e11.insert(END, str(3.74177118*10**-16))
    elif d=="C\u2082":
        e11.insert(END, str(0.014387752))
    elif d=="σ":
        e11.insert(END, str(5.5704*10**-8))
    elif d=="µ\u2080":
        e11.insert(END, str(1.256637061*10**-34))
    elif d=="ϵ\u2080":
        e11.insert(END, str(8.854187817*10**-12))
    elif d=="φ\u2080":
        e11.insert(END, str(2.067833667*10**-15))
    elif d=="G\u2080":
        e11.insert(END, str(7.7480917*10**-5))
    elif d=="Z\u2080":
        e11.insert(END, str(376.7303135))
    elif d=="t(Kelvin Sci)":
        e11.insert(END, str(273.15))
    elif d=="G":
        e11.insert(END, str(6.62606896*10**-34))
    elif d=="atm":
        e11.insert(END, str(1.013*10**5))
    elif d=="bar":
        e11.insert(END, str(1.01325))
    elif d=="K(Kelvin)":
        e11.insert(END, str(273))
    elif d=="e(electron)":
        e11.insert(END, str(1.602176487*10**-19))
    elif d=="π":
        e11.insert(END, str(3.141592654))


#for unit conversion  
def Cov():
    global lbx2
    global f1
    f1=Toplevel()
   
    f1.config(bg="#1F1F1F")
    f1.title("Constants")

    f1.geometry("200x230")
    r=Frame(f1)
    r.grid(row=0,column=0)
    lbx2= Listbox(r, bg="#1F1F1F", fg="#40E0D0",font="Consolas 12 ",background="#313335", foreground="#40E0D0")
    lbx2.pack(side=LEFT, expand='True', anchor="e", fill=BOTH)
    xro=Scrollbar(r, activebackground="gray", bg="#1F1F1F", bd=0, highlightbackground="#313335")
    
    xro.pack(side=RIGHT, expand='True', anchor="e",fill= Y)
    xro.configure(command=lbx2.yview)

    lbx2.configure(yscrollcommand=xro.set)
    lbx2.insert(END, "in -> cm")
    lbx2.insert(END, "in <- cm")
    lbx2.insert(END, "ft -> m")
    lbx2.insert(END, "ft <- m")
    lbx2.insert(END, "yd -> m")
    lbx2.insert(END, "yd <- m")
    lbx2.insert(END, "miles -> km")
    lbx2.insert(END, "miles <- km")
    lbx2.insert(END, "miles -> km")
    lbx2.insert(END, "miles <- m")

    lbx2.insert(END, "acre -> m\u00B2")
    lbx2.insert(END, "acre <- m\u00B2")
    lbx2.insert(END, "gal(US standard) -> l")
    lbx2.insert(END, "gal(US standard) <- l")
    lbx2.insert(END, "gal(UK standard) -> l")
    lbx2.insert(END, "gal(UK standard) <- l")
    lbx2.insert(END, "pc -> km")
    lbx2.insert(END, "pc <- km")
    lbx2.insert(END, "m/s -> km/h")
    lbx2.insert(END, "m/s <- km/h")

    lbx2.insert(END, "oz -> g")
    lbx2.insert(END, "oz <- g")
    lbx2.insert(END, "lb -> kg")
    lbx2.insert(END, "lb <- kg")
    lbx2.insert(END, "atm -> Pa")
    lbx2.insert(END, "atm <- Pa")
    lbx2.insert(END, "mmHg -> Pa")
    lbx2.insert(END, "mmHg <- Pa")
    lbx2.insert(END, "hp -> kW")
    lbx2.insert(END, "hp <- kW")

    lbx2.insert(END, "kgf/cm\u00B2 -> Pa")
    lbx2.insert(END, "kgf/cm\u00B2 <- Pa")
    lbx2.insert(END, "kgf.m -> J")
    lbx2.insert(END, "kgf.m <- J")
    lbx2.insert(END, "lbf/in\u00B2 -> kPa")
    lbx2.insert(END, "lbf/in\u00B2 <- kPa")
    lbx2.insert(END, "F\u00B0 -> C\u00B0")
    lbx2.insert(END, "F\u00B0 <- C\u00B0")
    lbx2.insert(END, "J -> cal")
    lbx2.insert(END, "J <- cal")
    lbx2.bind("<Double-Button-1>", Uncanny)


def Uncanny(self):
    global lbx2
    global f1
    

    f= lbx2.get(ANCHOR)

    #1st slice of unit conversion
    if f=="in -> cm":
        d=eval(e.get())*2.54
        e.delete(0, END)
        e.insert(1, str(d))
    elif f=="in <- cm":
        d=eval(e.get())/2.54
        e.delete(0, END)
        e.insert(1, str(d))

    elif f=="ft -> m":
        d=eval(e.get())*0.305
        e.delete(0, END)
        e.insert(1, str(d))        

    elif f=="ft <- m":
        d=eval(e.get())/0.305
        e.delete(0, END)
        e.insert(1, str(d))        

    elif f=="yd -> m":
        d= eval(e.get())*0.305*3
        e.delete(0,END)
        e.insert(1, str(d))
    
    elif f=="yd <- m":
        d= eval(e.get())/0.305/3
        e.delete(0,END)
        e.insert(1, str(d))
    
    elif f=="miles -> km":
        d=eval(e.get())*1.609
        e.delete(0,END)
        e.insert(1, str(d))

    elif f=="miles <- km":
        d=eval(e.get())/1.609
        e.delete(0,END)
        e.insert(1, str(d))

    elif f=="miles -> m":
        d=eval(e.get())*1609
        e.delete(0,END)
        e.insert(1, str(d))

    elif f=="miles <- m":
        d=eval(e.get())/1609
        e.delete(0,END)
        e.insert(1, str(d))

    #second slice of units convertion

    elif f=="acre -> m\u00B2":
        d= eval(e.get())*4046.856
        e.delete(0, END)
        e.insert(1, str(d))

    elif f=="acre <- m\u00B2":
        d= eval(e.get())/4046.856
        e.delete(0, END)
        e.insert(1, str(d))

    elif f=="gal(US standard) -> l":
        d= eval(e.get())*3.785
        e.delete(0, END)
        e.insert(1, str(d))

    elif f=="gal(US standard) <- l":
        d= eval(e.get())/3.785
        e.delete(0, END)
        e.insert(1, str(d))

    elif f=="gal(UK standard) -> l":
        d= eval(e.get())*4.546
        e.delete(0,END)
        e.insert(1, str(d))

    elif f=="gal(UK standard) <- l":
        d= eval(e.get())/4.546
        e.delete(0,END)
        e.insert(1, str(d))

    elif f=="pc -> km":
        d=eval(e.get())*3.086e13
        e.delete(0,END)
        e.insert(1, str(d))

    elif f=="pc <- km":
        d=eval(e.get())/3.086e13
        e.delete(0,END)
        e.insert(1, str(d))

    elif f=="m/s -> km/h":
        d= eval(e.get())*3.6
        e.delete(0,END)
        e.insert(1, str(d))

    elif f=="m/s <- km/h":
        d= eval(e.get())/3.6
        e.delete(0,END)
        e.insert(1, str(d))

    #3rd slice of unit conversion

    elif f=="oz -> g":
        d= eval(e.get())*28.35
        e.delete(0,END)
        e.insert(1, str(d))

    elif f=="oz <- g":
        d= eval(e.get())/28.35
        e.delete(0,END)
        e.insert(1, str(d))

    elif f=="lb -> kg":
        d= eval(e.get())*0.454
        e.delete(0,END)
        e.insert(1, str(d))

    elif f=="lb <- kg":
        d= eval(e.get())/0.454
        e.delete(0,END)
        e.insert(1, str(d))

    elif f=="atm -> Pa":
        d= eval(e.get())*1.01325e5
        e.delete(0, END)
        e.insert(1, str(d))

    elif f=="atm <- Pa":
        d= eval(e.get())/1.01325e5
        e.delete(0, END)
        e.insert(1, str(d))
        
    elif f=="mmHg -> Pa":
        d= eval(e.get())*133.322
        e.delete(0,END)
        e.insert(1, str(d))

    elif f=="mmHg <- Pa":
        d= eval(e.get())/133.322
        e.delete(0,END)
        e.insert(1, str(d))

    elif f=="hp -> kW":
        d= eval(e.get())*0.746
        e.delete(0,END)
        e.insert(1, str(d))

    elif f=="hp <- kW":
        d= eval(e.get())/0.746
        e.delete(0,END)
        e.insert(1, str(d))

    #4th slice of units conversion

    elif f=="kgf/cm\u00B2 -> Pa":
        d= eval(e.get())*98066.5
        e.delete(0, END)
        e.insert(1, str(d))

    elif f=="kgf/cm\u00B2 <- Pa":
        d= eval(e.get())/98066.5
        e.delete(0, END)
        e.insert(1, str(d))

    elif f=="kgf.m -> J":
        d= eval(e.get())*9.81
        e.delete(0, END)
        e.insert(1, str(d))

    elif f=="kgf.m <- J":
        d= eval(e.get())/9.81
        e.delete(0, END)
        e.insert(1, str(d))

    elif f=="lbf/in\u00B2 -> kPa":
        d= eval(e.get())*6.895
        e.delete(0, END)
        e.insert(1, str(d))

    elif f=="lbf/in\u00B2 <- kPa":
        d= eval(e.get())/6.895
        e.delete(0, END)
        e.insert(1, str(d))

    elif f=="F\u00B0 -> C\u00B0":
        d= (eval(e.get())-32)*5/9
        e.delete(0, END)
        e.insert(1, str(d))

    elif f=="F\u00B0 <- C\u00B0":
        d= eval(e.get())*(9/5)+32
        e.delete(0, END)
        e.insert(1, str(d))

    elif f=="J -> cal":
        d= eval(e.get())*4.1842
        e.delete(0, END)
        e.insert(1, str(d))

    elif f=="J <- cal":
        d= eval(e.get())/4.1842
        e.delete(0, END)
        e.insert(1, str(d))

    f1.destroy()
     
def diff():
    global lbx3
    global f11
    f11=Toplevel()
    
    f11.config(bg="#1F1F1F")
    f11.title("Constants")

    f11.geometry("200x230")
    r=Frame(f11)
    r.grid(row=0,column=0)
    lbx3= Listbox(r, bg="#1F1F1F", fg="#40E0D0",font="Consolas 12 ",background="#313335", foreground="#40E0D0")
    lbx3.pack(side=LEFT, expand='True', anchor="e", fill=BOTH)
    xro=Scrollbar(r, activebackground="gray", bg="#1F1F1F", bd=0, highlightbackground="#313335")
    
    xro.pack(side=RIGHT, expand='True', anchor="e",fill= Y)
    xro.configure(command=lbx3.yview)

    lbx3.configure(yscrollcommand=xro.set)
    lbx3.insert(END, "in -> cm")
    lbx3.insert(END, "in <- cm")
    lbx3.insert(END, "ft -> m")
    lbx3.insert(END, "ft <- m")
    lbx3.insert(END, "yd -> m")
    lbx3.insert(END, "yd <- m")
    lbx3.insert(END, "miles -> km")
    lbx3.insert(END, "miles <- km")
    lbx3.insert(END, "miles -> km")
    lbx3.insert(END, "miles <- m")

    lbx3.insert(END, "acre -> m\u00B2")
    lbx3.insert(END, "acre <- m\u00B2")
    lbx3.insert(END, "gal(US standard) -> l")
    lbx3.insert(END, "gal(US standard) <- l")
    lbx3.insert(END, "gal(UK standard) -> l")
    lbx3.insert(END, "gal(UK standard) <- l")
    lbx3.insert(END, "pc -> km")
    lbx3.insert(END, "pc <- km")
    lbx3.insert(END, "m/s -> km/h")
    lbx3.insert(END, "m/s <- km/h")

    lbx3.insert(END, "oz -> g")
    lbx3.insert(END, "oz <- g")
    lbx3.insert(END, "lb -> kg")
    lbx3.insert(END, "lb <- kg")
    lbx3.insert(END, "atm -> Pa")
    lbx3.insert(END, "atm <- Pa")
    lbx3.insert(END, "mmHg -> Pa")
    lbx3.insert(END, "mmHg <- Pa")
    lbx3.insert(END, "hp -> kW")
    lbx3.insert(END, "hp <- kW")

    lbx3.insert(END, "kgf/cm\u00B2 -> Pa")
    lbx3.insert(END, "kgf/cm\u00B2 <- Pa")
    lbx3.insert(END, "kgf.m -> J")
    lbx3.insert(END, "kgf.m <- J")
    lbx3.insert(END, "lbf/in\u00B2 -> kPa")
    lbx3.insert(END, "lbf/in\u00B2 <- kPa")
    lbx3.insert(END, "F\u00B0 -> C\u00B0")
    lbx3.insert(END, "F\u00B0 <- C\u00B0")
    lbx3.insert(END, "J -> cal")
    lbx3.insert(END, "J <- cal")
    lbx3.bind("<Double-Button-1>", Uncanny1)

   
def Uncanny1(self):
    global lbx3
    global f11
    global e11
    

    f= lbx3.get(ANCHOR)

    #1st slice of unit conversion
    if f=="in -> cm":
        d=eval(e11.get())*2.54
        e11.delete(0, END)
        e11.insert(1, str(d))
    elif f=="in <- cm":
        d=eval(e11.get())/2.54
        e11.delete(0, END)
        e11.insert(1, str(d))

    elif f=="ft -> m":
        d=eval(e11.get())*0.305
        e11.delete(0, END)
        e11.insert(1, str(d))        

    elif f=="ft <- m":
        d=eval(e11.get())/0.305
        e11.delete(0, END)
        e11.insert(1, str(d))        

    elif f=="yd -> m":
        d= eval(e11.get())*0.305*3
        e11.delete(0,END)
        e11.insert(1, str(d))
    
    elif f=="yd <- m":
        d= eval(e11.get())/0.305/3
        e11.delete(0,END)
        e11.insert(1, str(d))
    
    elif f=="miles -> km":
        d=eval(e11.get())*1.609
        e11.delete(0,END)
        e11.insert(1, str(d))

    elif f=="miles <- km":
        d=eval(e11.get())/1.609
        e11.delete(0,END)
        e11.insert(1, str(d))

    elif f=="miles -> m":
        d=eval(e11.get())*1609
        e11.delete(0,END)
        e11.insert(1, str(d))

    elif f=="miles <- m":
        d=eval(e11.get())/1609
        e11.delete(0,END)
        e11.insert(1, str(d))

    #second slice of units convertion

    elif f=="acre -> m\u00B2":
        d= eval(e11.get())*4046.856
        e11.delete(0, END)
        e11.insert(1, str(d))

    elif f=="acre <- m\u00B2":
        d= eval(e11.get())/4046.856
        e11.delete(0, END)
        e11.insert(1, str(d))

    elif f=="gal(US standard) -> l":
        d= eval(e11.get())*3.785
        e11.delete(0, END)
        e11.insert(1, str(d))

    elif f=="gal(US standard) <- l":
        d= eval(e11.get())/3.785
        e11.delete(0, END)
        e11.insert(1, str(d))

    elif f=="gal(UK standard) -> l":
        d= eval(e11.get())*4.546
        e11.delete(0,END)
        e11.insert(1, str(d))

    elif f=="gal(UK standard) <- l":
        d= eval(e11.get())/4.546
        e11.delete(0,END)
        e11.insert(1, str(d))

    elif f=="pc -> km":
        d=eval(e11.get())*3.086e13
        e11.delete(0,END)
        e11.insert(1, str(d))

    elif f=="pc <- km":
        d=eval(e11.get())/3.086e13
        e11.delete(0,END)
        e11.insert(1, str(d))

    elif f=="m/s -> km/h":
        d= eval(e11.get())*3.6
        e11.delete(0,END)
        e11.insert(1, str(d))

    elif f=="m/s <- km/h":
        d= eval(e11.get())/3.6
        e11.delete(0,END)
        e11.insert(1, str(d))

    #3rd slice of unit conversion

    elif f=="oz -> g":
        d= eval(e11.get())*28.35
        e11.delete(0,END)
        e11.insert(1, str(d))

    elif f=="oz <- g":
        d= eval(e11.get())/28.35
        e11.delete(0,END)
        e11.insert(1, str(d))

    elif f=="lb -> kg":
        d= eval(e11.get())*0.454
        e11.delete(0,END)
        e11.insert(1, str(d))

    elif f=="lb <- kg":
        d= eval(e11.get())/0.454
        e11.delete(0,END)
        e11.insert(1, str(d))

    elif f=="atm -> Pa":
        d= eval(e11.get())*1.01325e5
        e11.delete(0, END)
        e11.insert(1, str(d))

    elif f=="atm <- Pa":
        d= eval(e11.get())/1.01325e5
        e11.delete(0, END)
        e11.insert(1, str(d))
        
    elif f=="mmHg -> Pa":
        d= eval(e11.get())*133.322
        e11.delete(0,END)
        e11.insert(1, str(d))

    elif f=="mmHg <- Pa":
        d= eval(e11.get())/133.322
        e11.delete(0,END)
        e11.insert(1, str(d))

    elif f=="hp -> kW":
        d= eval(e11.get())*0.746
        e11.delete(0,END)
        e11.insert(1, str(d))

    elif f=="hp <- kW":
        d= eval(e11.get())/0.746
        e11.delete(0,END)
        e11.insert(1, str(d))

    #4th slice of units conversion

    elif f=="kgf/cm\u00B2 -> Pa":
        d= eval(e11.get())*98066.5
        e11.delete(0, END)
        e11.insert(1, str(d))

    elif f=="kgf/cm\u00B2 <- Pa":
        d= eval(e11.get())/98066.5
        e11.delete(0, END)
        e11.insert(1, str(d))

    elif f=="kgf.m -> J":
        d= eval(e11.get())*9.81
        e11.delete(0, END)
        e11.insert(1, str(d))

    elif f=="kgf.m <- J":
        d= eval(e11.get())/9.81
        e11.delete(0, END)
        e11.insert(1, str(d))

    elif f=="lbf/in\u00B2 -> kPa":
        d= eval(e11.get())*6.895
        e11.delete(0, END)
        e11.insert(1, str(d))

    elif f=="lbf/in\u00B2 <- kPa":
        d= eval(e11.get())/6.895
        e11.delete(0, END)
        e11.insert(1, str(d))

    elif f=="F\u00B0 -> C\u00B0":
        d= (eval(e11.get())-32)*5/9
        e11.delete(0, END)
        e11.insert(1, str(d))

    elif f=="F\u00B0 <- C\u00B0":
        d= eval(e11.get())*(9/5)+32
        e11.delete(0, END)
        e11.insert(1, str(d))

    elif f=="J -> cal":
        d= eval(e11.get())*4.1842
        e11.delete(0, END)
        e11.insert(1, str(d))

    elif f=="J <- cal":
        d= eval(e11.get())/4.1842
        e11.delete(0, END)
        e11.insert(1, str(d))

    f11.destroy()



def applier():
    global sgk
    global IMGF1
    global IMGF2
    global e11
    global e22
    




    exp1=Toplevel()
  
    exp1.title("Exponential Root")
    exp1.config(bg="#1F1F1F")

    expf=LabelFrame(exp1, bg="#1F1F1F", fg="#40E0D0", border=0)


    
    expf.grid(row=0, column=0, columnspan=2)
    imgf1=Image.open("d:/border.PNG")
    imgf1=imgf1.resize((380,45), Image.ANTIALIAS)
    IMGF1=ImageTk.PhotoImage(imgf1)



    Limg=Label(expf, image=IMGF1, bg="#1F1F1F")
    Limg.grid(row=1, column=0)    
    e11= Entry(expf, bg="#1F1F1F", fg="#40E0D0", insertbackground="#40E0D0", border=0, width=39)
    e11.grid(row=1, column=0)


    so=LabelFrame(exp1,bg="#1F1F1F", border=0)
    so.grid(row=2,column=0,columnspan=1,padx=6,pady=6,ipady=6)

    soa=LabelFrame(exp1,bg="#1F1F1F", border=0)
    soa.grid(row=2,column=1,columnspan=8,padx=6,pady=6,ipady=6)

    sowe=LabelFrame(exp1,bg="#1F1F1F", border=0)
    sowe.grid(row=1,column=0,columnspan=1,padx=6,pady=6,ipady=6)

    ldf=Label(sowe, text="NUMBERS PAD: ", bg="#1F1F1F",fg="#40E0D0")
    ldf.grid(row=0, column=0)
    ldf1=Button(sowe, text=" Unit Conversion ", bg="#313335",fg="#40E0D0", border= 0, font= "Consolas 10", command=diff)
    ldf1.grid(row=0, column=1)

    but1e= Button(so,text="1",command= lambda: Add1(1), bg="#313335",fg="#40E0D0",padx=19,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but2e= Button(so,text="2",command= lambda: Add1(2), bg="#313335",fg="#40E0D0",padx=19,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but3e= Button(so,text="3",command= lambda: Add1(3), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but4e= Button(so,text="4",command= lambda: Add1(4), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but5e= Button(so,text="5",command= lambda: Add1(5), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but6e= Button(so,text="6",command=lambda: Add1(6), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but7e= Button(so,text="7",command= lambda:Add1(7), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but8e= Button(so,text="8",command= lambda:Add1(8), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but9e= Button(so,text="9",command=lambda: Add1(9), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    but0e= Button(so,text="0",command=lambda: Add1(0), bg="#313335",fg="#40E0D0",padx=18,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    butde= Button(so,text=".",command=lambda: Add1("."), bg="#313335",fg="#40E0D0",padx=21,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    butne= Button(so,text="+/-",command=eneg, bg="#313335",fg="#40E0D0",padx=14,pady=13,borderwidth=4,font="Sans 12 bold", border =0)
    
    
    
    but1e.grid(row=0, column=0, padx=8, pady=8)
    but2e.grid(row=0, column=1, padx=8, pady=8)
    but3e.grid(row=0, column=2, padx=8, pady=8)
    but4e.grid(row=1, column=0, padx=8, pady=8)
    but5e.grid(row=1, column=1, padx=8, pady=8)
    but6e.grid(row=1, column=2, padx=8, pady=8)
    but7e.grid(row=2, column=0, padx=8, pady=8)
    but8e.grid(row=2, column=1, padx=8, pady=8)
    but9e.grid(row=2, column=2, padx=8, pady=8)
    but0e.grid(row=3, column=1, padx=8, pady=8)
    butde.grid(row=3, column=0, padx=8, pady=8)
    butne.grid(row=3, column=2, padx=8, pady=8)

    buta= Button(soa,text="+",command=lambda: Add1("+"), bg="#3D3D3D",fg="#40E0D0",padx=19,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    buta.grid(row=0, column=0, padx=8, pady=8)
    buts= Button(soa,text="-",command=lambda: Add1("-"), bg="#3D3D3D",fg="#40E0D0",padx=20,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    buts.grid(row=1, column=0, padx=8, pady=8)
    butm= Button(soa,text="*",command=lambda: Add1("*"), bg="#3D3D3D",fg="#40E0D0",padx=21,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butm.grid(row=2, column=0, padx=8, pady=8)    
    butd= Button(soa,text="/",command=lambda: Add1("/"), bg="#3D3D3D",fg="#40E0D0",padx=22,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butd.grid(row=3, column=0, padx=8, pady=8)
    buter= Button(soa,text="1/x",command=resc, bg="#3D3D3D",fg="#40E0D0",padx=13,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    buter.grid(row=0, column=1, padx=8, pady=8)
    butpoo= Button(soa,text="^",command=lambda: Add1("**"), bg="#3D3D3D",fg="#40E0D0",padx=20,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butpoo.grid(row=1, column=1, padx=8, pady=8)
    butnex= Button(soa,text="next",command=nexto, bg="#3D3D3D",fg="#40E0D0",padx=8,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butnex.grid(row=2, column=1, padx=8, pady=8)
    butcalc= Button(soa,text="=",command=Calc, bg="#3D3D3D",fg="#40E0D0",padx=21,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butcalc.grid(row=3, column=1, padx=8, pady=8)
    butclr= Button(soa,text="AC",command=e11deleter, bg="#3D3D3D",fg="#40E0D0",padx=12,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butclr.grid(row=0, column=2, padx=8, pady=8)
    butbcck= Button(soa,text="<-",command=e11bcck, bg="#3D3D3D",fg="#40E0D0",padx=16,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butbcck.grid(row=1, column=2, padx=8, pady=8)
    butfunc= Button(soa,text="+func",command=functions, bg="#3D3D3D",fg="#40E0D0",padx=4,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butfunc.grid(row=2, column=2, padx=8, pady=8)
    butconn= Button(soa,text="const",command=conn, bg="#3D3D3D",fg="#40E0D0",padx=4,pady=13,borderwidth=4,font="Sans 12 bold", border =0)    
    butconn.grid(row=3, column=2, padx=8, pady=8)
    

    
def Pg3():
    global sgk
    exp=Toplevel(root)
    exp.iconbitmap("d:/mymatelogo.ico")
    exp.title("Exponential Calculation")
    exp.config(bg="#1F1F1F")
    l1=Label(exp, text="Chose Exponential", bg="#1F1F1F", fg="#40E0D0")
    l1.grid(row=0, column=0)
    sgk=ttk.Combobox(exp,values=["x^2","x^3","x^4","As amuch as I want"])
    sgk.grid(row=0, column=1)
    sgk.insert(1,"x^2")
    sgkproof=Button(exp, text="Apply", bg="#313335", fg="#40E0D0",command=applier  ,  border=0)
    sgkproof.grid(row=1,column=0, columnspan=2)
    

def Pg2():
    dff=LabelFrame(root,bg="#1F1F1F", border=0,)
    dff.grid(row=0,column=0,columnspan=8,padx=6,pady=6,ipady=6)

        
    e= Entry(dff, text= "input",width=45,borderwidth=30,bg="#313335",fg="#40E0D0",font="Consolas 13",insertbackground="#40E0D0", border =0)
    e.grid(row=0,column=0,columnspan=6,padx=6,pady=6,ipady=6)

    page1=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="Page-1",border=0, activebackground="#313335",command=Pg1)
    page1.grid(row=1,column=0)

    page2=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="Page-2",border=0, activebackground="#313335",command=Pg2)
    page2.grid(row=1,column=1)

    page3=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="Exponential calculation",border=0, activebackground="#313335",command=applier)
    page3.grid(row=1,column=2)

    page4=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="Constants",border=0, activebackground="#313335",command=Const)
    page4.grid(row=1,column=3)

    page5=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="Units ",border=0, activebackground="#313335",command=Cov)
    page5.grid(row=1,column=4)

    page6=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="About",border=0, activebackground="#313335",command=Const)
    page6.grid(row=1,column=5)
    
    so=LabelFrame(root,bg="#1F1F1F", border=0,)
    so.grid(row=1,column=0,columnspan=8,padx=6,pady=6,ipady=6)


    but1= Button(so,text="π",command= lambda: Add(3.142), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    but2= Button(so,text="K",command= lambda: Add(9.0*10**(9)), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 italic", border =0)
    but3= Button(so,text="R ",command= lambda: Add(8.314), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 italic", border =0)
    but4= Button(so,text="e ",command= lambda: Add(2.71828),bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    but5= Button(so,text="c",command= lambda: Add(3.0*10**8),bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    but6= Button(so,text="mass of e ",command=lambda: Add(9.10938356*10**(-31)), bg="#313335",fg="#40E0D0",padx=25,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    but7= Button(so,text="(e\u207B) ",command= lambda:Add(1.60217662*10**(-19)),bg="#313335",fg="#40E0D0",padx=43,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    but8= Button(so,text="g ",command= lambda:Add(9.8), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    but9= Button(so,text="P ",command=lambda: Add(1.01*10**5), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    but0= Button(so,text="Tk",command=lambda: Add(273), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    butA=Button(so,text="+",command=Sum,bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    butS=Button(so,text="-",command=Sub,bg="#313335",fg="#40E0D0",padx=51,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    butM=Button(so,text="x",command=Mul,bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=5,font="Sans 10 bold", border =0)
    butD=Button(so,text="/",command=Did,bg="#313335",fg="#40E0D0",padx=52,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    butcl=Button(so,text="CC",command=lambda: CL(),bg="#313335",fg="#40E0D0",padx=45.8,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    butexit=Button(so,text="+func",command=funct,padx=38,pady=13,bg="#313335",fg="#40E0D0",borderwidth=4,font="Sans 10 bold", border =0)
    butsin= Button(so,text="sin",command=Sin,padx=44,pady=13,fg="#40E0D0",bg="gray",borderwidth=5,font="Sans 10", border =0)
    butEq=Button(so,text="=",command=EQ ,bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=5,font="Sans 10 bold", border =0)
    butcos= Button(so,text="cos",command=COS,padx=43,pady=13,fg="#40E0D0",bg="gray",borderwidth=4,font="Sans 10", border =0)
    buttan= Button(so,text="tan",command=TAN,padx=44,pady=13,fg="#40E0D0",bg="gray",borderwidth=4,font="Sans 10 ", border =0)
    butcot= Button(so,text="cot",command=COT,padx=44,pady=13,fg="#40E0D0",bg="gray",borderwidth=4,font="Sans 10 ", border =0)
    butsec= Button(so,text="sec",command=SEC,padx=43,pady=13,fg="#40E0D0",bg="gray",borderwidth=4,font="Sans 10 ", border =0)
    butcsc= Button(so,text="csc(cosec)",command=CSC,padx=22,pady=13,fg="#40E0D0",bg="gray",borderwidth=4,font="Sans 10", border =0)
    butflo= Button(so,text=".",command=DOT,padx=54,pady=13,bg="#313335",fg="#40E0D0",borderwidth=4,font="Sans 10 bold ", border =0)
    butneg= Button( so, text = "neg(-)", command=Neg, padx=38,pady=13,fg="white",bg="orange",borderwidth=4,font="Sans 10 ", border =0)
    butdel=Button(so,text="<-backspace",command=back,padx=16,pady=13,fg="red",bg="orange",borderwidth=4,font="Sans 10 ", border =0)

    butln= Button(so,text="ln",command=LN,padx=47,pady=13,fg="red",bg="#D3D3D3",borderwidth=5,font="Sans 10 ", border =0)
    butlog= Button(so,text="log",command=LOG10,padx=45,pady=13,fg="red",bg="#D3D3D3",borderwidth=5,font="Sans 10 ", border =0)
    butpow= Button(so,text="^",command=POW,padx=50,pady=13,fg="green",bg="white",borderwidth=5,font="Sans 10 ", border =0)
    butlog2= Button(so,text="log2",command=LOG2,padx=41,pady=13,fg="red",bg="#D3D3D3",borderwidth=5,font="Sans 10", border =0)
    butdis=Entry(so,text="Deg ",width=15,fg="#40E0D0",bg="gray",borderwidth=6,font="Sans 10", border =0)
    butmode=Button(so,text="Mode",command=Mode,padx=36,pady=13,fg="green",bg="white",borderwidth=5,font="Sans 10 ", border =0)
    butop=Button(so,text="(",command=Op,padx=50, pady=13,fg="black",bg="white",borderwidth=5,font="Sans 10 ", border =0)
    butclo=Button(so,text=")",command=Clo,padx=50, pady=13,fg="black",bg="white",borderwidth=5,font="Sans 10 ", border =0)
    butres=Button(so,text="Reciprocal",command=Res, padx=21, pady=13,fg="black",bg="white",borderwidth=5,font="Sans 10 ", border =0)
    butmem=Entry(so,text="0",width=15,fg="#40E0D0",bg="gray",borderwidth=6,font="Sans 10", border =0)
    butalphadis=Entry(so,text="1",width=15,fg="#40E0D0",bg="gray",borderwidth=6,font="Sans 10 italic", border =0)
    butAcon=Button(so,text="Alpha for inverse",command=Alpha, padx=5, pady=13,fg="green",bg="white",borderwidth=6,font="Sans 10 ", border =0)
    butSp=Button(so,text="Delete memories",command=Sp, padx=6, pady=13,fg="black",bg="orange",borderwidth=5,font="Sans 10 ", border =0)
    butall=Button(so,text="Delete all memory",command=All, padx=2, pady=13,fg="black",bg="orange",borderwidth=5,font="Sans 10 ", border =0)
    butper=Button(so,text="Percentage%",command=Per, padx=14, pady=13,fg="black",bg="#D3D3D3",borderwidth=5,font="Sans 10 ", border =0)




    butAns=Button(so,text="Reuse last Ans ",command=Ans, padx=8, pady=13,fg="black",bg="#D3D3D3",borderwidth=5,font="Sans 10 ", border =0)
    butAns.grid(row=4,column=7)

    but1.grid(row= 1,column=0,padx=8,pady=10)
    but2.grid(row= 1,column= 1,padx=8,pady=10)
    but3.grid(row= 1,column=2 ,padx=8,pady=10)
    but4.grid(row= 2,column=0 ,padx=8,pady=10)
    but5.grid(row= 2,column= 1,padx=8,pady=10)
    but6.grid(row= 2,column= 2,padx=8,pady=10)
    but7.grid(row= 3,column= 0,padx=8,pady=10)
    but8.grid(row= 3,column= 1,padx=8,pady=10)
    but9.grid(row= 3,column= 2,padx=8,pady=10)
    but0.grid(row= 4,column= 0,padx=8,pady=10)
    butA.grid(row= 5,column= 0,padx=8,pady=10)
    butS.grid(row=6 ,column= 0,padx=8,pady=10)
    butM.grid(row=6 ,column= 1,padx=8,pady=10)
    butD.grid(row=6 ,column=2 ,padx=8,pady=10)
    butEq.grid(row= 5,column= 1,padx=8,pady=10)
    butsin.grid(row=1,column=3)
    butcl.grid(row= 4,column= 1,padx=8,pady=10)
    butexit.grid(row=5,column=2,padx=8,pady=10)
    butcos.grid(row=2,column=3,padx=8,pady=10)
    buttan.grid(row=3,column=3,padx=8,pady=10)
    butcot.grid(row=4,column=3,padx=8,pady=10)
    butsec.grid(row=5,column=3,padx=8,pady=10)
    butcsc.grid(row=6,column=3,padx=8,pady=10)
    butflo.grid(row=4,column= 2,padx=8,pady=10)
    butln.grid(row=1,column= 4,padx=8,pady=10)
    butlog.grid(row=2,column= 4,padx=8,pady=10)
    butlog2.grid(row=3,column= 4,padx=8,pady=10)
    butpow.grid(row=4,column= 4,padx=8,pady=10)
    butneg.grid(row=5,column= 4,padx=8,pady=10)
    butdel.grid(row=6,column= 4,padx=8,pady=10)
    butdis.grid(row=1,column=5,ipady=15,padx=8,pady=10)
    butmode.grid(row=2,column=5,padx=8,pady=10)
    butop.grid(row=3,column=5,padx=8,pady=10)
    butclo.grid(row=4,column=5,padx=8,pady=10)
    butres.grid(row=5,column=5,padx=8,pady=10)
    butmem.grid(row=6,column=5,ipady=15,padx=8,pady=10)
    butalphadis.grid(row=1,column=7,ipady=15,padx=8,pady=10)
    butAcon.grid(row=2,column=7,padx=8,pady=10)
    butSp.grid(row=5,column=7,padx=8,pady=10)
    butall.grid(row=6,column=7,padx=8,pady=10)
    butper.grid(row=3,column=7,padx=8,pady=10)



def Pg1():
    dff=LabelFrame(root,bg="#1F1F1F", border=0,)
    dff.grid(row=0,column=0,columnspan=8,padx=6,pady=6,ipady=6)

        
    e= Entry(dff, text= "input",width=45,borderwidth=30,bg="#313335",fg="#40E0D0",font="Consolas 13",insertbackground="#40E0D0", border =0)
    e.grid(row=0,column=0,columnspan=6,padx=6,pady=6,ipady=6)

    page1=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="Page-1",border=0, activebackground="#313335",command=Pg1)
    page1.grid(row=1,column=0)

    page2=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="Page-2",border=0, activebackground="#313335",command=Pg2)
    page2.grid(row=1,column=1)


    page3=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="Exponential calculation",border=0, activebackground="#313335",command=applier)
    page3.grid(row=1,column=2)

    page4=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="Constants",border=0, activebackground="#313335",command=Const)
    page4.grid(row=1,column=3)

    page5=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="Units ",border=0, activebackground="#313335",command=Cov)
    page5.grid(row=1,column=4)

    page6=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="About",border=0, activebackground="#313335",command=Const)
    page6.grid(row=1,column=5)

    so=LabelFrame(root,bg="#1F1F1F", border=0,)
    so.grid(row=1,column=0,columnspan=8,padx=6,pady=6,ipady=6)


    but1= Button(so,text="1",command= lambda: Add(1),bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    but2= Button(so,text="2",command= lambda: Add(2), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    but3= Button(so,text="3 ",command= lambda: Add(3), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    but4= Button(so,text="4 ",command= lambda: Add(4), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    but5= Button(so,text="5 ",command= lambda: Add(5),bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    but6= Button(so,text="6 ",command=lambda: Add(6),bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    but7= Button(so,text="7 ",command= lambda:Add(7), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    but8= Button(so,text="8 ",command= lambda:Add(8), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    but9= Button(so,text="9 ",command=lambda: Add(9), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    but0= Button(so,text="0 ",command=lambda: Add(0), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    butA=Button(so,text="+",command=Sum,bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    butS=Button(so,text="-",command=Sub,bg="#313335",fg="#40E0D0",padx=51,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    butM=Button(so,text="x",command=Mul,bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=5,font="Sans 10 bold", border =0)
    butD=Button(so,text="/",command=Did,bg="#313335",fg="#40E0D0",padx=52,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    butcl=Button(so,text="CC",command=lambda: CL(),bg="#313335",fg="#40E0D0",padx=45.8,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    butexit=Button(so,text="Exit",command=root.destroy,padx=43,bg="#313335",fg="#40E0D0",pady=13,borderwidth=4,font="Sans 10 bold", border =0)
    butsin= Button(so,text="sin",command=Sin,padx=44,pady=13,fg="#40E0D0",bg="gray",borderwidth=5,font="Sans 10", border =0)
    butEq=Button(so,text="=",command=EQ ,bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=5,font="Sans 10 bold", border =0)
    butcos= Button(so,text="cos",command=COS,padx=43,pady=13,fg="#40E0D0",bg="gray",borderwidth=4,font="Sans 10", border =0)
    buttan= Button(so,text="tan",command=TAN,padx=44,pady=13,fg="#40E0D0",bg="gray",borderwidth=4,font="Sans 10 ", border =0)
    butcot= Button(so,text="cot",command=COT,padx=44,pady=13,fg="#40E0D0",bg="gray",borderwidth=4,font="Sans 10 ", border =0)
    butsec= Button(so,text="sec",command=SEC,padx=43,pady=13,fg="#40E0D0",bg="gray",borderwidth=4,font="Sans 10 ", border =0)
    butcsc= Button(so,text="csc(cosec)",command=CSC,padx=22,pady=13,fg="#40E0D0",bg="gray",borderwidth=4,font="Sans 10", border =0)
    butflo= Button(so,text=".",command=DOT,padx=54,pady=13,bg="#313335",fg="#40E0D0",borderwidth=4,font="Sans 10 bold ", border =0)
    butneg= Button( so, text = "neg(-)", command=Neg, padx=38,pady=13,fg="white",bg="orange",borderwidth=4,font="Sans 10 ", border =0)
    butdel=Button(so,text="<-backspace",command=back,padx=17,pady=13,fg="red",bg="orange",borderwidth=4,font="Sans 10 ", border =0)

    butln= Button(so,text="ln",command=LN,padx=47,pady=13,fg="red",bg="#D3D3D3",borderwidth=5,font="Sans 10 ", border =0)
    butlog= Button(so,text="log",command=LOG10,padx=45,pady=13,fg="red",bg="#D3D3D3",borderwidth=5,font="Sans 10 ", border =0)
    butpow= Button(so,text="^",command=POW,padx=50,pady=13,fg="green",bg="white",borderwidth=5,font="Sans 10 ", border =0)
    butlog2= Button(so,text="log2",command=LOG2,padx=41,pady=13,fg="red",bg="#D3D3D3",borderwidth=5,font="Sans 10", border =0)
    butdis=Entry(so,text="Deg ",width=15,fg="#40E0D0",bg="gray",borderwidth=6,font="Sans 10", border =0)
    butmode=Button(so,text="Mode",command=Mode,padx=36,pady=13,fg="green",bg="white",borderwidth=5,font="Sans 10 ", border =0)
    butop=Button(so,text="(",command=Op,padx=50, pady=13,fg="black",bg="white",borderwidth=5,font="Sans 10 ", border =0)
    butclo=Button(so,text=")",command=Clo,padx=50, pady=13,fg="black",bg="white",borderwidth=5,font="Sans 10 ", border =0)
    butres=Button(so,text="Reciprocal",command=Res, padx=21, pady=13,fg="black",bg="white",borderwidth=5,font="Sans 10 ", border =0)
    butmem=Entry(so,text="0",width=15,fg="#40E0D0",bg="gray",borderwidth=6,font="Sans 10", border =0)
    butalphadis=Entry(so,text="1",width=15,fg="#40E0D0",bg="gray",borderwidth=6,font="Sans 10 italic", border =0)
    butAcon=Button(so,text="Alpha for inverse",command=Alpha, padx=5, pady=13,fg="green",bg="white",borderwidth=6,font="Sans 10 ", border =0)
    butSp=Button(so,text="Delete memories",command=Sp, padx=6, pady=13,fg="black",bg="orange",borderwidth=5,font="Sans 10 ", border =0)
    butall=Button(so,text="Delete all memory",command=All, padx=2, pady=13,fg="black",bg="orange",borderwidth=5,font="Sans 10 ", border =0)
    butper=Button(so,text="Percentage%",command=Per, padx=14, pady=13,fg="black",bg="#D3D3D3",borderwidth=5,font="Sans 10 ", border =0)




    butAns=Button(so,text="Reuse last Ans ",command=Ans, padx=8, pady=13,fg="black",bg="#D3D3D3",borderwidth=5,font="Sans 10 ", border =0)
    butAns.grid(row=4,column=7)

    but1.grid(row= 1,column=0,padx=8,pady=10)
    but2.grid(row= 1,column= 1,padx=8,pady=10)
    but3.grid(row= 1,column=2 ,padx=8,pady=10)
    but4.grid(row= 2,column=0 ,padx=8,pady=10)
    but5.grid(row= 2,column= 1,padx=8,pady=10)
    but6.grid(row= 2,column= 2,padx=8,pady=10)
    but7.grid(row= 3,column= 0,padx=8,pady=10)
    but8.grid(row= 3,column= 1,padx=8,pady=10)
    but9.grid(row= 3,column= 2,padx=8,pady=10)
    but0.grid(row= 4,column= 0,padx=8,pady=10)
    butA.grid(row= 5,column= 0,padx=8,pady=10)
    butS.grid(row=6 ,column= 0,padx=8,pady=10)
    butM.grid(row=6 ,column= 1,padx=8,pady=10)
    butD.grid(row=6 ,column=2 ,padx=8,pady=10)
    butEq.grid(row= 5,column= 1,padx=8,pady=10)
    butsin.grid(row=1,column=3)
    butcl.grid(row= 4,column= 1,padx=8,pady=10)
    butexit.grid(row=5,column=2,padx=8,pady=10)
    butcos.grid(row=2,column=3,padx=8,pady=10)
    buttan.grid(row=3,column=3,padx=8,pady=10)
    butcot.grid(row=4,column=3,padx=8,pady=10)
    butsec.grid(row=5,column=3,padx=8,pady=10)
    butcsc.grid(row=6,column=3,padx=8,pady=10)
    butflo.grid(row=4,column= 2,padx=8,pady=10)
    butln.grid(row=1,column= 4,padx=8,pady=10)
    butlog.grid(row=2,column= 4,padx=8,pady=10)
    butlog2.grid(row=3,column= 4,padx=8,pady=10)
    butpow.grid(row=4,column= 4,padx=8,pady=10)
    butneg.grid(row=5,column= 4,padx=8,pady=10)
    butdel.grid(row=6,column= 4,padx=8,pady=10)
    butdis.grid(row=1,column=5,ipady=15,padx=8,pady=10)
    butmode.grid(row=2,column=5,padx=8,pady=10)
    butop.grid(row=3,column=5,padx=8,pady=10)
    butclo.grid(row=4,column=5,padx=8,pady=10)
    butres.grid(row=5,column=5,padx=8,pady=10)
    butmem.grid(row=6,column=5,ipady=15,padx=8,pady=10)
    butalphadis.grid(row=1,column=7,ipady=15,padx=8,pady=10)
    butAcon.grid(row=2,column=7,padx=8,pady=10)
    butSp.grid(row=5,column=7,padx=8,pady=10)
    butall.grid(row=6,column=7,padx=8,pady=10)
    butper.grid(row=3,column=7,padx=8,pady=10)



dff=LabelFrame(root,bg="#1F1F1F", border=0,)
dff.grid(row=0,column=0,columnspan=8,padx=6,pady=6,ipady=6)

    
e= Entry(dff, text= "input",width=45,borderwidth=30,bg="#313335",fg="#40E0D0",font="Consolas 13",insertbackground="#40E0D0", border =0)
e.grid(row=0,column=0,columnspan=6,padx=6,pady=6,ipady=6)

page1=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="Page-1",border=0, activebackground="#313335",command=Pg1)
page1.grid(row=1,column=0)

page2=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="Page-2",border=0, activebackground="#313335",command=Pg2)
page2.grid(row=1,column=1)


page3=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="Exponential calculation",border=0, activebackground="#313335",command=applier)
page3.grid(row=1,column=2)

page4=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="Constants",border=0, activebackground="#313335",command=Const)
page4.grid(row=1,column=3)

page5=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="Units ",border=0, activebackground="#313335",command=Cov)
page5.grid(row=1,column=4)

page6=Button(dff,bg="#313335",fg="#40E0D0",font="Sans 13", text="About",border=0, activebackground="#313335",command=Const)
page6.grid(row=1,column=5)

so=LabelFrame(root,bg="#1F1F1F", border=0,)
so.grid(row=1,column=0,columnspan=8,padx=6,pady=6,ipady=6)


but1= Button(so,text="1",command= lambda: Add(1),bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
but2= Button(so,text="2",command= lambda: Add(2), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
but3= Button(so,text="3 ",command= lambda: Add(3), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
but4= Button(so,text="4 ",command= lambda: Add(4), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
but5= Button(so,text="5 ",command= lambda: Add(5),bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
but6= Button(so,text="6 ",command=lambda: Add(6),bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
but7= Button(so,text="7 ",command= lambda:Add(7), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
but8= Button(so,text="8 ",command= lambda:Add(8), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
but9= Button(so,text="9 ",command=lambda: Add(9), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
but0= Button(so,text="0 ",command=lambda: Add(0), bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
butA=Button(so,text="+",command=Sum,bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
butS=Button(so,text="-",command=Sub,bg="#313335",fg="#40E0D0",padx=51,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
butM=Button(so,text="x",command=Mul,bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=5,font="Sans 10 bold", border =0)
butD=Button(so,text="/",command=Did,bg="#313335",fg="#40E0D0",padx=52,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
butcl=Button(so,text="CC",command=lambda: CL(),bg="#313335",fg="#40E0D0",padx=45.8,pady=13,borderwidth=4,font="Sans 10 bold", border =0)
butexit=Button(so,text="Exit",command=root.destroy,padx=43,bg="#313335",fg="#40E0D0",pady=13,borderwidth=4,font="Sans 10 bold", border =0)
butsin= Button(so,text="sin",command=Sin,padx=44,pady=13,fg="#40E0D0",bg="gray",borderwidth=5,font="Sans 10", border =0)
butEq=Button(so,text="=",command=EQ ,bg="#313335",fg="#40E0D0",padx=50,pady=13,borderwidth=5,font="Sans 10 bold", border =0)
butcos= Button(so,text="cos",command=COS,padx=43,pady=13,fg="#40E0D0",bg="gray",borderwidth=4,font="Sans 10", border =0)
buttan= Button(so,text="tan",command=TAN,padx=44,pady=13,fg="#40E0D0",bg="gray",borderwidth=4,font="Sans 10 ", border =0)
butcot= Button(so,text="cot",command=COT,padx=44,pady=13,fg="#40E0D0",bg="gray",borderwidth=4,font="Sans 10 ", border =0)
butsec= Button(so,text="sec",command=SEC,padx=43,pady=13,fg="#40E0D0",bg="gray",borderwidth=4,font="Sans 10 ", border =0)
butcsc= Button(so,text="csc(cosec)",command=CSC,padx=22,pady=13,fg="#40E0D0",bg="gray",borderwidth=4,font="Sans 10", border =0)
butflo= Button(so,text=".",command=DOT,padx=54,pady=13,bg="#313335",fg="#40E0D0",borderwidth=4,font="Sans 10 bold ", border =0)
butneg= Button( so, text = "neg(-)", command=Neg, padx=38,pady=13,fg="white",bg="orange",borderwidth=4,font="Sans 10 ", border =0)
butdel=Button(so,text="<-backspace",command=back,padx=17,pady=13,fg="red",bg="orange",borderwidth=4,font="Sans 10 ", border =0)

butln= Button(so,text="ln",command=LN,padx=47,pady=13,fg="red",bg="#D3D3D3",borderwidth=5,font="Sans 10 ", border =0)
butlog= Button(so,text="log",command=LOG10,padx=45,pady=13,fg="red",bg="#D3D3D3",borderwidth=5,font="Sans 10 ", border =0)
butpow= Button(so,text="^",command=POW,padx=50,pady=13,fg="green",bg="white",borderwidth=5,font="Sans 10 ", border =0)
butlog2= Button(so,text="log2",command=LOG2,padx=41,pady=13,fg="red",bg="#D3D3D3",borderwidth=5,font="Sans 10", border =0)
butdis=Entry(so,text="Deg ",width=15,fg="#40E0D0",bg="gray",borderwidth=6,font="Sans 10", border =0)
butmode=Button(so,text="Mode",command=Mode,padx=36,pady=13,fg="green",bg="white",borderwidth=5,font="Sans 10 ", border =0)
butop=Button(so,text="(",command=Op,padx=50, pady=13,fg="black",bg="white",borderwidth=5,font="Sans 10 ", border =0)
butclo=Button(so,text=")",command=Clo,padx=50, pady=13,fg="black",bg="white",borderwidth=5,font="Sans 10 ", border =0)
butres=Button(so,text="Reciprocal",command=Res, padx=21, pady=13,fg="black",bg="white",borderwidth=5,font="Sans 10 ", border =0)
butmem=Entry(so,text="0",width=15,fg="#40E0D0",bg="gray",borderwidth=6,font="Sans 10", border =0)
butalphadis=Entry(so,text="1",width=15,fg="#40E0D0",bg="gray",borderwidth=6,font="Sans 10 italic", border =0)
butAcon=Button(so,text="Alpha for inverse",command=Alpha, padx=5, pady=13,fg="green",bg="white",borderwidth=6,font="Sans 10 ", border =0)
butSp=Button(so,text="Delete memories",command=Sp, padx=6, pady=13,fg="black",bg="orange",borderwidth=5,font="Sans 10 ", border =0)
butall=Button(so,text="Delete all memory",command=All, padx=2, pady=13,fg="black",bg="orange",borderwidth=5,font="Sans 10 ", border =0)
butper=Button(so,text="Percentage%",command=Per, padx=14, pady=13,fg="black",bg="#D3D3D3",borderwidth=5,font="Sans 10 ", border =0)


butdis.insert(0,"Deg")
butmem.insert(0,"000")

butalphadis.insert(0,"Alpha: Off")

butAns=Button(so,text="Reuse last Ans ",command=Ans, padx=8, pady=13,fg="black",bg="#D3D3D3",borderwidth=5,font="Sans 10 ", border =0)
butAns.grid(row=4,column=7)

but1.grid(row= 1,column=0,padx=8,pady=10)
but2.grid(row= 1,column= 1,padx=8,pady=10)
but3.grid(row= 1,column=2 ,padx=8,pady=10)
but4.grid(row= 2,column=0 ,padx=8,pady=10)
but5.grid(row= 2,column= 1,padx=8,pady=10)
but6.grid(row= 2,column= 2,padx=8,pady=10)
but7.grid(row= 3,column= 0,padx=8,pady=10)
but8.grid(row= 3,column= 1,padx=8,pady=10)
but9.grid(row= 3,column= 2,padx=8,pady=10)
but0.grid(row= 4,column= 0,padx=8,pady=10)
butA.grid(row= 5,column= 0,padx=8,pady=10)
butS.grid(row=6 ,column= 0,padx=8,pady=10)
butM.grid(row=6 ,column= 1,padx=8,pady=10)
butD.grid(row=6 ,column=2 ,padx=8,pady=10)
butEq.grid(row= 5,column= 1,padx=8,pady=10)
butsin.grid(row=1,column=3)
butcl.grid(row= 4,column= 1,padx=8,pady=10)
butexit.grid(row=5,column=2,padx=8,pady=10)
butcos.grid(row=2,column=3,padx=8,pady=10)
buttan.grid(row=3,column=3,padx=8,pady=10)
butcot.grid(row=4,column=3,padx=8,pady=10)
butsec.grid(row=5,column=3,padx=8,pady=10)
butcsc.grid(row=6,column=3,padx=8,pady=10)
butflo.grid(row=4,column= 2,padx=8,pady=10)
butln.grid(row=1,column= 4,padx=8,pady=10)
butlog.grid(row=2,column= 4,padx=8,pady=10)
butlog2.grid(row=3,column= 4,padx=8,pady=10)
butpow.grid(row=4,column= 4,padx=8,pady=10)
butneg.grid(row=5,column= 4,padx=8,pady=10)
butdel.grid(row=6,column= 4,padx=8,pady=10)
butdis.grid(row=1,column=5,ipady=15,padx=8,pady=10)
butmode.grid(row=2,column=5,padx=8,pady=10)
butop.grid(row=3,column=5,padx=8,pady=10)
butclo.grid(row=4,column=5,padx=8,pady=10)
butres.grid(row=5,column=5,padx=8,pady=10)
butmem.grid(row=6,column=5,ipady=15,padx=8,pady=10)
butalphadis.grid(row=1,column=7,ipady=15,padx=8,pady=10)
butAcon.grid(row=2,column=7,padx=8,pady=10)
butSp.grid(row=5,column=7,padx=8,pady=10)
butall.grid(row=6,column=7,padx=8,pady=10)
butper.grid(row=3,column=7,padx=8,pady=10)

root.mainloop()









