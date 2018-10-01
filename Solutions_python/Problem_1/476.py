#!/usr/bin/env python

import psyco
psyco.full()

def get(s, q):
    if len(q) == 0: return 0
    last = [0] * len(s)
    for x in q:
        now = [len(q)] * len(s)
        for i in xrange(len(s)):
            if s[i] == x: continue
            for j in xrange(len(s)):
                here = last[j];
                if i != j: here += 1
                if here < now[i]: now[i] = here
        last = now
    return min(last)

n = input()
for x in xrange(n):
    ns = input()
    s = []
    for i in xrange(ns):
        s.append(raw_input())
    nq = input()
    q = []
    for i in xrange(nq):
        q.append(raw_input())
    print 'Case #%d: %s' % (x + 1, get(s, q))
