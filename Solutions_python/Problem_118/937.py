# Fair and Square
# https://code.google.com/codejam/contest/2270488/dashboard#s=p2

# PYTHON 3

import sys
import math

sys.stdin = open('c.in', 'r')
sys.stdout = open('c.out', 'w')


def fair_and_square_numbers(a, b):
    """ returns a list of fair and square numbers in a range """
    results = []
    sqrt_a = int(math.ceil(math.sqrt(a)))
    sqrt_b = int(math.sqrt(b))
    for i in range(sqrt_a, sqrt_b + 1):
        str_i = str(i)
        # check if this number is a palindrome, a palindrome cannot start
        # with a zero so numbers ending in 0 are omitted
        if not str_i[-1] == '0' and str_i == str_i[::-1]:
            sqr_i = i ** 2
            str_sqr_i = str(sqr_i)
            if str_sqr_i == str_sqr_i[::-1]:
                results.append(sqr_i)
    return results

t = int(input())

# these are possible bounds given in the first large test case
min_range = 1
max_range = 10 ** 14

palins = fair_and_square_numbers(min_range, max_range)

for T in range(1, t + 1):
    c = 0  # result count
    a, b = [int(x) for x in input().split()]
    for p in palins:
        if a <= p <= b:
            c += 1
    print("Case #%d: %d" % (T, c))
