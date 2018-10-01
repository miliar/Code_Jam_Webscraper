#!/usr/bin/python
"""
Google Code Jam
1) Ample Syrup
"""

import fileinput
import math
import itertools


def exposed_area(p, hidden=None):
    radius, height = p
    top = math.pi * math.pow(radius, 2)
    sides = 2 * math.pi * radius * height
    cover = 0
    if hidden:
        cover = math.pi * math.pow(hidden, 2)
    return top + sides - cover

def get_result(N, K, pancakes):
    exposed = exposed_area(pancakes[-1])
    for i, p in enumerate(pancakes[:-1]):
        exposed += exposed_area(p, pancakes[i+1][0])
    return exposed


def testcase(N, K, P):
    pancakes = sorted(P)[::-1]
    exposed = [get_result(N, K, kovern) for kovern in itertools.combinations(pancakes, K)]
    return max(exposed)


def main():
    f = fileinput.input()
    T = int(f.readline().strip())
    for t in xrange(1, T+1):
        N, K = map(int, f.readline().strip().split())
        P = [map(int, f.readline().strip().split()) for n in xrange(N)]
        print 'Case #{}: {:.9f}'.format(t, testcase(N, K, P))


if __name__ == '__main__':
    main()
