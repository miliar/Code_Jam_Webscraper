#!/usr/bin/env python

import sys

T = int(raw_input())
numbers = set(range(1,10))
ignore = lambda x : sorted(i for i in str(x) if int(i) > 0)
for t in range(T):
    N = int(raw_input())
    a = ignore(N)
    b = set(a)
    d = N + 1
    while True:
        e = ignore(d)
        if set(e) == b and e == a:
            break
        else:
            d += 1
    print "Case #%d: %d" % (t+1, d)
    sys.stdout.flush()
        
    
