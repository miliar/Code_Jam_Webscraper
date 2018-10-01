#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:23:03 2017

@author: ansli
"""
import heapq

def gen(x):
    x -= 1
    return (x - x/2, x/2)

def push(h, n):
    heapq.heappush(h, -n)
    
def pop(h):
    return -heapq.heappop(h)

totalCase = int(raw_input())  # read a line with a single integer
for case in xrange(1, totalCase + 1):
    n, k = [int(s) for s in raw_input().split(" ")]
    h = []
    d = {n: 1}
    push(h, n)
    while k > 0:
        cur = pop(h)
        curCount = d[cur]
        g = gen(cur)
        for r in g:
            if (r in d):
                d[r] += curCount
            else:
                d[r] = curCount
                push(h, r)
        k -= curCount
    print "Case #{}: {} {}".format(case, g[0], g[1])