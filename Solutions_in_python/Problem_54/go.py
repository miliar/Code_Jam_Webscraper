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

def gcf(a, b):
    #print "gcf", a, b
    a,b = min(a,b), max(a,b)
    while a>0:
        a, b = b%a, a
    return b

def do_trial(vals):
    #import pdb; pdb.set_trace()
    vals.sort()
    first_val = vals[0]
    new_vals = [v-first_val for v in vals if v>first_val]
    big_gcf = reduce(gcf, new_vals)
    remainder = first_val % big_gcf
    if remainder == 0: return 0
    return big_gcf - remainder

#f = file("B-small-attempt1.in.txt")
#f = file("1")
#f = file("tiny")
f = file("B-large.in.txt")
C = int(f.readline()[:-1])
for i in range(C):
    vals = [int(x) for x in f.readline()[:-1].split()]
    v = do_trial(vals[1:])
    print "Case #%d: %s" % (i+1, v)
