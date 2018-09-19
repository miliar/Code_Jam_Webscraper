#!/usr/bin/python
import sys
import itertools

def checkPerm(perm):
    seen = set()
    last = None
    for car in perm:
        for c in car:
            #print c, seen, last
            if c in seen and (last is not None and c != last):
                return False
            else:
                seen.add(c)
                last = c
    return True

def simplify(s):
    last = None
    out = []
    for c in s:
        if c != last:
            out.append(c)
        last = c
    return "".join(out)

T = int(sys.stdin.readline())
for i in xrange(T):
    print "Case #%d:" % (i+1),
    N = int(sys.stdin.readline().strip())
    cars = sys.stdin.readline().strip().split(" ")
    for i in xrange(len(cars)):
        cars[i] = simplify(cars[i])
    #print cars
    total = 0
    for perm in itertools.permutations(cars):
        if checkPerm(perm):
            total += 1
    print total
