#!/usr/bin/python

import sys

def prefixes(s):
    return set([s[:i] for i in range(len(s) + 1)])

def prefixnum(strset):
    ps = set([])
    for s in strset:
        ps |= prefixes(s)
    return len(ps)

def solve(servernum, unassigned, ass):
    if len(unassigned) == 0:
        the = [[i for i in ass if ass[i] == k] for k in range(servernum)]
        return (sum(prefixnum(strset) for strset in the), 1)
    maxx = 0
    maxct = 0
    for i in range(servernum):
        ass[unassigned[0]] = i
        a, ct = solve(servernum, unassigned[1:], ass)
        if a > maxx:
            maxx = a
            maxct = ct
        elif a == maxx:
            maxct += ct
    try:
        del ass[unassigned[0]]
    except:
        pass
    return (maxx, maxct)

cases = int(sys.stdin.readline())

for casenum in range(1, cases+1):
    strnum, servers = map(int, sys.stdin.readline().split())
    strs = []
    for i in range(strnum):
        strs.append(sys.stdin.readline().strip())
    a, b = solve(servers, strs, {})
    
    print 'Case #{}: {} {}'.format(casenum, a, b)
    print >> sys.stderr, casenum
