#!/usr/bin/python
from sys import stderr
import sys
sys.setrecursionlimit(1000000)

def memoize(f):
    global cache
    def g(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return g

@memoize
def f(e, i): # e is engine index, i is index in qs
    global qs, S
    if not qs[i:]:
        #print >> stderr, "len(qs), i:", len(qs), i, "return 0"
        return 0 # nothing left
    else:
        q = qs[i] # current query
        min_ = float('inf')
        # try the other engines
        for s in range(S):
            if s != e:
                m = f(s,i+1) + 1 # switched engines, so pay 1
            elif e != q:
                # if the current engine can handle the current query try it for free
                #print >> stderr, "e != q: s,e,q", s,e,q, "calling f(e,i+i)"
                m = f(e,i+1)
            else: 
                #print >> stderr, "s == e == q: s,e,q", s,e,q
                m = min_
            if m < min_: min_ = m
        return min_

def main():
    global cache, eti, qs, S
    N = input()
    for n in range(1,N+1):
        cache = {}
        S = input()
        eti = {} # engine to index
        for s in range(S):
            l = raw_input()
            eti[l] = s
        #print >> stderr, "eti:", eti
        Q = input()
        qs = [] # queries stored as indices
        for q in range(Q):
            q = raw_input()
            qs.append(eti[q])
        #print >> stderr, "qs:", qs

        min_switches = min(f(s,0) for s in range(S))
        print "Case #%i: %i" % (n, min_switches)

main()
