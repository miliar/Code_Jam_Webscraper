#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
http://code.google.com/codejam/contest/dashboard?c=975485#s=p3
GoroSort
'''

import sys, re, math

def lin(): return sys.stdin.readline()
def ints(): return [int(s) for s in lin().split()]

ncases = ints()[0]
for casenum in range(ncases):
    N = ints()[0]
    ls = ints()
    ans = 0
    for i in range(N):
        if ls[i]!=i+1:
            ans +=1
    print "Case #%d: %d.000000" % (casenum+1, ans)
