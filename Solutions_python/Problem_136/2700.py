# -*- coding: utf-8 -*-

import sys


def solve():
    def get_one_more_farm_cost(t, rate):
        new_t = t + C / rate
        new_rate = rate + F
        cost = new_t + X / new_rate
        return cost, new_t, new_rate

    (C, F, X) = list(map(float, input().split()))
    current_cost = X / 2
    t = 0
    rate = 2

    while True:
        next_cost, t, rate = get_one_more_farm_cost(t, rate)
        if next_cost >= current_cost:
            break
        current_cost = next_cost
    return current_cost

def main():
    T = int(input())
    for i in range(T):
        print('Case #{}: {}'.format(i + 1, solve()))

if __name__ == '__main__':
    sys.exit(main())
