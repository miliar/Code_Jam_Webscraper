from collections import deque
#from decimal import Decimal
from sys import stdin, stderr
import copy
import fractions
import heapq
import itertools
import math
#import networkx as nx
import random
import re
import sys

sys.setrecursionlimit(100)

isa = isinstance
INF = 1 << 66

def winner(A):
    L = []
    for r in A:                 # each row
        L.append(r)
    for j in range(4):          # each col
        col = []
        for i in range(4):
            col.append(A[i][j])
        L.append(col)
    L.append((A[0][0],A[1][1],A[2][2],A[3][3])) # diagonal \
    L.append((A[0][3],A[1][2],A[2][1],A[3][0])) # diagonal /
    for grp in L:
        D = dict()
        for a in grp:
            D.setdefault(a,0)
            D[a] += 1
        K = sorted(D)
        if ['X'] == K:
            return 'X'
        if ['O'] == K:
            return 'O'
        if sorted(['X','T']) == K:
            return 'X'
        if sorted(['O','T']) == K:
            return 'O'
    return None

def solve(A):
    w = winner(A)
    if w:
        ans = "%s won" % w
    else:
        has_empty = False
        for a in A:
            if '.' in a:
                has_empty = True
                break
        if has_empty:
            ans = 'Game has not completed'
        else:
            ans = 'Draw'
    return ans

def check_test(A, B, data='', case=[0]):
    print
    print "test %d:" % case[0]
    print A
    if A != B:
        if data:
            print data
        print '>>>', A
        print '<<<', B
        print "!!!!!!!! FAIL !!!!!!!!"
    else:
        print ":::::::) OK"
    case[0] += 1

def unit_test():
    A, ans = ('XXXT','....','OO..','....',), 'X won'
    check_test(solve(A), ans, A)

    A, ans = ('XOXT','XXOO','OXOX','XXOO',), 'Draw'
    check_test(solve(A), ans, A)

    A, ans = ('XOX.','OX..','....','....',), 'Game has not completed'
    check_test(solve(A), ans, A)

    A, ans = ('OOXX','OXXX','OX.T','O..O',), 'O won'
    check_test(solve(A), ans, A)

    A, ans = ('XXXO','..O.','.O..','T...',), 'O won'
    check_test(solve(A), ans, A)

    A, ans = ('OXXX','XO..','..O.','...O',), 'O won'
    check_test(solve(A), ans, A)

def output():
    for case in xrange(1, int(stdin.next()) + 1):
        A = []
        for _ in range(4):
            A.append(stdin.next().strip())
        ans = solve(A)
        stdin.next()
        print 'Case #%d:' % case, ans
        print >>stderr, 'Case #%d:' % case, ans

if __name__ == '__main__':
#    unit_test()
    output()
