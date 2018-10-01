import numpy as np
from collections import deque
import bisect
import copy

test_cases = int(raw_input().strip())


def d_war(naomi_blocks, ken_blocks):
    c = 0
    while (naomi_blocks):
        if ken_blocks[-1] > naomi_blocks[-1]:
            ken_blocks.pop()
            naomi_blocks.pop(0)
        else:
            for spent in naomi_blocks:
                if spent > ken_blocks[0]:
                    c += 1
                    del spent
                    ken_blocks.pop(0)
            break
    return c


def war_answer(naomi_blocks, ken_blocks):
    c = 0
    while naomi_blocks and ken_blocks:
        naomi_greater = naomi_blocks.pop()
        if naomi_greater > ken_blocks[-1]:
            ken_blocks.popleft()
            c += 1
        else:
            # ken won
            value = ken_blocks[bisect.bisect_left(ken_blocks, naomi_greater)]
            ken_blocks.remove(value)
    return c


for test_case in xrange(test_cases):
    n_wood = int(raw_input().strip())
    naomi_blocks = sorted(map(float, raw_input().strip().split()))
    ken_blocks = sorted(map(float, raw_input().strip().split()))

    deceit = d_war(list(naomi_blocks), list(ken_blocks))
    war = war_answer(deque(naomi_blocks), deque(ken_blocks))

    print "Case #%d: %d %d" % (test_case + 1, deceit, war)

