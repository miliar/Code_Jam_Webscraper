#!/usr/bin/python

import sys
import re

infinity = 100000

def f(choices,ses,q,mem):
    t = tuple(q)
    if t in mem:
        return mem[t]
    res = {}
    for x in choices:
        res[x] = simul(x,ses,list(q),mem)
    r = infinity
    for x in res.values():
        if x < r:
            r = x
    mem[t] = r
    return r

def simul(curr,ses,qs,mem):
    if len(qs) == 0:
        return 0
    q = qs.pop()
    if q == curr:
        c = list(ses)
        c.remove(q)
        return f(c,ses,list(qs),mem) + 1
    else:
        return simul(curr,ses,list(qs),mem)

if __name__ == "__main__":
    infile = sys.argv[1]
    lines = open(infile)
    n = lines.next().rstrip()
    for i in range(int(n)):
        s = lines.next().rstrip()
        se = []
        for j in range(int(s)):
            se.append(lines.next().rstrip())
        q = lines.next().rstrip()
        queries = []
        for j in range(int(q)):
            queries.append(lines.next().rstrip())
        queries.reverse()
        print "Case #%i: %s" % (i+1,f(se,se,queries,{}))