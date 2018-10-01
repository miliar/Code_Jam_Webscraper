#!/usr/bin/env python3
# coding=utf-8

"""
  Solution to Qualification Round.A

  Author: killerrex@gmail.com
"""

import sys
import itertools


def parse_input(txt):
    """
    Read a line and return an array of numbers

    Format: Smax  <0 to Smax>

    :param txt:
    :return:
    """
    sm, levels = txt.split()
    sm = int(sm)
    assert(len(levels) == sm + 1)

    levels = [int(c) for c in levels]

    return levels


def ovation(scene):
    """
    Solve a scene for an ovation
    :param scene: list of shyness public
    :return: number of friends
    """

    f = max(t + 1 - s for t, s in enumerate(itertools.accumulate(scene)))
    return max(f, 0)


def solve(fd):
    """
    Process an input and write the correct output...
    """

    cases = int(fd.readline().strip())

    for k in range(cases):
        txt = fd.readline().strip()
        if not txt:
            continue
        scene = parse_input(txt)
        f = ovation(scene)
        print("Case #{}: {}".format(k+1, f))


if __name__ == '__main__':

    # Read stdin and write stdout
    solve(sys.stdin)
