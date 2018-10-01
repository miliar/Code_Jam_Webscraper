#!/usr/bin/python
# -*- coding:utf-8 -*-

# Let's be fair

import math
from itertools import count

def n_digits(n):
    return int(math.ceil(math.log(n + 1,10)))

def is_fair(n):
    if n_digits(n) == 1:
        return True

    digits = list(str(n))
    n = len(digits)
    head = digits[:n/2]
    tail = digits[-n/2+n%2:]
    tail.reverse()

    return head == tail

def fair_from_num(n, odd = 0, center = 0):
    d = n_digits(n)

    result = n * 10**(d + odd)
    result += center * 10**(d)
    rev = list(str(n))
    rev.reverse()
    rev = "".join(rev)
    result += int(rev)

    return int(result)

def generate_fair_numbers(start_length = 1):
    for length in count(start_length):
        if length == 1: # Generate from 0 to 9
            for i in range(0,10):
                yield i

        elif length % 2 == 1: # odd length
            i = int(10 ** (length/2 - 1))
            limit = 10 ** (length/2)
            while i < limit:
                for c in range(0,10):
                    yield fair_from_num(i, odd = 1, center = c)
                i+=1

        else: # even length
            i = int(10 ** (length/2 - 1))
            limit = 10 ** (length/2)
            while i < limit:
                yield fair_from_num(i)
                i+=1


def find(A, B):
    n = 0
    for i in generate_fair_numbers(n_digits(math.sqrt(A))):
        p = i * i
        if p < A:
            continue
        elif p > B:
            break
        elif is_fair(p):
            n+=1

    return n

if __name__ == "__main__":
#    import time
    import sys

    if len(sys.argv) < 2:
        input_file = "test_input.txt"
    else:
        input_file = sys.argv[1]

    f = open(input_file, "r")

    T = int(f.readline())

#    start = time.time()

    for i in range(1, T+1):
        A, B = f.readline().split(" ")
        print "Case #%d: %d" % (i, find(int(A),int(B)))

#    print "Tiempo:", time.time() - start
