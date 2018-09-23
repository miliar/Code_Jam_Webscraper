#!/usr/bin/env python

import collections

import math
import re
import sys

#sys.setrecursionlimit(50)

INPUT = "tiny"
INPUT = "B-large.in"
#INPUT = "B-small-attempt0.in"


def debug(*args):
    return
    sys.stderr.write(str(args) + "\n")


class Memoize:
    def __init__(self,function):
        self._cache = {}
        self._callable = function
            
    def __call__(self, *args, **kwds):
        cache = self._cache
        key = self._getKey(*args,**kwds)
        try: return cache[key]
        except KeyError:
            cachedValue = cache[key] = self._callable(*args,**kwds)
            return cachedValue
    
    def _getKey(self,*args,**kwds):
        return kwds and (args, ImmutableDict(kwds)) or args    


def is_tidy(n):
    if n < 10:
        return True
    n, last_digit = divmod(n, 10)
    ld = n % 10
    if ld > last_digit:
        return False
    return is_tidy(n)


def do_trial(N):
    if is_tidy(N):
        return N
    return do_trial((N // 10) - 1) * 10 + 9


f = file(INPUT)
T = int(f.readline()[:-1])
for i in range(T):
    N = int(f.readline()[:-1])
    v = do_trial(N)
    print "Case #%d: %s" % (i+1, v)
