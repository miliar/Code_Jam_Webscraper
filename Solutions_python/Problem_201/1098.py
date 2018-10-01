#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem C. Bathroom Stalls
# https://code.google.com/codejam/contest/dashboard?c=3264486#s=p2
#

import sys
import random


def solve(N, K):
    l = r = 0
    stock = {N: 1}
    while K > 0:
        N = sorted(stock.keys())[-1]
        count = stock.pop(N)
        K -= count
        left = int(N / 2)
        right = (N - 1) - left
        stock[left] = stock.get(left, 0) + count
        stock[right] = stock.get(right, 0) + count
    return '{} {}'.format(max(left, right), min(left, right))


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        N, K = map(int, IN.readline().split())
        OUT.write('Case #{}: {}\n'.format(index + 1, solve(N, K)))


def makesample(T=100, Nmax=10 ** 18):
    print(T)
    for index in range(T):
        N = random.randint(1, Nmax)
        K = random.randint(1, N)
        print('{} {}'.format(N, K))


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)
