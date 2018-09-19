'''
Qualification Round 2012

Problem C. Recycled Numbers

Small input
10 points

Large input
15 points

Do you ever become frustrated with television because you
keep seeing the same things, recycled over and over again?
Well I personally don't care about television, but I do
sometimes feel that way about numbers.

Let's say a pair of distinct positive integers (n, m) is
recycled if you can obtain m by moving some digits from the
back of n to the front without changing their order. For
example, (12345, 34512) is a recycled pair since you can
obtain 34512 by moving 345 from the end of 12345 to the
front. Note that n and m must have the same number of
digits in order to be a recycled pair.

Given integers A and B with the same number of digits, how
many distinct recycled pairs (n, m) are there with
A <= n < m <= B?

Input

The first line of the input gives the number of test cases,
T. T test cases follow. Each test case consists of a single
line containing the integers A and B.

Output

For each test case, output one line containing "Case #x: y",
where x is the case number (starting from 1), and y is the
number of recycled pairs (n, m) with A <= n < m <= B.

Limits
1 <= T <= 50.
A and B have the same number of digits.

Small dataset
1 <= A <= B <= 1000.

Large dataset
1 <= A <= B <= 2000000.

Sample
Input

4
1 9
10 40
100 500
1111 2222

output

Case #1: 0
Case #2: 3
Case #3: 156
Case #4: 287
'''

from collections import deque
from decimal import Decimal
import heapq
import itertools
import random
import re
import sys

MAX = 2000007

def find_for_A_in_MAX(A,memo):
    n = len(str(A))
    S = set()
    for i in range(1,n):
        M1 = 10 ** i
        M2 = 10 ** (n-i)
        C = (A % M1) * M2 + (A // M1)
        if A < C <= MAX:
            S.add(C)            # dedup 1212: (2121,1212,2121)
    memo[A] = S

def solve(A,B,memo=dict()):
    ans = 0
    while A < B:
        if A not in memo:
            find_for_A_in_MAX(A,memo)
        for a in memo[A]:
            if a <= B:
                ans += 1
        A += 1
    return ans

def check_test(A, B):
    if A != B:
        print '>>>', A
        print '<<<', B
        print "!!!!!!!! FAIL !!!!!!!!"
    else:
        print ":::::::) OK"

def unit_test():
    print
    A,B = 1,9
    check_test(solve(A,B), 0)

    A,B = 10,40
    check_test(solve(A,B), 3)

    A,B = 100,500
    check_test(solve(A,B), 156)

    A,B = 1111,2222
    check_test(solve(A,B), 287)

    A,B = 1,1
    check_test(solve(A,B), 0)

    A,B = MAX,MAX
    check_test(solve(A,B), 0)

    A,B = MAX-1,MAX
    check_test(solve(A,B), 0)

    for i in range(50):
        A,B = random.randint(1,MAX), random.randint(1,MAX)
        A,B = sorted([A,B])
        print solve(A,B)
    A,B = 1,2000000
    print solve(A,B)

if __name__ == '__main__':
#    unit_test()

    for case in xrange(1, int(sys.stdin.next()) + 1):
        A,B = (int(i) for i in sys.stdin.next().split())
        # if case in [12]:
        #     print A
        #     break
        print 'Case #%d:' % case, solve(A,B)
