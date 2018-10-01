#!/usr/bin/python

import sys
from collections import defaultdict

def add_sym(output, sym, opposites):
    if sym in opposites and opposites[sym].intersection(output):
        output = []
    else:
        output.append(sym)
    return output

def solve(transforms, opposites, series):
    output = []
    for sym in series:
        output.append(sym)
        while tuple(output[-2:]) in transforms:
            trans = transforms[tuple(output[-2:])]
            output.pop()
            output.pop()
            output.append(trans)
        if output and output[-1] in opposites and opposites[output[-1]].intersection(output[:-1]):
            output = []
    return output

def main():
    lines = iter(sys.stdin)
    T = int(next(lines))
    for i, line in enumerate(lines):
        transforms = {}
        opposites = defaultdict(set)

        items = line.split()

        C = int(items.pop(0))
        for tr in items[:C]:
            a, b, t = list(tr)
            transforms[(a,b)] = t
            transforms[(b,a)] = t
        del items[:C]

        D = int(items.pop(0))
        for opp in items[:D]:
            a, b = list(opp)
            a, b = list(opp)
            opposites[a].add(b)
            opposites[b].add(a)
        del items[:D]

        N = int(items.pop(0))
        series = list(items.pop(0))

        output = solve(transforms, opposites, series)
        print "Case #%s: [%s]" % (i+1, ", ".join(output))

main()
