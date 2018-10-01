#!/usr/bin/env python

#
# Copyright (c) 2012 J.M. Dana
#

import fileinput
import string
import sys
import os
import re


def doit(a,b):
    count=0
    
    theList=[]
    
    for x in range(a,b+1):
        n=[int(i) for i in str(x)]
        l=[n[i:] + n[:i] for i in range(1,len(n))]
        
        for i in l:        
            m=int(string.join(['%s' % y for y in i]).replace(' ',''))
                    
            if len(n) == len(i) and x < m <= b:
                if (x,m) not in theList:
                    theList.append((x,m))
                    count+=1
    
    return len(theList)

theIN=fileinput.FileInput()

N = int(theIN.readline())

for case in range(1,N+1):
    a,b=map(int,theIN.readline().strip('\n').split(' '))

    print 'Case #%d: %s' % (case,doit(a,b))

