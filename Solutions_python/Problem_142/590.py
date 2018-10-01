#!/usr/bin/env python3

import collections
from itertools import groupby

num_cases = int(input())

def runlengths(input):
    return [(len(list(g)), k) for k,g in groupby(input)]


for case in range(1, num_cases+1):
    N = int(input())
    run_lengths = [runlengths(input()) for _ in range(N)]

    result = 0
    if len(run_lengths[0]) != len(run_lengths[1]):
        result = "Fegla Won"
    else:
        for idx, rl in enumerate(run_lengths[0]):
            if rl[1] != run_lengths[1][idx][1]:
                result = "Fegla Won"
                break
            result += abs(rl[0] - run_lengths[1][idx][0])


    print("Case #{}: {}".format(case, result))
    
