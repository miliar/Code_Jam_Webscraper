#!/usr/bin/env python
import sys
import numpy as np


def min_friends(audience):
    standing = audience[0]
    friends = 0

    for shyness, n in enumerate(audience[1:], 1):
        if n > 0 and standing < shyness:
            new_friends = (shyness - standing)
            friends += new_friends
            standing += new_friends

        standing += n

    return friends


with open(sys.argv[1]) as inp:
    next(inp)  # skip T line

    for i, l in enumerate(inp, 1):
        s_max, audience = l.strip().split()
        audience = np.array([int(c) for c in audience])

        ans = min_friends(audience)
        print("Case #{i}: {ans}".format(i=i, ans=ans))
