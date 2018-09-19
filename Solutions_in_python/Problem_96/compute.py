#!/usr/bin/env python

import sys

cnt = int(sys.stdin.readline())

for i in range(cnt):
    N, S, p, scores = sys.stdin.readline().strip().split(' ', 3)
    scores = map(int, scores.split(' '))
    N = int(N)
    S = int(S)
    p = int(p)

    result = 0
    result_surprise = 0
    for score in scores:
        vote = score / 3
        vote += score % 3 > 0
        if vote >= p:
            result += 1
            continue
        else:
            if vote + (score % 3 in [0, 2]) >= p and vote > 0:
                result_surprise += 1

    
    print "Case #%d: %d" % (i + 1, min(S, result_surprise) + result)
