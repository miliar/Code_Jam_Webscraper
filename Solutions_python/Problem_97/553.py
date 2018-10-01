#!/usr/bin/env python

import sys

def recycled(a,b):
    pairs = set()
    count = 0

    for i in range(a,b+1):
        s = str(i)
        if s in pairs:
            continue

        paircount = 1
        for j in range(1,len(s)):
            r = s[j:] + s[:j]
            if r[0] == '0' or r in pairs or r == s: 
                continue            
            c = int(r)
            if c >= a and c <= b:
                paircount = paircount + 1
                pairs.add(r)
                
        if paircount > 1:
            count = count + comb(paircount)
            pairs.add(s)

    return count
    
def comb(n):
    return n * (n-1) / 2

lines = sys.stdin.readline()
c = 1
for i in sys.stdin:
    (a,b) = i.strip().split(' ')
    print "Case #%d:" % (c), recycled(int(a),int(b))
    c = c+1
