'''
Qualification Round 2012

Problem A. Speaking in Tongues

Small input
15 points

We have come up with the best possible language here at
Google, called Googlerese. To translate text into Googlerese,
we take any message and replace each English letter with
another English letter. This mapping is one-to-one and onto,
which means that the same input letter always gets replaced
with the same output letter, and different input letters
always get replaced with different output letters. A letter
may be replaced by itself. Spaces are left as-is.

For example (and here is a hint!), our awesome translation
algorithm includes the following three mappings: 'a' -> 'y',
'o' -> 'e', and 'z' -> 'q'. This means that "a zoo" will
become "y qee".

Googlerese is based on the best possible replacement mapping,
and we will never change it. It will always be the same. In
every test case. We will not tell you the rest of our mapping
because that would make the problem too easy, but there are
a few examples below that may help.

Given some text in Googlerese, can you translate it to back
to normal text?

Solving this problem

Usually, Google Code Jam problems have 1 Small input and 1
Large input. This problem has only 1 Small input. Once you
have solved the Small input, you have finished solving this
problem.

Input

The first line of the input gives the number of test cases,
T. T test cases follow, one per line.

Each line consists of a string G in Googlerese, made up of
one or more words containing the letters 'a' - 'z'. There
will be exactly one space (' ') character between consecutive
words and no spaces at the beginning or at the end of any
line.

Output

For each test case, output one line containing "Case #X: S"
where X is the case number and S is the string that becomes
G in Googlerese.

Limits
1 <= T <= 30.
G contains at most 100 characters.
None of the text is guaranteed to be valid English.

Sample
Input

3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv

Output

Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
'''

from collections import deque
from decimal import Decimal
import heapq
import itertools
import re
import sys

def mapping():
    D = dict()
    A = [ 'ejp mysljylc kd kxveddknmc re jsicpdrysi',
          'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
          'de kr kd eoya kw aej tysr re ujdr lkgc jv' ]
    B = [ 'our language is impossible to understand',
          'there are twenty six factorial possibilities',
          'so it is okay if you want to just give up' ]
    for Ai,Bi in zip(A,B):
        for a,b in zip(Ai,Bi):
            D[b] = a
    D['z'] = 'q'    
    # for i in sorted(D):
    #     print "'%s', '%s'" % (i, D[i])
    #     '''
    #     ' ', ' '   
    #     'a', 'y'
    #     'b', 'n'
    #     'c', 'f'
    #     'd', 'i'
    #     'e', 'c'
    #     'f', 'w'
    #     'g', 'l'
    #     'h', 'b'
    #     'i', 'k'
    #     'j', 'u'
    #     'k', 'o'
    #     'l', 'm'
    #     'm', 'x'
    #     'n', 's'
    #     'o', 'e'
    #     'p', 'v'
    #     'r', 'p'
    #     's', 'd'
    #     't', 'r'
    #     'u', 'j'
    #     'v', 'g'
    #     'w', 't'
    #     'x', 'h'
    #     'y', 'a'
    #     'z', 'q'
    #      |    |
    #      \   'z' is missing
    #     'q' is missing
    #     '''
    #     # 'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'
    D['q'] = 'z'
    DD = dict()
    for c in D:
        DD[D[c]] = c
    return DD

def solve(S,D=mapping()):
    L = list()
    for s in S:
        if s in D:
            L.append(D[s])
        else:
            L.append(s)
    return ''.join(L)

def check_test(A, B):
    if A != B:
        print '>>>', A
        print '<<<', B
        print "!!!!!!!! FAIL !!!!!!!!"
    else:
        print ":::::::) OK"

def unit_test():
    print
    A = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
    B = 'our language is impossible to understand'
    check_test(solve(A), B)

    A = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
    B = 'there are twenty six factorial possibilities'
    check_test(solve(A), B)

    A = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
    B = 'so it is okay if you want to just give up'
    check_test(solve(A), B)

if __name__ == '__main__':
#    unit_test()

    for case in xrange(1, int(sys.stdin.next()) + 1):
        A = sys.stdin.next().strip()
        # if case in [12]:
        #     print A
        #     break
        print 'Case #%d:' % case, solve(A)
