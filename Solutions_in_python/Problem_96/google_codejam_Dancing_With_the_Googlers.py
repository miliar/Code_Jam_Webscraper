'''
Qualification Round 2012

Problem B. Dancing With the Googlers

Small input
10 points

Large input
10 points

You're watching a show where Googlers (employees of Google)
dance, and then each dancer is given a triplet of scores by
three judges. Each triplet of scores consists of three
integer scores from 0 to 10 inclusive. The judges have very
similar standards, so it's surprising if a triplet of scores
contains two scores that are 2 apart. No triplet of scores
contains scores that are more than 2 apart.

For example: (8, 8, 8) and (7, 8, 7) are not surprising.
(6, 7, 8) and (6, 8, 8) are surprising. (7, 6, 9) will never
happen.

The total points for a Googler is the sum of the three scores
in that Googler's triplet of scores. The best result for a
Googler is the maximum of the three scores in that Googler's
triplet of scores. Given the total points for each Googler,
as well as the number of surprising triplets of scores, what
is the maximum number of Googlers that could have had a best
result of at least p?

For example, suppose there were 6 Googlers, and they had the
following total points: 29, 20, 8, 18, 18, 21. You remember
that there were 2 surprising triplets of scores, and you want
to know how many Googlers could have gotten a best result of
8 or better.

With those total points, and knowing that two of the triplets
were surprising, the triplets of scores could have been:

10 9 10
6 6 8 (*)
2 3 3
6 6 6
6 6 6
6 7 8 (*)

The cases marked with a (*) are the surprising cases. This
gives us 3 Googlers who got at least one score of 8 or better.
There's no series of triplets of scores that would give us a
higher number than 3, so the answer is 3.

Input

The first line of the input gives the number of test cases,
T. T test cases follow. Each test case consists of a single
line containing integers separated by single spaces. The
first integer will be N, the number of Googlers, and the
second integer will be S, the number of surprising triplets
of scores. The third integer will be p, as described above.
Next will be N integers ti: the total points of the Googlers.

Output

For each test case, output one line containing "Case #x: y",
where x is the case number (starting from 1) and y is the
maximum number of Googlers who could have had a best result
of greater than or equal to p.

Limits
1 <= T <= 100.
0 <= S <= N.
0 <= p <= 10.
0 <= ti <= 30.
There will be at least S total points between 2 and 28,
inclusive.

Small dataset
1 <= N <= 3.

Large dataset
1 <= N <= 100.

Sample
Input

4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21

Output

Case #1: 3
Case #2: 2
Case #3: 1
Case #4: 3
'''

from collections import deque
from decimal import Decimal
import heapq
import itertools
import re
import sys

def is_possible(N,S,p,T):
    count = 0
    for i in range(len(T)):
        a,b,c = 0,0,0
        a, use_S = p, False
        if S > 0 and a-2 >= 0:
            b = a - 2
            S -= 1
            use_S = True
        elif a-1 >= 0:
            b = a - 1
        c = T[i] - a - b
        if c >= 0 and (c >= a or a-c < 2 or (use_S and a-c <= 2)):
            count += 1
        else:
            if use_S:
                S += 1
    return count >= N

def solve(S,p,T):
    T = sorted(T)
    lo,hi = 0,len(T)
    while lo < hi:
        mid = lo + (hi-lo+1)/2
        if is_possible(mid,S,p,T) is False:
            hi = mid - 1
        else:
            lo = mid
    return lo

def check_test(A, B):
    if A != B:
        print '>>>', A
        print '<<<', B
        print "!!!!!!!! FAIL !!!!!!!!"
    else:
        print ":::::::) OK"

def unit_test():
    print
    S,p,T = 1, 5, [15,13,11]
    check_test(solve(S,p,T), 3)

    S,p,T = 0, 8, [23,22,21]
    check_test(solve(S,p,T), 2)

    S,p,T = 1, 1, [8,0]
    check_test(solve(S,p,T), 1)

    S,p,T = 2, 8, [29,20,8,18,18,21]
    check_test(solve(S,p,T), 3)

    S,p,T = 1, 1, [1,0]
    check_test(solve(S,p,T), 1)

    S,p,T = 1, 1, [0,0]
    check_test(solve(S,p,T), 0)

    S,p,T = 0, 1, [0,0]
    check_test(solve(S,p,T), 0)

    S,p,T = 1, 0, [0,0]
    check_test(solve(S,p,T), 2)

if __name__ == '__main__':
#    unit_test()

    for case in xrange(1, int(sys.stdin.next()) + 1):
        A = [int(i) for i in sys.stdin.next().strip().split()]
        N,S,p = A[:3]
        T = A[3:3+N]
        # if case in [12]:
        #     print A
        #     break
        print 'Case #%d:' % case, solve(S,p,T)
