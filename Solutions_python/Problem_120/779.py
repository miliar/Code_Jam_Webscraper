#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

def calc_area(lower):
    return (lower ** 2 - (lower - 1) ** 2)

def f(r, t):
    tot = 0
    while True:
        lol = calc_area(r + 1)
        if lol > t:
            return tot
        tot += 1
        t -= lol
        r += 2

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        r, t = map(int, input().split())
        ret = f(r, t)
        print('Case #{}: {}'.format(i+1, ret))
