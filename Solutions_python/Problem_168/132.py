#!/usr/bin/env python

import collections

import math
import re
import sys

#sys.setrecursionlimit(50)

INPUT = "tiny"
INPUT = "A-small-attempt1.in"
INPUT = "A-large.in"
#INPUT = "C-small-attempt0.in"

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

DIRS = {
    "^" : (0, -1),
    "v" : (0, 1),
    "<" : (-1, 0),
    ">" : (1, 0)
}

def do_trial(rows):
    count = 0
    height = len(rows)
    width = len(rows[0])
    bad = []
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(set())
        bad.append(row)

    for x in range(width):
        y = 0
        while y < height:
            if rows[y][x] == ".":
                y += 1
                continue
            bad[y][x].add("^")
            break

    for x in range(width):
        y = height - 1
        while y >= 0:
            if rows[y][x] == ".":
                y -= 1
                continue
            bad[y][x].add("v")
            break

    for y in range(height):
        x = 0
        while x < width:
            if rows[y][x] == ".":
                x += 1
                continue
            bad[y][x].add("<")
            break

    for y in range(height):
        x = width - 1
        while x >= 0:
            if rows[y][x] == ".":
                x -= 1
                continue
            bad[y][x].add(">")
            break

    for r in rows:
        debug(r)

    for r in bad:
        debug(r)

    #import pdb; pdb.set_trace()
    count = 0
    for x in range(width):
        for y in range(height):
            if len(bad[y][x]) >= 4:
                return "IMPOSSIBLE"
            if rows[y][x] in bad[y][x]:
                count += 1
    return count


f = file(INPUT)
T = int(f.readline()[:-1])
for i in range(T):
    R, C = [int(x) for x in f.readline().split()]
    rows = []
    for _ in range(R):
        row = f.readline()[:-1]
        rows.append(row)
    v = do_trial(rows)
    print "Case #%d: %s" % (i+1, v)
