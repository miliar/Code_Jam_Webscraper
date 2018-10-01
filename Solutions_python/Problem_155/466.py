#!/usr/bin/env python

from __future__ import division, print_function

import fileinput

import numpy as np


def minimum_friends(audience):
    minimum_audience = 1 + np.arange(len(audience))
    return max(0, np.max(minimum_audience - np.cumsum(audience)))


if __name__ == '__main__':
    for i, line in enumerate(fileinput.input()):
        if i == 0:
            continue
        _, audience = line.strip().split()
        audience = map(int, audience)
        print("Case #{}: {}".format(i, minimum_friends(audience)))
