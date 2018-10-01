#!/usr/bin/env python
# -*- coding: utf-8 -*-

cases = int(raw_input())
for case in range(cases):
    coords = int(raw_input())
    v1 = [int(x) for x in str(raw_input()).split(' ')]
    v2 = [int(x) for x in str(raw_input()).split(' ')]
    scalar = 0
    while v1:
        scalar += max(v1) * min(v2)
        v1.remove(max(v1))
        v2.remove(min(v2))
    print "Case #%d: %d" % ((case + 1), scalar)
