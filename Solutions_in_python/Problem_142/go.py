#!/usr/bin/env python

import collections
import itertools

import math
import re
import sys

#sys.setrecursionlimit(50)

INPUT = "tiny"
#INPUT = "C-large.in"
INPUT = "A-small-attempt0.in"

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

def counts_for_string(s):
    chars = []
    counts = []
    count = 0
    this_char = None
    for idx, c in enumerate(s):
        if c == this_char:
            count += 1
        else:
            if count:
                counts.append(count)
                chars.append(this_char)
            this_char = c
            count = 1
    counts.append(count)
    chars.append(this_char)
    return ''.join(chars), counts

assert counts_for_string("aabbccc") == ("abc", [2,2,3])

def fastest(vals):
    debug(vals)
    best = 1e8
    for v in set(vals):
        total = sum(abs(k - v) for k in vals)
        best = min(total, best)
    debug("***", vals, best)
    return best

def do_trial(strings):
    rv = [counts_for_string(s) for s in strings]
    debug(rv)
    if len(set(c[0] for c in rv)) > 1:
        return "Fegla Won"
    counts = [r[1] for r in rv]
    debug(counts)
    total = 0
    for vals in zip(*counts):
        total += fastest(vals)
    return total

f = file(INPUT)
T = int(f.readline()[:-1])
for i in range(T):
    N, = [int(x) for x in f.readline().split()]
    strings = []
    for k in range(N):
        strings.append(f.readline()[:-1])
    v = do_trial(strings)
    print "Case #%d: %s" % (i+1, v)
