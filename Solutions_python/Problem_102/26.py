#!/usr/bin/python

# google code jam - c.durr - 2012

#
#

try:
    import psyco
except:
    pass

from math import *
from fractions import *

def readint():    return int(raw_input())
def readarray(f): return map(f, raw_input().split())

def needs(p, q):
    retval =0
    for pi in p:
        if pi<q:
            retval += q-pi
    return retval

def minScore(p):
    low = 0.
    top = 1.
    while (top-low>1e-9):
        mid = (top+low)/2.
        if needs(p,mid)>=1:
            top = mid
        else:
            low = mid
    return low


for test in range(readint()):
    t = readarray(float)
    n = t[0]
    s = t[1:]
    X = float(sum(s))
    p = [si/X for si in s]
    print "Case #%i:"% (test+1),
    m = minScore(p)
    for pi in p:
        print max(0,m-pi)*100.0,
    print
    
    
