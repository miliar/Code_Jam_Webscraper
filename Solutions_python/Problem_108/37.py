#!/usr/bin/python
#A.py
#Author: James Damore
#Created on: May 26, 2012
#Time-stamp: <2012-05-26 10:50:26>
#cat Downloads/-small-attempt0.in | ~/A.py > output.txt

import sys, math, collections, Queue
import numpy as np

def dbgln(a): sys.stderr.write(str(a) + "\n")
def read_ints(lines=None, fmt=int):
    if lines is None: return map(int, raw_input().split())
    return [map(fmt, raw_input().split()) for _ in range(lines)]


def read_input():
    N = input()
    d, l = zip(*read_ints(lines=N))
    D = input()

    best = np.zeros(N)
    best[0] = d[0]
    cur = (0, d[0], d[0])
    Q = [cur]
    while Q:
        cur = Q.pop()
        if cur[1] + cur[2] >= D:
            return "YES"
        if cur[2] < best[cur[0]]:
            continue
        #nexts = []
        #print cur
        for i, dist in enumerate(d[cur[0] + 1:], cur[0] + 1):
            if cur[1] + cur[2] >= dist:
                length = min(dist - cur[2], l[i])
                if best[i] < length:
                    Q.append((i, length, dist))
                    best[i] = length
                #nexts.append((i, min(dist - cur[2], l[i]),
                #              dist))
            else:
                break
        #if nexts:
            #cur = (0, 0, 0)
        #    old = cur
        #    for n in nexts:
        #        if n[1] + n[2] >= cur[1] + cur[2]:
        #            cur = n
        #    if old == cur:
        #        return "YES" if cur[1] + cur[2] >= D else "NO"
        #else:
        #    return "YES" if cur[1] + cur[2] >= D else "NO"
    return "NO"


numCases=input()
for i in range(1, numCases+1):
    #read_input()
    #dbgln(i)
    output = read_input()
    print "Case #%d:" % i, output
