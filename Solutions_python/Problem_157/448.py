# -*- coding: utf-8 -*-
"""
Problem C. 
uses python 3.4.1

@author: Eric Kuritzky
"""
from collections import *
import itertools as ito
import operator as op
import functools as ft
from sys import argv, stdin, stdout, stderr, setrecursionlimit

#setrecursionlimit(1000000)

errprt = ft.partial(print, file=stderr)

tbl = [[0, 1, 2, 3], # 1, i, j, k, -1, -i, -j, -k
       [1, 4, 3, 6], # 0  1  2  3   4   5   6   7
       [2, 7, 4, 1],
       [3, 2, 5, 4]]

for irow in range(4):
    row = tbl[irow]
    row.extend([(4+n)%8 for n in row])
    tbl.append(row[4:] + row[:4])

assert all(tbl[a][tbl[b][c]] == tbl[tbl[a][b]][c]
           for a, b, c in ito.product(range(8), repeat=3))

def readcase(f):
    L, X = readints(f)
    s = f.readline().strip()
    assert len(s) == L
    return (X, s)

def solvecase(case, tbl=tbl):
    X, s = case
    s = [ord(c) - ord('h') for c in s]
    v = 0
    for c in s:
        v = tbl[v][c]
    if v==0 or v==4 and X&1 == 0 or v not in (0,4) and X&3 != 2:
        return 'NO'
    start = 0
    ipart = None
    for i in range(min(4, X)):
        w = start
        for j, c in enumerate(s):
            w = tbl[w][c]
            if w == 1:
                ipart = (i, j)
                break
        if w == 1:
            break
        start = tbl[start][v]
    if ipart is None:
        return 'NO'
    start = 0
    kpart = None
    for i in range(min(4, X)):
        w = start
        for j, c in enumerate(s[::-1]):
            w = tbl[c][w]
            if w == 3:
                kpart = (X - i - 1, len(s) - j - 1)
                break
        if w == 3:
            break
        start = tbl[v][start]
    if kpart is None or kpart <= ipart:
        return 'NO'
    else:
        return 'YES'
	
def readints(f):
    return list(map(int, f.readline().strip().split(' ')))

def readflds(f, types):
    if isinstance(types, tuple):
        return [typ(fld) for fld, typ
                in zip(f.readline().strip().split(),
                       ito.chain(types, ito.repeat(types[-1])))]
    else:
        return [types(fld) for fld in f.readline().strip().split()]

def main():
    with open('C-large.in') as f, open('out', 'w') as out:
        cases = int(f.readline())
        for ncase in range(1, cases+1):
            case = readcase(f)
            soln = solvecase(case)
            print('Case #%d: %s' % (ncase, soln))
            print('Case #%d: %s' % (ncase, soln), file=out)

from datetime import datetime

start = datetime.now()
print(str(start))
main()
stop = datetime.now()
print(str(stop-start))
