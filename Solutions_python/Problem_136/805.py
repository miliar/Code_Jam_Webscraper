#!/usr/bin/env python
#from decimal import *


def times(N):
    build_cost = float(0)
    for i in range(N):
        speed = float(2) + boost * i
        curr = build_cost + target / speed
        if curr > minima:
            break
        yield curr
        build_cost += cost / speed

fin = open('b-small.in')
TEST_COUNT = int(fin.readline())
# print TEST_COUNT

fout = open('b.out', 'w')
for test in range(TEST_COUNT):
    [cost, boost, target] = map(float, fin.readline().strip().split(' '))
    #print cost, boost, target
    minima = target
    max_factories = int(target / cost) + 3
    verdict = min(times(max_factories))

    answer = 'Case #%d: %.12f' % (test + 1, verdict)
    print answer
    fout.write(answer + '\n')

fout.close()
