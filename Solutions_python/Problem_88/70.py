#!/usr/bin/env python
# coding=utf-8
from __future__ import division
from sys import stdin

def avg(data):
    res = sum(data)/len(data)
    return res

def dist(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**.5

def check(M, xl, xr, yl, yr):
    #print("check({0}, {1}, {2}, {3})".format(xl, xr, yl, yr))
    mid = [0,0]
    mx = (xl+xr)/2
    my = (yl+yr)/2
    for x in range(xl, xr+1):
        for y in range(yl, yr+1):
            if (y,x) in ((yl,xl), (yl,xr), (yr,xl), (yr,xr)):
                continue
            m = M[y][x]
            mid[0] += m*(x-mx)
            mid[1] += m*(y-my)
            #print("{0}:{1}".format((x,y), mid))
    #print(mid)
    return mid == [0,0]


def solve(caseNo):
    res = "IMPOSSIBLE"
    R, C, D = map(int, stdin.readline().strip().split())
    M = [ map(int, stdin.readline().strip()) for i in range(R)]
    for k in range(3, min(R,C)+1):
        for y in range(R-k+1):
            for x in range(C-k+1):
                if check(M, x, x+k-1, y, y+k-1):
                    res = k

    print("Case #{0}: {1}".format(caseNo, res))

if __name__ == "__main__":
    cases = int(stdin.readline().strip())
    for i in range(cases):
        solve(i+1)
