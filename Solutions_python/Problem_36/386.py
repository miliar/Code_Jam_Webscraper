#!/usr/bin/env python2.6
import sys
import bisect
from collections import defaultdict

string = "welcome to code jam"
L = len(string)

with open(sys.argv[1], "r") as f:
    k = int(f.readline().strip())
    tests = [f.readline().strip() for i in range(k)]


def get_positions(s):
    positions = defaultdict(list)
    for i, c in enumerate(s):
        positions[c].append(i)
    return positions


def find(current, pos, char_p, memo):
    current_char = string[current]

    ccp = char_p[current_char]
    
    f = bisect.bisect_left(ccp, pos)
    C = len(ccp)

    if f == C:
        return 0
    elif current == L - 1:
        return len(ccp[f:])
    else:
        d = 0
        while f < len(ccp):
            e = f
            while e + 1 < C and ccp[e] == ccp[e+1] + 1:
                e += 1
            
            key = (current + 1, ccp[e])
            try:
                sub = memo[key]
            except KeyError:
                sub = memo[key] = (f - e + 1) * find(current + 1, ccp[e], char_p, memo)
            d += sub
            f = e + 1
        return d


for i, t in enumerate(tests):
    r = "%04d" % (find(0, 0, get_positions(t), {}), )
    print "Case #%d: %s" % (i + 1, r[-4:])
