# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 23:42:30 2015

@author: guy
"""


infile = open('2.in','r')
outFile = open('2.out','w')
n = infile.readline()
n = int(''.join(n.split('\n')))



def answer(pancakeList):
    if max(pancakeList) <= 1:
        return max(pancakeList)
    return min(i+sum(map(lambda x: (x-1)//i,pancakeList)) for i in range(1,max(pancakeList)+1))

for i in range(n):
    dontNeed = infile.readline()
    dinerList = list(map(int,infile.readline().split()))
    outFile.write("Case #{0}: {1}\n".format(i+1,answer(dinerList)))
outFile.close()