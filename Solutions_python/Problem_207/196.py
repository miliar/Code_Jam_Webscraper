# coding: utf-8

import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect


def array2d(d1, d2, init=None):
    return [[init for _ in range(d2)] for _ in range(d1)]


def solve_small():
    # for small
    N, R, O, Y, G, B, V = map(int, input().split(" "))

    colors_orig = {"R": R, "Y": Y, "B": B}
    colors = []
    for k, v in sorted(colors_orig.items(), key=lambda x: -x[1]):
        colors.append({"name": k, "n": v})
    if colors[0]["n"] > colors[1]["n"] + colors[2]["n"]:
        return "IMPOSSIBLE"
    arr = ""
    for i in range(colors[0]["n"]):
        arr += colors[0]["name"]
        if i < colors[1]["n"]:
            arr += colors[1]["name"]
        if i >= colors[0]["n"] - colors[2]["n"]:
            arr += colors[2]["name"]
    return arr


def main():
    n_cases = int(input())
    for i in range(n_cases):
        print("Case #{}: {}".format(i + 1, solve_small()))


if __name__ == "__main__":
    main()
