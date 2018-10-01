#!/usr/bin/env python3
import sys
from itertools import zip_longest
import numpy as np
import math
from numba import jit
from concurrent.futures import ProcessPoolExecutor


def min_time(plates):
    min_time = plates[0]['P']
    max_cuts = min_time

    for cuts in range(1, max_cuts+1):
        plate = max(plates, key=lambda x: math.ceil(x['P']/(x['cuts'] + 1)))

        plate['cuts'] += 1

        time = max(math.ceil(x['P']/(x['cuts'] + 1)) for x in plates) + cuts
        if time <= min_time:
            min_time = time

    return min_time


with open(sys.argv[1]) as f:
    next(f)  # skip T

    cases = []
    for i, (line1, line2) in enumerate(zip_longest(*[f]*2), 1):
        cases.append((line1, line2))

    with ProcessPoolExecutor() as executor:
        for i, ans in enumerate(executor.map(min_time, cases), ):

        D = int(line1)
        plates = np.array([(int(p), 0) for p in line2.strip().split()],
                          dtype=[('P', int), ('cuts', int)])
        plates.sort(order='P')
        plates = plates[::-1]

        ans = min_time(plates)
        print("Case #{i}: {ans}".format(i=i, ans=ans))
