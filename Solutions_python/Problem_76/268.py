#!/usr/bin/python

__author__ = "Thomas van den Berg"

# from itertools import izip, permutations
# from numpy import *

fn = 'C-large.in'
f = open(fn,'r')
fout = open(fn.replace('.in','.out'),'w')

T = int(f.readline())
for case in xrange(T):
    
    N = int(f.readline())
    c = [int(nm) for nm in f.readline().split()]
    
    # Determine if possible
    total = reduce(lambda x,y: x ^ y, c)
    
    if total != 0:
        ans = 'NO'
    else:
        ans = sum(c) - min(c)
    
    fout.write('Case #%d: %s\n'%(case+1,ans))
    
