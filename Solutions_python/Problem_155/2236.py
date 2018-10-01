#!/usr/bin/env python
# -*- coding: utf-8 -*-

def process(num):

    text = input().split(" ")
    text = list(map(str, text))
    
    if len(text)!=2  :
        return

    smax = int(text[0])
    kvalues = str(text[1])
   
    if (smax > smax_val) | (smax < smin_val):
        return
    
  
    if ((len(kvalues)-1) != smax):
        print(kvalues)
        return
    
    total_clap = 0
    invite = 0
    
    for s,k in enumerate(kvalues):
        
        if k!=0:
            while s > total_clap:
                total_clap +=1
                invite +=1

        total_clap += int(k)
            

    return "Case #"+ str(num+1) +": " +str(invite) + "\n"
            
            

global tmax
global tmin
global smax_val
global smin_val

tmax = 100
tmin = 1
smax_val = 1000
smin_val = 0


global metin
metin=""

tnumber = int(input(""))
    
if (tnumber <= tmax) & (tnumber >= tmin):
    for num in range(0,tnumber):
        metin += process(num)


dosya = open("answer2.txt", "w")
dosya.write(metin)
dosya.close()
