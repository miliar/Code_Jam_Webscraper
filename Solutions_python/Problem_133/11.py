#!/usr/bin/python3

from common import *

def testcase(x):
    b, n = readintegers()

    xs = readintegers()

    val = [0] * 37
    for i in range(n):
        val[i] = xs[i]

    val.sort()
    # print (x, val)

    n = 37

    best = 0
    for k1 in range(1, n - 1):
        for k2 in range(k1, n):
            if k2 < n and val[k2 - 1] == val[k2]:
                continue

            cost1 = 0
            for j in range(k1):
                cost1 += val[k2 - 1] - val[j]

            cost2 = 0
            for j in range(k1, k2):
                cost2 += 1 + val[k2 - 1] - val[j]

            if cost1 + cost2 > b:
                continue

            q = (b - cost1 - cost2) // k2
            if k2 < n and val[k2 - 1] + q >= val[k2]:
                q = val[k2] - val[k2 - 1] - 1

            if k2 > n - 1:
                q = 0

            ev = ((cost1 + q * k1) * (n - 1) / k1) - (cost1 + cost2 + q * k2)

            if ev > best:
                best = ev

    writeline("Case #{:d}: {:.9f}".format(x, best))

run_tests(testcase)
