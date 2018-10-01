#!/usr/bin/env python

import sys

f = open(sys.argv[1], 'r')
T = int(f.readline())

def possible(lawn,rows, cols):
    # for every cell, is there a path out
    for r in range(rows):
        for c in range(cols):
            v = lawn[r][c]
            # walk left
            path = [lawn[r][x] for x in range(0,c+1)]
            Hpath = max(path) <= v
            # walk right
            path = [lawn[r][x] for x in range(c,cols)]
            # need to get out left and right
            Hpath &= max(path) <= v
            # walk north
            path = [lawn[x][c] for x in range(r+1)]
            Vpath = max(path) <= v
            # walk south
            path =  [lawn[x][c] for x in range(r,rows)]
            Vpath &= max(path) <= v
            Qpath = Hpath | Vpath
            if not Qpath:
                return False
    return True
            

for i in range(T):
    rows, cols = map(int, f.readline().split())
    lawn = []
    for r in range(rows):
        lawn.append(map(int, f.readline().split()))
    if possible(lawn,rows,cols):
        print "Case #%d: YES" % (i + 1)
    else:
        print "Case #%d: NO" % (i + 1)
    
