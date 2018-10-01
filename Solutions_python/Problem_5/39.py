#! /usr/bin/env python

from __future__ import with_statement

import sys

def read_cases():
    if len(sys.argv) != 2:
        exit(-1)
    with open(sys.argv[1]) as handle:
        cases = int(handle.readline().strip())
        for idx in range(cases):
            yield test_cases(handle)

def test_cases(handle):
    N = int(handle.readline().strip())
    M = int(handle.readline().strip())
    prefs = []
    for i in range(M):
        nums = [int(j) for j in handle.readline().split()]
        curr = []
        for idx in range(0,nums[0]*2,2):
            curr.append((nums[idx+1], nums[idx+2]))
        prefs.append(curr)
    return (N, M, prefs)

def satisified(cust, flavors):
    for p in cust:
        if flavors[p[0]-1] == p[1]:
            return True
    return False

def recurse(prefs, flavors, depth=0):
    if depth >= len(prefs):
        return flavors
    cust = prefs[depth]
    if satisified(cust, flavors):
        return recurse(prefs, flavors, depth+1)
    else:
        for p in cust:
            if flavors[p[0]-1] < 0:
                flavors[p[0]-1] = p[1]
                ret = recurse(prefs, flavors, depth+1)
                if ret:
                    return ret
                flavors[p[0]-1] = -1
        return None

def solve(cid, case):
    (N, M, prefs) = case
    prefs.sort(key=len)
    flavors = [-1] * N
    sol = recurse(prefs, flavors)
    if sol:
        for idx in range(len(sol)):
            if sol[idx] < 0:
                sol[idx] = 0
            sol[idx] = str(sol[idx])
        sol = ' '.join(sol)
    else:
        sol = 'IMPOSSIBLE'
    print "Case #%s: %s" % (cid, sol)

for cid, case in enumerate(read_cases()):
    solve(cid+1, case)