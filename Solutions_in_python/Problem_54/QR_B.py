#!/usr/bin/python

import sys
import fractions
import math

def abs(x):
    if (x>0):
        return x
    else:
        return -x

def main():
    sC = sys.stdin.readline()
    C = int(sC)
    for t in xrange(C):
        sL = sys.stdin.readline()
        sN = [long(z) for z in sL.split()]
        g = 0
        for i in xrange(len(sN)-2):
            g = fractions.gcd(g,sN[i+1]-sN[i+2])
            g = abs(g)
        r = g - sN[1] % g
        if r == g:
            r = 0
        print "Case #"+str(t+1)+": "+str(r)

if __name__ == "__main__":
    main()
