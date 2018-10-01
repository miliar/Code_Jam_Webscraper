#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

from collections import Counter
import math


def last_will(n):
    """
    i'm tired pls i can't think
    """
    if n % 2:
        return (n-1)/2,(n-1)/2
    elif n:
        return n/2,(n/2)-1
    else:
        return 0,0

def more_quick(n,k):
    log = int(math.log(k,2))
    tour = 0
    c = Counter({n : 1})
    for j in range(log):
        tour += 2**j
        for i,nb in c.items():
            if i % 2 != 0:
                c[(i-1)/2] += nb*2
                del c[i]
            elif i:
                c[(i/2)-1] += nb
                c[i/2] += nb
                del c[i]
            else:
                c[i] += nb
    while tour < k-1:
        big = max(c)
        nb = c[big]
        cc = nb
        if sum(c.values()) >= k+1:
            break
        if big % 2 != 0:
            c[(big-1)/2] += cc*2
            c[big] -= cc*1
        elif big:
            c[(big/2)-1] += cc*1
            c[big/2] += cc*1
            c[big] -= cc*1
        if c[big] == 0:
            del c[big]
        tour += cc
    return last_will(max(c))

def slowpoke():
    """
    slowest than bogo
    """
    l = [n]
    tmp = n
    c = Counter()
    for j in range(k):
        a = l.pop(0)
        u,v = choose(a)
        l.append(u)
        l.append(v)
        l.sort(reverse=True)
        c[a] += 1


def main():
    """
    Do the job.
    """
    t = int(sys.stdin.readline())
    for i in range(t):
        n, k = map(int, sys.stdin.readline().split())
        #u,v = more_quick(n,k)
        l = [n]
        tmp = n
        c = Counter()
        for j in range(k):
            a = l.pop(0)
            u,v = last_will(a)
            l.append(u)
            l.append(v)
            l.sort(reverse=True)
            c[a] += 1
        print("Case #%s: %s %s" % (i+1, u, v))
main()
