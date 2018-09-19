#!/usr/bin/python
import sys
import numpy as np     # http://www.numpy.org/
import scipy           # http://scipy.org/
import networkx as nx  # https://networkx.github.io/
import sympy           # http://www.sympy.org
import itertools
import operator
import string
import fractions
#import visual      # vpython.org
#import Levenshtein  #  https://pypi.python.org/pypi/python-Levenshtein/0.12.0
import cmath

sys.setrecursionlimit(5000)

T = int(sys.stdin.readline())

charmap = {'.':0, '^': 1, 'v':-1,'>':2,'<':2}

dirR = {'.':0, '^': 1, 'v':-1,'>':0,'<':0}
dirC = {'.':0, '^': 0, 'v':0,'>':1,'<':-1}


def test(field):
    bools = field!='.'
    d1 = np.sum(bools,axis=1)
    d2 = np.sum(bools,axis=0)
    for i in range(R):
        for j in range(C):
            if field[i,j]=='.': continue
            if d1[i]==1 and d2[j]==1: return "IMPOSSIBLE"

    count = 0
    for i in range(R):
        for j in range(C):
            if field[i,j]=='.': continue
            if field[i,j]=='<': 
                count+=1
            break
            
        for j in range(C):
            if field[i,C-j-1]=='.': continue
            if field[i,C-j-1]=='>': 
                count+=1
            break

    for j in range(C):
        for i in range(R):
            if field[i,j]=='.': continue
            if field[i,j]=='^':
                count+=1
            break
            
        for i in range(R):
            if field[R-i-1,j]=='.': continue
            if field[R-i-1,j]=='v': 
                count+=1
            break
    return str(count)
    

for case in range(0, T):
    R,C = map(int,sys.stdin.readline().strip().split())
    field = np.chararray( (R,C))

    for i in range(R):
        line=sys.stdin.readline().strip()
        for c in range(len(line)):
            field[i,c] = line[c]

    solution = test(field)
    print "Case #%i: %s" % (case + 1, solution)

