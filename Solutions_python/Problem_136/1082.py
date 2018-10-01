#!/usr/bin/env python

import sys

case = int(sys.stdin.readline())

for i in range(case):
    row = sys.stdin.readline()
    c, f, x = (float(f) for f in row.split(' '))
    t = x / 2.0
    answer = c / 2.0
    j = 0

    while True:
        if j > 0:
            answer += c/(j*f + 2.0)
        this_answer = answer + x/((j+1)*f+2.0)

        if this_answer < t:
            t = this_answer
            j += 1
        else:
            break

    print('Case #%d: %.7f' % (i+1, t))
