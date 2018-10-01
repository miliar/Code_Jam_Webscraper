#!/usr/bin/env python

import sys
from collections import deque
import bisect

case = int(sys.stdin.readline())

for c in range(case):
    b = int(sys.stdin.readline())
    naomi = deque(sorted([float(f) for f in sys.stdin.readline().split(' ')]))
    ken1 = sorted([float(f) for f in sys.stdin.readline().split(' ')])
    ken2 = list(ken1)
    mark_deceitful = 0
    mark_war = 0

    # War
    for i, naomi_block in enumerate(naomi):
        k = bisect.bisect(ken1, naomi_block)
        if k == b-i:
            mark_war += 1
            k = 0
        ken1.pop(k)

    # Deceitful
    for i in range(b):
        for j in range(b-i):
            if naomi[j] < ken2[j]:
                break
        else:
            # All naomi[i] > ken[i], get all remaining marks
            mark_deceitful = b-i
            break
        naomi.popleft()
        ken2.pop()

    print('Case #%d: %d %d' % (c+1, mark_deceitful, mark_war))
