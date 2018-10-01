#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from itertools import *

def mycmp(a,b):
    if a=='.':
        return -1
    if b=='.':
        return 1
    return 0

N=int(sys.stdin.readline())
for testn in range(1,N+1):
    N,K = map(int, sys.stdin.readline().split())
    arr = []
    for i in range(N):
        arr.append(sys.stdin.readline().strip())
    # print arr
    arr=[sorted(row,cmp=mycmp) for row in arr]
    # print '\n'.join(''.join(x) for x in arr)
    arr=[list(reversed(row)) for row in zip(*arr)]
    # print
    # print '\n'.join(''.join(x) for x in arr)

    dia1 = {}
    dia2 = {}
    for row_index, row in enumerate(arr):
        for col_index, elem in enumerate(row):
            key1=row_index-col_index
            key2=row_index+col_index
            dia1.setdefault(key1,[]).append(elem)
            dia2.setdefault(key2,[]).append(elem)

    g1,g2=tee(chain((''.join(row) for row in arr),
                          (''.join(col) for col in zip(*arr)),
                          (''.join(x) for x in dia1.values()),
                          (''.join(x) for x in dia2.values())))
    r_win, b_win = any(imap(lambda e:e.find('R'*K)!=-1, g1)), any(imap(lambda e:e.find('B'*K)!=-1, g2))
    result = "Neither"
    if r_win and b_win:
        result = "Both"
    elif r_win:
        result = "Red"
    elif b_win:
        result = "Blue"
        
    print "Case #%d: %s" % (testn, result)
    
