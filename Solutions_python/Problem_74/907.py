#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import sys

DEBUG = False

def print_world(clock, pos_orange, pos_blue):
    if not DEBUG:
        return
    print(clock)
    print('+--+-+-+')
    for i in range(10):
        print('|{0:2}|{1}|{2}|'.format(i, 'O' if i == pos_orange else ' ', 'B' if i == pos_blue else ' '))
    print('+--+-+-+')

def seconds(orders):
    clock = 0
    pos_orange = 1
    pos_blue = 1
    last_clock_orange = 0
    last_clock_blue = 0

    for color, position in orders:
        if color == 'O':
            distance = abs(position - pos_orange)
            clock = max(last_clock_orange + distance + 1, clock + 1)
            last_clock_orange = clock
            pos_orange = position
        else:
            distance = abs(position - pos_blue)
            clock = max(last_clock_blue + distance + 1, clock + 1)
            last_clock_blue = clock
            pos_blue = position
        print_world(clock, pos_orange, pos_blue)
    return clock

def main(argv=None):
    if argv == None:
        argv = sys.argv

    if len(argv) <= 1:
        print('pass the input file name!')
        sys.exit(-1)

    input_file = open(argv[1], 'r')

    T = int(input_file.readline())
    for num_case in range(1, T + 1):
        elements = input_file.readline().split()
        num_orders = int(elements[0])
        raw_orders = elements[1:num_orders * 2 + 1]
        orders = ((raw_orders[i], int(raw_orders[i + 1]))
                  for i in range(0, len(raw_orders), 2))
        print('Case #{0}: {1}'.format(num_case, seconds(orders)))

if __name__ == '__main__':
    main()
