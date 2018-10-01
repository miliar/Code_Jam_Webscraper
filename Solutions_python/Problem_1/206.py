#!/usr/bin/env python

import sys

f=sys.stdin
n=int(f.next())

for case in range(1, n+1):
    S=int(f.next())
    engines = set( f.next() for i in range(S) )
    Q=int(f.next())
    queries = [ f.next() for i in range(Q) ]
    
    e=set(engines)
    changes = 0
    for q in queries:
        e.discard(q)
        if not e:
            changes += 1
            e=set(engines)
            e.discard(q)
    print "Case #%s: %s"%(case,changes)


