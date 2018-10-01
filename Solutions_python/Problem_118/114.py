#!/usr/bin/env python
import sys

from itertools import *

def palindromes():
    # conjecture: you don't need all palindromes
    yield 1
    yield 2
    yield 3
    for digits in count(1):
        x = ['1'+''.join(_) for _ in product('01', repeat=digits-1) if _.count('1') <= 3]
        x.append('2' + '0'*(digits-1))
        print >> sys.stderr, digits, len(x)
        for n in x:
            yield int(n + n[::-1])
        for n in x:
            for middle in '012':
                yield int(n + middle + n[::-1])

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

def find(upper_bound):
    # Loop through palindromic numbers and check that their squares are palindromes.
    result = []
    for n in palindromes():
        square = n**2
        if square > upper_bound:
            break
        if is_palindrome(square):
            result.append(square)
    return result

def solve(A, B, fair_squares):
    count = 0
    for x in fair_squares:
        if x > B:
            break
        if x >= A:
            count += 1
    return count

if __name__ == '__main__':
    fair_squares = find(10**100)

    with open(sys.argv[1], 'rU') as fin, open(sys.argv[2], 'w') as fout:
        T = int(fin.readline())
        for case in xrange(1, T+1):

            A, B = map(int,fin.readline().split())
            soln = solve(A, B, fair_squares)

            print >> fout, "Case #{0}: {1}".format(case, soln)
