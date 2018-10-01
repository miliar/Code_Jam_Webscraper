#!/usr/bin/env python3.2

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

def ooo(numbers):
    return sum(i + 1 != n for i, n in enumerate(numbers))

ncases = int(readline())
for caseno in range(ncases):
    _ = readvals(int)
    numbers = readvals(int)
    print('Case #{}: {:f}'.format(caseno + 1, ooo(numbers)))
    sys.stdout.flush()
