#!/usr/bin/env python
from __future__ import unicode_literals
import decimal
import fractions
import Queue
import sys
import threading

def compute_result(P, groups):
    # 1<=N<=100
    # small: 2<=P<=3, large: 2<=P<=4
    # first, any group sizes that are 0 mod P should go first. All of them are compatible.
    # what if you start with a certain number?

    """
    if P == 2, then all evens work, and then half (rounded down) the number of odd groups
    """
    arr = [0] * P
    for group in groups:
        arr[group % P] += 1
    if P == 2:
        total = arr[0]
        arr[0] = 0
        simple_combos = arr[1] / 2
        total += simple_combos
        arr[1] -= 2*simple_combos
        if (arr[1] > 0):
            total += 1
        return total
    elif P == 3:
        total = arr[0]
        simple_combos = min(arr[1], arr[2])
        total += simple_combos
        arr[1] -= simple_combos
        arr[2] -= simple_combos
        total += arr[1] / 3 + arr[2] / 3
        if (arr[1] % 3 != 0 or arr[2] % 3 != 0):
            total += 1
        return total
    elif P == 4:
        total = arr[0]
        
        # does it ever make sense not to combine?
        # can you ever make 8 or 12, but get hurt if you try to make a 4?
        # no, it should divide cleanly.

        # 1 3
        simple_combos = min(arr[1], arr[3])
        total += simple_combos
        arr[1] -= simple_combos
        arr[3] -= simple_combos
        # 2 2
        simple_combos = arr[2] / 2
        total += simple_combos
        arr[2] -= simple_combos * 2
        # 1 1 1 1
        simple_combos = arr[1] / 4
        total += simple_combos
        arr[1] -= simple_combos * 4
        # 3 3 3 3
        simple_combos = arr[3] / 4
        total += simple_combos
        arr[3] -= simple_combos * 4
        # 1 1 2
        # 2 3 3
        assert 0 <= arr[2] <= 1
        if arr[2] == 1:
            if arr[1] >= 2:
                total += 1
                arr[2] -= 1
                arr[1] -= 2
            elif arr[3] >= 2:
                total += 1
                arr[2] -= 1
                arr[3] -= 2
        if arr[1] > 0 or arr[2] > 0 or arr[3] > 0:
            total += 1
        return total

    return -1

def main(argv=sys.argv):
    infile = argv[1]
    outfile = argv[2]

    with open(infile) as fin, open(outfile, 'w') as fout:
        T = int(fin.readline().strip())
        
        for case in xrange(1, T+1):
            # read stuff
            N, P = map(int, fin.readline().strip().split())
            groups = map(int, fin.readline().strip().split())
            result = compute_result(P, groups)
            fout.write("Case #{}: {}\n".format(case, result))

    return 0

if __name__ == "__main__":
    status = main(argv=sys.argv)
    sys.exit(status)
