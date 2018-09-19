#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools


def int2digits(number):
    while True:
        yield number % 10
        number /= 10
        if not number:
            break
    raise StopIteration


def get_pairs(number):
    number = [_ for _ in int2digits(number)]
    if min(number) == max(number):
        raise StopIteration
    number.reverse()
    for _ in xrange(len(number) - 1):
        number.insert(0, number.pop())
        yield reduce(lambda base, digit: base * 10 + digit, number)
    raise StopIteration


if __name__ == '__main__':
    count = int(raw_input())

    for index in xrange(count):
        A, B = map(int, raw_input().split())

        numbers = set()
    
        for a in range(A, B):
            pairs = [b for b in get_pairs(a) if (a < b <= B)]
            for b in pairs:
                numbers.add((a, b))
    
        print 'Case #%d: %d' % (index + 1, len(numbers))
    
    sys.exit()
