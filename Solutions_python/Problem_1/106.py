#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from itertools import izip, repeat

cases  = int(sys.stdin.readline())

for case in xrange(cases):
    ecount = int(sys.stdin.readline())

    switches = 0
    engines  = [sys.stdin.readline().strip() for i in xrange(ecount)]

    queries  = int(sys.stdin.readline())

    possible = dict(izip(engines, repeat(None)))
    for i in xrange(queries):
        eng = sys.stdin.readline().strip()
        if eng not in possible:
            continue
        else:
            del possible[eng]
            if len(possible) == 0:
                switches += 1
                possible = dict(izip(engines, repeat(None)))
                del possible[eng]

    print "Case #%d: %d" % (case+1, switches)
