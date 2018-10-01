#! /usr/bin/env python

from __future__ import division

import itertools

read_int = lambda: int(raw_input())

def best_time(cost, boost, win):
    prod = 2
    for n in itertools.count(0):
        if win / (prod + n * boost) < cost / (prod + n * boost) + win / (prod + (n + 1) * boost):
            break
    return sum(cost / (prod + i * boost ) for i in range(n)) + win / (prod + n * boost)

T = read_int()
for case in range(T):
    C, F, X = map(float, raw_input().split())
    print "Case #{}: {:0.7f}".format(case + 1, best_time(C, F, X))
