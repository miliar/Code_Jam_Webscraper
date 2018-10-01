# -*- coding: utf-8 -*-
# This library is available online and free to use:
# https://github.com/yanatan16/pycodejam
from codejam.parsers import iter_parser

# Input
#
# 5
# 1 9
# 1 10
# 3 40
# 1 1000000000000000000
# 10000000000000000 1000000000000000000
#
#
# Output
#
# Case #1: 1
# Case #2: 2
# Case #3: 3
# Case #4: 707106780
# Case #5: 49


def paint_ring(r):
    # R - r == 1
    # R + r == 2 * r + 1
    # pi * (R ** 2 - r ** 2) = pi * (R - r) * (R + r) = pi * (2 * r + 1)
    return 2 * r + 1


def solve(*lines):
    radius, milliliters = map(int, lines)
    # print radius, milliliters
    count_rings = 0
    while 1:
        milliliters -= paint_ring(radius)
        if milliliters < 0:
            break
        else:
            count_rings += 1
            radius += 2
    return count_rings


@iter_parser
def parse(nxtline):
    return nxtline().split()


if __name__ == "__main__":
    from codejam import CodeJam
    # import ipdb; ipdb.set_trace()
    CodeJam(parse, solve).main()
