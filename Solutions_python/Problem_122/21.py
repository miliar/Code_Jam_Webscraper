#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from sys import stderr, setrecursionlimit
from collections import deque
from itertools import *
import sys
from sys import stderr
from collections import deque, defaultdict
from itertools import *
from math import *
from pprint import pprint
from bisect import *
import random
data = deque(map(int,sys.stdin.read().split()))
token = data.popleft

# Bisect_right
def bisect_right_fun(b, e, callback):
    if b == e:
        return e - 1

    m = int((b+e)/2)
    if callback(m):
        return bisect(m+1, e, callback)
    else:
        return bisect(b, m, callback)

maps = {}
def genMaps():
    for sel in product(*([[2,3,4,5]]*3)):
        if list(sorted(sel)) != list(sel):
            continue
        r = []
        for i in range(4):
            for c in combinations(sel, i):
                cr = 1
                for val in c:
                    cr *= val
                r.append(cr)
        maps[''.join(map(str,sel))] = list(set(r))
#    pprint(maps)


def mainSmall():
    def test():
        R = token()
        N = token()
        M = token()
        K = token()

        def run():
            v = [token() for _ in range(K)]
            keys = maps.keys()
            for i in v:
                keys = filter(lambda k: i in maps[k], keys)
#                print i, keys

            if not len(keys):
                print "222"
            else:
                print >> stderr, len(keys)
                print random.choice(keys)

        for _ in xrange(R):
            run()

    T = int(token())
    for case in xrange(1, T+1):
        print "Case #%d:" % (case,)
        test()
        sys.stdout.flush()

if __name__ == '__main__':
    genMaps()
    mainSmall()
