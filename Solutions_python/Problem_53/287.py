#!/usr/bin/env python

import re
import sys

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

def do_trial(N,K):
    while N>1:
        #print N, K
        if K%2!=1:
            return "OFF"
        K=K/2
        N=N-1
    if K%2!=1:
        return "OFF"
    return "ON"

f = file("A-large.in.txt")
#f = file("tiny")
T = int(f.readline()[:-1])
for i in range(T):
    N, K = [int(x) for x in f.readline()[:-1].split()]
    v = do_trial(N,K)
    print "Case #%d: %s" % (i+1, v)
