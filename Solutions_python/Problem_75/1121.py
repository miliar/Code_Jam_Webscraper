#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys

def solve(cmb, repulsives, elements):
    res = []
    while len(elements):
        el = elements.pop(0)
        while len(res) and (res[-1] + el) in cmb:
            el = cmb[res.pop() + el]
        idx = len(res) - 1
        while idx >= 0:
            if repulsives.get(res[idx]) == el:
                break
            idx -= 1
        if idx >= 0:
            res = []
        else:
            res.append(el)
    return '[' + ', '.join(res) + ']'

f = open(sys.argv[1])
with f:
    nbcases = int(f.readline())
    for case in xrange(nbcases):
        l = f.readline().split()
        repulsives = []
        combinations = {}
        for cmb in (l.pop(0) for _ in xrange(int(l.pop(0)))):
            combinations[cmb[0:2]] = cmb[-1]
            combinations[cmb[1] + cmb[0]] = cmb[-1]
        repulsives = {}
        for rep in (l.pop(0) for _ in xrange(int(l.pop(0)))):
            repulsives[rep[0]] = rep[1]
            repulsives[rep[1]] = rep[0]
        elements = [k for k in l[-1]]
        #print combinations, repulsives, elements
        print 'Case #' + str(case + 1) + ':', solve(combinations, repulsives, elements)
