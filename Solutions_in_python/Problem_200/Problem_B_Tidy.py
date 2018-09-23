# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 12:36:15 2017

@author: Ghomam
"""
import sys
import numpy as np

def isTidy(x):
    y = str(x)
    return sum(list(np.int32(np.array([ int(y[i])-int(y[i-1]) for i in range(1, len(y)) ]) < 0))) == 0

def nextTidy(x):
    y = str(x)
    try:
        k = list(np.int32(np.array([0]+[ int(y[i])-int(y[i-1]) for i in range(1, len(y)) ]) < 0)).index(1)
        while k:
            y = y[:k-1] + str(int(y[k-1])-1) + '9'*len(y[k:])
            try:
                k = list(np.int32(np.array([0]+[ int(y[i])-int(y[i-1]) for i in range(1, len(y)) ]) < 0)).index(1)
            except:
                break
    except:
        pass
    return int(y)

#Open Test file
f = open(sys.argv[1])
data = f.readlines()
f.close()

# Input
tests = []
for t in data[1:]:
    tests.append( int(t) )

output = []
for n in tests:
    result = 0
    output += [nextTidy(n)]
    
#Output
result = open(sys.argv[1].replace('in', 'out'), 'w')
for i, r in enumerate(output):
    out = 'Case #{}: {}'.format(i+1, r)
    print out
    result.write(out+'\n')
result.close()