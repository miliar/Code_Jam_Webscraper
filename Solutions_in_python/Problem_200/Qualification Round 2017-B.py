#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Bilal Saim 2017 [Bilisel]
'''
import math
import sys
import os

def algorithm(num,inval):
    ##########################
    #Code Area
    d = inval.readline().strip()
    t = int(d)
    elde = False
    for i in range(len(d)-1,0,-1):
        
        if int(d[i]) < int(d[i-1]) or elde or d[i] == "0":
            
            for j in range(i,len(d)):
                d = d[:j] + "9" + d[j + 1:]
            if d[i-1] == "1" and i-1 == 0:
                d = d[1:]
            elif d[i-1] == "0":
                elde = True
            else:
                a = int(d[i-1])-1
                d = d[:i-1] + str(a) + d[i:]
                elde = False
            


    result = d
    #
    ##########################
    return "Case #"+ str(num+1) +": " + result + "\n"


##########################
#CODES FOR LAZYJAM
##########################
text = ""
data = "test"
infile = "Input-test.txt"
print("Running...")
if os.path.isfile("Operation.txt"):
    with open("Operation.txt","r") as t:
        data = t.readline().strip()
        infile = t.readline().strip()

#We read input values from file
inval = open(infile,"r")

#If there is limit for case!
tnumber = int(inval.readline().strip())
    
for num in range(0,tnumber):
    text += algorithm(num,inval)

dosya = open("Output-"+data+".txt", "w")
dosya.write(text)
dosya.close()

print("Output:")
print(text)

#print(text)
if data == "test":
    with open("Output.txt") as t:
        a = t.readlines()
    with open("Output-test.txt") as t:
        b = t.readlines()

    if a==b:
        print("Results are smiliar")
    else:
        print("Results didn't match!")
