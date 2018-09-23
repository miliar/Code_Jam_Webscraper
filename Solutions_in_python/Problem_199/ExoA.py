# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:45:16 2017

@author: Julien
"""


import os

s='---------'
k=3

def solve(s,k):
    a=[]
    for i in s:
        if i=='-':
            a.append(1)
        else:
            a.append(0)
    
    counter=0
    while(len(a)>k):
        if sum(a)==0:
            return counter

         
#        print(a)
        if a[0]==0:
            a.pop(0)
        else:
            counter+=1
            a.pop(0)
            for i in range(k-1):
                a[i]=(a[i]+1)%2
        
        if sum(a)==0:
            return counter
        
#        print("apres 1er flip")         
#        print(a)

        if a[-1]==0:
            a.pop()
        else:
            counter+=1
            a.pop()
            
            for i in range(k-1):
                a[-i-1]=(a[-1-i]+1)%2

#        print(a)


    if sum(a)==0:
        return counter
    elif sum(a)==k:
        return counter +1 
    else:
        return 'IMPOSSIBLE'
            
       
#print(solve(s,k))



#
fh="A-large.in"
chem="C:\CodeJam\ExoA"
fhOut='Solution_'+fh

with open(os.path.join(chem,fh),'r') as f:
    with open(os.path.join(chem,fhOut),'w') as fOut:
        CASE=int(f.readline())
        
        for c in range(CASE):
            l=(f.readline())
            [s,k]=l.split()
            k=int(k)
            
            res=solve(s,k)
#            print(s +str(k))
#            print(res)
            fOut.write("Case #" +str(c+1) + ': ' + str(res) +'\n')