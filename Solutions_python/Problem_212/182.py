#!/usr/bin/env python
# encoding: utf-8

T = int(raw_input())

for t in xrange(1, T + 1):
    n, p = map(int, raw_input().split())
    a = map(int, raw_input())

    b = [0] * 5
    for i in xrange(1, n):
        b[a[i - 1] % p] += 1

    ans = 0
    if p == 2:
        ans = b[0] + (b[1] + 1) / 2
    elif p == 3:
        ans = b[0]
        if b[1] > b[2]:
            b[1], b[2] = b[2], b[1]
        ans += b[1]
        b[2] -= b[1]
        ans += b[2] / 3
        if b[2] % 3 > 0:
            ans += 1
    elif p == 4:
        ans = b[0]
        if b[1] > b[3]:
            b[1], b[3] = b[3], b[1]
            ans += b[1]
            b[3] -= b[1]
            tmp = 0
            for i in xrange(n + 1):
                if i * 4 > b[3]:
                    break
                res = i
                t3 = b[3] - i * 4
                t2 = b[2]
                if t3 / 2 > t2:
                    res += t2
                    t3 -= 2 * t2
                    res += t3 / 4
                    t3 %= 4
                    if t3 > 0:
                        res += 1
        else:
            res += t3 / 2

            t2 -= t3 / 2
            t3 %= 2
            res += t2 / 2
            t2 %= 2
            if t2 or t3:
                res += 1
        if res > tmp:
            tmp = res
    ans += tmp

print "Case #" + str(t) + ": " + str(ans)
