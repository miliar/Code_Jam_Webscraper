# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:21:05 2017

@author: pellowes
"""

import numpy as np
import sys
from queue import PriorityQueue

fileIn = '/Users/pellowes/test.in'
fileIn = '/Users/pellowes/Downloads/C-small-1-attempt0.in'
fileIn = '/Users/pellowes/Downloads/C-small-2-attempt1.in'
fileOut = fileIn.split('.')[0]+'.out'

f = open(fileIn,'r')
fo = open(fileOut,'w')
    

    
def solve1(stalls,poopers):
    #maintain a PriorityQueue of all lengths of free stalls
    #maintain the last set of stalls entered. 
    availableStalls = PriorityQueue()
    availableStalls.put(-1*stalls)
    for i in range(0,poopers):
        block = int(availableStalls.get())
        if(block%2==1):
            bigger = block//2+1
            smaller = block//2+1
        else:
            bigger = block//2
            smaller = (block//2)+1
        availableStalls.put(bigger)
        availableStalls.put(smaller)
    return(str(-1*bigger)+' '+str(-1*smaller))
    
def solve2(stalls,poopers):
    #attempt an analytical approach
    toSplit = 1
    while True:
        if(poopers <= toSplit):
            break
        poopers -= toSplit
        stalls = (stalls-1)/2
        toSplit*=2
    #print(toSplit)
    #print(poopers)
    #print(stalls)
    if(poopers/toSplit <= stalls-int(stalls)):
        remaining = int(stalls)+1
    else:
        remaining = int(stalls)
    if(remaining%2==1):
        #print(str(remaining//2)+' '+str(remaining//2))
        return(str(remaining//2)+' '+str(remaining//2))
    else:
        #print(str(remaining//2)+' '+str(remaining//2 - 1))
        return(str(remaining//2)+' '+str(remaining//2 - 1))

numcases = int(f.readline())
for casenum in range(1,numcases+1):
    problem = f.readline().strip().split(' ')
    stalls = int(problem[0])
    poopers = int(problem[1])
    #print('---')
    fo.write('Case #' + repr(casenum) + ': ' + solve2(stalls,poopers)+'\n')
    
f.close()
fo.close()