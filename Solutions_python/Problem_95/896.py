#!/usr/bin/env python

#
# Copyright (c) 2012 J.M. Dana
#

import fileinput
import string
import sys
import os
import re

theDict={}

source = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qz'
target = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zq'

for idx,s in enumerate(source):
    theDict[s]=target[idx]
    
def doit(x):
    out=''
    
    for i in x:
        out+=theDict[i]
        
    return out

theIN=fileinput.FileInput()

N = int(theIN.readline())

for case in range(1,N+1):
    line=theIN.readline().strip('\n')

    print 'Case #%d: %s' % (case,doit(line))

