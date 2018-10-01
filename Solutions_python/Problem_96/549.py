# -*- coding: utf-8 -*-

from __future__ import print_function

import math


def count(_n, suprising, p, *scores):
    count = 0

    for score in scores:
        if not score:
            count += p == 0
        elif score >= 3 * p - 2:
            count += 1
        elif suprising and score >= 3 * p - 4:
            count += 1
            suprising -= 1

    return count


if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(1, t + 1):
        data = map(int, raw_input().split())
        print("Case #{0}: {1}".format(i, count(*data)))
