#!/usr/bin/env python
def solve(line):
    x, r, c = (int(t) for t in line.split())
    if r * c % x != 0:
        return 'RICHARD'
    if x == 1 or x == 2:
        return 'GABRIEL'
    if x == 3:
        if r * c >= 6 and r >= 2 and c >= 2:
            return 'GABRIEL'
    if x == 4:
        if r * c >= 12 and r >= 3 and c >= 3:
            return 'GABRIEL'
    return 'RICHARD'

case_num = input()
for case in range(1, case_num + 1):
    line = raw_input()
    print("Case #%i: %s" % (case, solve(line)))

