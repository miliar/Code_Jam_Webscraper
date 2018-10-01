#!/usr/bin/python
import sys, math        

T = int(sys.stdin.readline())
for t in range(T):
    s, ks = sys.stdin.readline().strip().split(" ")
    k = int(ks)
    ls = list(s)
    l = len(s)
    flips = 0
    result = ''
    for i in range(len(s)):
        if ls[i] == '+':
            continue
        if k+i > l:
            result = "IMPOSSIBLE"
            break
        for j in range(k):
            ls[i+j] = '-'  if ls[i+j] == '+' else '+'
        flips += 1

    if len(result) == 0:
        result = str(flips)

    print "Case #%d: %s" % ((t + 1), result)
