#!/usr/bin/env python3

import sys
import math


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('Usage: {0} IN_FILE [OUT_FILE]'.format(sys.argv[0]))
        return

    in_file = open(sys.argv[1])
    out_file = open(sys.argv[1]+'.txt' if len(sys.argv) == 2 else sys.argv[2], mode='w')
    cases = int(next(in_file))
    for c in range(cases):
        l, h = [int(x) for x in next(in_file).rstrip('\n').split(' ')]
        counter = 0
        for i in range(l, h+1):
            if is_fair_and_square(i):
                counter += 1
        out_file.write('Case #{0}: {1}\n'.format(c+1, counter))


def is_fair_and_square(num):
    if math.sqrt(num) % 1 > 0:
        return False
    return is_palindrome(num) and is_palindrome(math.sqrt(num))


def is_palindrome(num):
    digit_list = []
    while num > 0:
        digit_list.append(num % 10)
        num //= 10
    return digit_list == digit_list[::-1]


if __name__ == '__main__':
    main()
