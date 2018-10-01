#!/usr/bin/python
"Google Qualification - B"

import re

T = int(raw_input())

for case in range(1, T + 1):
    line = raw_input().split()
    H = range(1, int(line.pop(0)) + 1)
    W = range(1, int(line.pop(0)) + 1)
    m = {}
    for r in H:
        m[r] = {}
        line = raw_input().split()
        for c in W:
            height = int(line.pop(0))
            m[r][c] = height

    d = {}
    for r in H:
        d[r] = {}
        for c in W:
            d[r][c] = (r, c)
    finished = False
    while not finished:
        finished = True
        for r in H:
            for c in W:
                heights = [(m[r2][c2], o, r2, c2)
                           for (o, r2, c2) in [(1, r - 1, c),
                                               (2, r, c - 1),
                                               (3, r, c + 1),
                                               (4, r + 1, c)] # N, W, E, S
                           if (r2 in H) and (c2 in W)]
                heights.sort()

                if heights:
                    #print r, c, heights

                    (z, o, r2, c2) = heights[0]
                    if m[r2][c2] < m[r][c]:
                        #print r, c, 'flows to', r2, c2
                        if d[r2][c2] != d[r][c]:
                            d[r][c] = d[r2][c2]
                            finished = False
                    #else:
                    #    print r, c, 'is a sink'

    alpha = list('abcdefghijklmnopqrstuvwxyz')
    seen = {}

    print 'Case #%d:' % case
    #print repr(d)
    for r in H:
        row = ''
        for c in W:
            v = d[r][c]
            if v not in seen:
                seen[v] = alpha.pop(0)
            row += ('%s ' % seen[v])
        print row.strip()

