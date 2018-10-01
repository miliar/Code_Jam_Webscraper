#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(D, N, horses):
    maxt = 0
    for i in range(N):
        k, s = horses[i]
        d = D - k;
        t = d / s;
        if t > maxt:
            maxt = t

    return "{:.6f}".format(D/maxt)

if __name__ == "__main__":
    test_cases = input()

    for i in xrange(1, test_cases+1):
        horses = []
        D, N = raw_input().split(" ")

        for j in range(int(N)):
            k, s = raw_input().split(" ")
            horses.append((float(k), int(s)))

        print "Case #{}: {}".format(i, solve(float(D), int(N), horses))
