#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem B. Pogo
# https://code.google.com/codejam/contest/2437488/dashboard#s=p1
#

import sys


def solve(x, y):
    result = ''
    if x < 0:
        result += 'EW' * abs(x)
    else:
        result += 'WE' * x
    if y < 0:
        result += 'NS' * abs(y)
    else:
        result += 'SN' * y
    return result


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        X, Y = map(int, IN.readline().split())
        OUT.write('Case #%d: %s\n' % (index + 1, solve(X, Y)))


def makesample(XYmax=100, T=50):
    import random
    print T
    for index in range(T):
        X = Y = 0
        while X == 0 and Y == 0:
            X = random.randint(-XYmax, XYmax)
            Y = random.randint(-XYmax, XYmax)
        print X, Y


def check():
    import re
    for line in sys.stdin:
        m = re.search(r'Case #\d: ([NSEW]+)', line)
        if not m:
            break

        route = m.group(1)

        x = y = 0
        step = 1
        for d in route:
            xx, yy = {
                'N': (0, 1),
                'S': (0, -1),
                'E': (1, 0),
                'W': (-1, 0),
            }[d]
            x += xx * step
            y += yy * step
            step += 1
        print route, (x, y)


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    elif '-check' in sys.argv[1:]:
        check()
    else:
        main(sys.stdin, sys.stdout)

