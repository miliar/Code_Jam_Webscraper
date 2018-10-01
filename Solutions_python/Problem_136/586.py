#!/usr/bin/env python

import math
import sys

def solve_game_smarter(c, f, x):
    n = int(math.floor((x * f / c - 2) / f))
    if n < 0:
        n = 0
    time_to_get_farms = 0
    c_per_s = 2
    for _ in range(n):
        time_to_get_farms += c / c_per_s
        c_per_s += f
    return x / (n * f + 2) + time_to_get_farms

def solve_game(c, f, x):
    time = 0
    cookies = 0
    cookies_per_s = 2
    farm_break_even_time = c / f
    while True:
        if x - cookies <= c:
            return time + (x - cookies) / cookies_per_s
        elif cookies < c:
            time_this_round = (c - cookies) / cookies_per_s
            time += time_this_round
            cookies += time_this_round * cookies_per_s
            continue
        elif (x - cookies) / cookies_per_s <= farm_break_even_time:
            return time + (x - cookies) / cookies_per_s
        else:
            cookies -= c
            cookies_per_s += f

if __name__ == "__main__":
    games = []
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            games.append([float(i) for i in f.readline().strip().split()])

    seconds = []
    for g in games:
        seconds.append(solve_game_smarter(*g))

    for i, s in enumerate(seconds, start=1):
        print("Case #%d: %.7f" % (i, s))
