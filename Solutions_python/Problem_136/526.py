__author__ = 'Daniel Rodgers-Pryor'

import functools
from itertools import izip, chain, repeat, combinations, permutations

#fname = 'test'
#fname = 'B-small-attempt0'
fname = 'B-large'

out_format = 'Case #%d: %.7f'

data = []
with open(fname + '.in') as fp:
    N = int(fp.readline())
    for case_input in fp:
        C, F, X = map(float, case_input.split())

        data.append((C, F, X))

assert len(data) == N


with open(fname + '.out', 'w') as fp:
    for i, case in enumerate(data):
        C, F, X = case

        # Initially:
        rate = 2.0
        total_build_time = 0.0  # Time spent building farms
        time_left = X/rate

        while True:
            build_time = C/rate  # Time to build a new farm (at the last rate)

            # If another farm is built:
            new_rate = rate + F
            new_total_build_time = total_build_time + build_time
            new_time_left = new_total_build_time + (X/new_rate)  # Time spent building farms + time spent earning X

            if new_time_left < time_left:  # Beneficial case
                rate = new_rate
                total_build_time = new_total_build_time
                time_left = new_time_left
            else:
                # If building a new farm isn't beneficial, then we're done
                break

        # Output
        out = out_format % (1 + i, time_left)
        print out
        fp.write(out + '\n')