#!/usr/bin/env python
# -*- Encoding: utf-8 -*-

from __future__ import print_function, unicode_literals

import heapq
from collections import defaultdict, deque


def expand(grid, t, l, b, r, ch):
    could = False

    # try left
    if l > 0:
        can = True
        for rw in range(t, b + 1):
            if grid[rw][l - 1] not in ("?", ch):
                can = False
                break

        if can:
            could = True
            for rw in range(t, b + 1):
                grid[rw][l - 1] = ch
            l -= 1

    # try right
    if r < len(grid[0]) - 1:
        can = True
        for rw in range(t, b + 1):
            if grid[rw][r + 1] not in ("?", ch):
                can = False
                break

        if can:
            could = True
            for rw in range(t, b + 1):
                grid[rw][r + 1] = ch
            r += 1

    # try bottom
    if b < len(grid) - 1:
        can = True
        for cl in range(l, r + 1):
            if grid[b + 1][cl] not in ("?", ch):
                can = False
                break

        if can:
            could = True
            for cl in range(l, r + 1):
                grid[b + 1][cl] = ch
            b += 1

    # try top
    if t > 0:
        can = True
        for cl in range(l, r + 1):
            if grid[t - 1][cl] not in ("?", ch):
                can = False
                break

        if can:
            could = True
            for cl in range(l, r + 1):
                grid[t - 1][cl] = ch
            t -= 1

    return t, l, b, r, could


def solve(R, C, grid):
    s = set()
    topleft = defaultdict(int)
    bottomright = defaultdict(int)
    for r in range(R):
        row = grid[r]
        for c in range(C):
            ch = row[c]
            if ch != "?":
                s.add(ch)
                if ch not in topleft:
                    topleft[ch] = (r, c)
                bottomright[ch] = (r, c)

    for ch in s:
        if topleft[ch] != bottomright[ch]:
            t, l = topleft[ch]
            b, r = bottomright[ch]
            if l > r:
                l, r = r, l
            for rw in range(t, b + 1):
                for cl in range(l, r + 1):
                    assert grid[rw][cl] in ("?", ch), "grid[{}][{}] = {}".format(rw, cl, grid[rw][cl])
                    grid[rw][cl] = ch

    for ch in s:
        t, l = topleft[ch]
        b, r = bottomright[ch]
        if l > r:
            l, r = r, l
        could = True
        while could:
            t, l, b, r, could = expand(grid, t, l, b, r, ch)

    return grid

if __name__ == '__main__':
    T = int(raw_input())
    for Ti in range(T):
        R, C = map(int, raw_input().strip().split(" "))
        grid = []
        for Ri in range(R):
            grid.append([c for c in raw_input().strip()])
        ans = solve(R, C, grid)
        print("Case #{}:".format(Ti + 1))
        for row in ans:
            print("".join(row))
