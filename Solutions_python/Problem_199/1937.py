# coding=utf-8

# Created on 08/04/2017
# Code Jam 2017 qr a
# @author: manolo

import sys

ifile = sys.stdin
ofile = sys.stdout

IMPOSSIBLE = 'IMPOSSIBLE'


def r():
    return ifile.readline()[:-1]


def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))


def find_first_unhappy_i(pancakes):
    i = 0
    while i < len(pancakes) and pancakes[i] == '+':
        i += 1

    return i


def flip_pancake(pancake):
    return '+' if pancake == '-' else '-'


def flip_pancakes(first_unhappy_i, pancakes, flipper):
    for i in range(flipper):
        pancakes[first_unhappy_i + i] = flip_pancake(pancakes[first_unhappy_i + i])


def solve(flips, pancakes, flipper):

    # print '\n--------------------------'
    # print 'pancakes: {}'.format(pancakes)

    while True:
        if len(pancakes) == 0:
            # print 'done after {} flips (no more pancakes to flip)'.format(flips)
            return flips

        first_unhappy_i = find_first_unhappy_i(pancakes)
        if first_unhappy_i == len(pancakes):
            # print 'done after {} flips (no more unhappy pancakes)'.format(flips)
            return flips

        # print 'first unhappy pancake: [{}]'.format(first_unhappy_i)

        if len(pancakes[first_unhappy_i:]) < flipper:
            # print 'it\'s impossible, there are {} pancakes left ({}) and we have to flip always {} together'.format(
            #     len(pancakes[first_unhappy_i:]), pancakes[first_unhappy_i:], flipper)
            return IMPOSSIBLE

        flip_pancakes(first_unhappy_i, pancakes, flipper)
        # print 'flipped the next {} pancakes: {}'.format(flipper, pancakes)

        #solve(flips + 1, pancakes[first_unhappy_i+1:], flipper)
        flips += 1
        pancakes = pancakes[first_unhappy_i+1:]

    return flips

T = int(r())
for case in range(1, T+1):
    pancakes, flipper = r().split(' ')

    pancakes = list(pancakes)
    flipper = int(flipper)

    if flipper > len(pancakes):
        what = IMPOSSIBLE
    else:
        what = solve(0, pancakes, flipper)

    w(case, what)