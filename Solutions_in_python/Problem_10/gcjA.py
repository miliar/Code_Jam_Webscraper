#!/usr/bin/python

import sys
import re

infinity = 100000

sys.setrecursionlimit(infinity)

def f(p,k,l,freq):
    #e = enumerate(freq)
    #s = sorted(e,lambda x,y: x[1] - y[1])
    s = sorted(freq)
    key = k
    depth = 1
    total = 0
    for i in range(l):
        if key == 0:
            key = k
            depth = depth + 1
        highest = s.pop()
        total = total + depth * highest
        key = key - 1
    if depth > p:
        return "Impossible"
    return total
    
if __name__ == "__main__":
    infile = sys.argv[1]
    lines = open(infile)
    n = lines.next().rstrip()
    for i in range(int(n)):
        l1 = lines.next().rstrip()
        (p,k,l) = map(int,l1.split(" "))
        l2 = lines.next().rstrip()
        freq = map(int,l2.split(" "))
        print "Case #%i: %s" % (i+1,f(p,k,l,freq))