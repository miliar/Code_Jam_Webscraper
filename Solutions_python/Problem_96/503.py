#!/usr/bin/env python3.2

import sys
import bisect

def readline():
    return next(sys.stdin).strip()

def readvals(t):
    return map(t, readline().split())

ncases = int(readline())
for caseno in range(ncases):
    n, s, p, *scores = readvals(int)
    if p == 0:
        print('Case #{}: {}'.format(caseno + 1, n))
        continue
    assert len(scores) == n
    scores.sort()
    not_surpr = n - bisect.bisect_left(scores, 3 * p - 2)
    surpr = n - bisect.bisect_left(scores, max(3 * p - 4, 1))
    print('Case #{}: {}'.format(caseno + 1,
                                not_surpr + min(surpr - not_surpr, s)))
    sys.stdout.flush()
