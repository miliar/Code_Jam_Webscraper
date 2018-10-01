#!/usr/bin/env python

import sys
from collections import Counter
from math import floor, log

def bits_required(n):
    return floor(log(n, 2)) + 1

def numbers_less_than_n_with_bit_j_on(n, j):
    return n // (2**j) + n % 2

def do_case(f):
    A, B, K = map(int, f.readline().rstrip().split())
    P = A * B
    a = A - 1
    b = B - 1
    count = 0
    for i in xrange(A):
        for j in xrange(B):
            if i & j in range(K):
                count+=1
    return count
def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    for t in xrange(1,T+1):
        print 'Case #{}: {}'.format(t, do_case(f))
    f.close()

if __name__ == '__main__':
    # count = 0
    # for i in xrange(1000):
    #     for j in xrange(1000):
    #         if i & j in xrange(99):
    #             count += 1
    # print count
    main() 