#!/usr/bin/env python
import sys
import math
import string

wincheck = [[]]

ways = 0
for y in xrange(0,4):
    for x in xrange(0,4):
        wincheck[ways] += [[x,y]]
    wincheck += [[]]
    ways = ways + 1

for x in xrange(0,4):
    for y in xrange(0,4):
        wincheck[ways] += [[x,y]]
    wincheck += [[]]
    ways = ways + 1

for d in xrange(0,4):
    wincheck[ways] += [[d,d]]
wincheck += [[]]
ways = ways + 1
for d in xrange(0,4):
    wincheck[ways] += [[3-d,d]]


cases = int(sys.stdin.readline())

def solve(arr):
    complete = True
    for tchar in [ 'O', 'X' ]:
        for way in wincheck:
            row = 0
            for w in xrange(0,4):
                x = way[w][0]
                y = way[w][1]
                char = arr[x][y]
                if char == '.':
                    complete = False
                    continue
                elif tchar == char or char == 'T':
                    row = row + 1
                    if row == 4:
                        return tchar + ' won'

    if complete:
        return 'Draw'
    else:
        return 'Game has not completed'


for c in xrange(cases):
    arr = [['']*4 for i in range(4)]
    for y in xrange(0,4):
        line = sys.stdin.readline()
        for x in xrange(0,4):
            arr[x][y] = line[x]

    print "Case #" + str(c+1) + ": " + solve(arr)
    line = sys.stdin.readline()

