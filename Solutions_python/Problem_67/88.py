#!/usr/bin/env python3.1

from itertools import count
import copy
import sys

def readline():
    return next(sys.stdin).strip()

def readvals(t):
    return map(t, readline().split())

def memoize(func):
    cache = {}
    def f(*args, **kw):
        key = func.__module__, func.__name__, args
        if kw:
            key += frozenset(kw.iteritems()),
        try:
            return cache[key]
        except KeyError:
            cache[key] = result = func(*args, **kw)
            return result
    return f

def pr(ground):
    def repr(v):
        if v:
            return '+'
        else:
            return '.'
    for row in ground[:6]:
        print(''.join(map(repr, row[:6])))
    print()

ncases = int(readline())
for caseno in range(ncases):
    R = int(readline())

    ground = [[False] * 101 for _ in range(101)]
    
    for i in range(R):
        x1, y1, x2, y2 = readvals(int)
        for r in range(y1, y2 + 1):
            for c in range(x1, x2 + 1):
                ground[r][c] = True

    for turn in count(1):
        newground = copy.deepcopy(ground)
        for r in range(1, 101):
            for c in range(1, 101):
                if ground[r][c]:
                    newground[r][c] = ground[r - 1][c] or ground[r][c - 1]
                else:
                    newground[r][c] = ground[r - 1][c] and ground[r][c - 1]
        if all(not any(row) for row in newground):
            break
        ground = newground
    
    print('Case #{}: {}'.format(caseno + 1, turn))
    sys.stdout.flush()
