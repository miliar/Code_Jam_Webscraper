#!/usr/bin/env python

import collections
import heapq
import sys

sys.setrecursionlimit(50)

INPUT = "tiny"
INPUT = "C-large.in"
#INPUT = "C-small-1-attempt0.in"
#INPUT = "C-small-2-attempt0.in"


def debug(*args):
    # return
    sys.stderr.write(str(args) + "\n")


def do_trial(N, K):
    c = collections.Counter()
    c[N] = 1
    while K > 0:
        debug("*** %s" % c)
        v = max(t for t in c.keys() if c[t] > 0)
        v1, v2 = v // 2, (v-1) // 2
        cnt = min(c[v], K)
        c[v] -= cnt
        if c[v] == 0:
            del c[v]
        c[v1] += cnt
        c[v2] += cnt
        K -= cnt
    return v1, v2
    


f = file(INPUT)
T = int(f.readline()[:-1])
for i in range(T):
    N, K = [int(x) for x in f.readline().split()]
    v = do_trial(N, K)
    print "Case #%d: %d %d" % (i+1, v[0], v[1])
