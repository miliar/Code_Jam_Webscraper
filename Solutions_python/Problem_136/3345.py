#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10000)

class Solver(object):
    def __init__(self, C, F, X):
        self.cost = C
        self.rate_increase = F
        self.goal = X

    def wait(self, cookies = 0, rate = 2.0, elapsed = 0, prior = float('inf')):
        # at each rate, two values are meaningful
        # 1. How long would it take to reach the goal at this rate
        # 2. How much time will elapse before we can increase the rate.
        at_rate = (self.goal / rate) + elapsed
        if prior < at_rate:
            return prior
        to_increase = self.cost / rate
        return min(at_rate, self.wait(0, rate + self.rate_increase, to_increase + elapsed, at_rate))


if __name__ == '__main__':
    with open('b-small-in') as fhi, open('b-small-out', 'w') as fho:
        cases = int(fhi.readline(), 10)
        for case in range(1, cases + 1):
            C, F, X = map(float, fhi.readline().split())
            fho.write('Case #%d: %0.7f\n' % (case, Solver(C, F, X).wait()))
