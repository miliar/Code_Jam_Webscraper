#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 jitesh <jitesh@getsuga>
#
# Distributed under terms of the MIT license.

"""

"""

import re

T = int(raw_input())
t = 1
while t <= T:
    n = int(raw_input())
    a = raw_input()
    b = raw_input()
    ai = 0
    bi = 0
    moves = 0
    success = None

    while (ai < len(a)) and (bi < len(b)):
        if a[ai] == b[bi]:
            ai += 1
            bi += 1
            continue
        if ai > 0 and (a[ai] == a[ai-1]):
            a = a[:ai] + a[ai+1:]
            moves += 1
            continue
        if bi > 0 and (b[bi] == b[bi-1]):
            b = b[:bi] + b[bi+1:]
            moves += 1
            continue
        success = False
        break

    if success is False:
        pass
    elif ai < len(a):
        if re.match('^{}+$'.format(a[ai-1]), a[ai:]):
            moves += len(a) - ai
        else:
            success = False
    elif bi < len(b):
        if re.match('^{}+$'.format(b[bi-1]), b[bi:]):
            moves += len(b) - bi
        else:
            success = False
    else:
        success = True

    if success is False:
        print "Case #{0}: Fegla Won".format(t)
    else:
        print "Case #{0}: {1}".format(t, moves)
    t += 1
