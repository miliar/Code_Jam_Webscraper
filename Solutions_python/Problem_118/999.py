#!/usr/bin/python

import math
import os
import sys

fin = sys.stdin

msg_c = 'Case #%d: %s'

def is_pal(num):
    '''Return True if number is a palindrome'''
    s = str(num)
    for x in xrange(len(s) / 2):
        if s[x] != s[-x - 1]:
            return False
    return True

def squares(a, b):
    _a = int(math.ceil(math.sqrt(a)))
    _b = int(math.floor(math.sqrt(b)))
    i = _a
    s = i * i
    n = i * 2 + 1
    while i <= _b:
        yield [i, s]
        i += 1
        s += n
        n += 2

def solve(fin):
    count = 0
    A, B = map(int, fin.readline().strip().split())
    for n, s in squares(A, B):
        if is_pal(n) and is_pal(s):
            count += 1
    return str(count)

def main():
    T = int(fin.readline())
    for t in xrange(1, T + 1):
        print msg_c % (t, solve(fin))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fin = open(sys.argv[1], 'r')
    main()
