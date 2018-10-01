#!/usr/bin/env python

from sys import stdin

COOKIE_RATE = 2

cases = int(stdin.readline())

for i in range(1, cases + 1):
    (farm_cost, extra_rate, winning) = stdin.readline().split()

    farm_cost = float(farm_cost)
    extra_rate = float(extra_rate)
    winning = float(winning)

    min_time = winning / COOKIE_RATE
    last_time = 0
    last_rate = COOKIE_RATE

    while (1):
        last_time += farm_cost / last_rate
        last_rate += extra_rate
        new_time = last_time + winning / last_rate
        if new_time > min_time:
            break
        min_time = new_time

    print("Case #" + str(i) + ": %.7f" % min_time)
