#! /usr/bin/env python

import sys

def solve(a, b):
    recycled = 0
    for num in range(a, b+1):
        snum = str(num)
        unique = set()
        for i in range(-1, -1 * len(snum), -1):
            if snum[i] != '0':
                t = snum[i:] + snum[:i]
                v = int(t)
                if v > num and v <= b:
                    unique.add(v)
        recycled += len(unique)
    return recycled 


with open(sys.argv[1], 'r') as f:
    discard = True
    count = 1

    for line in f:
        if discard:
            discard = False
            continue


        (a, b) = line.rstrip().split()
        result = solve(int(a), int(b))
        print "Case #%s: %s" % (count, result)
        count += 1
