# encoding: utf-8
import sys
from math import sqrt

def palin(x):
    s = str(x)
    n = len(s)
    for i in xrange(0, n/2):
        if s[i] != s[n-1-i]:
            return False
    return True

def fair_and_square_numbers(A, B):
    sa = int(sqrt(A))
    if (sa*sa) < A:
        sa = sa + 1
    sb = int(sqrt(B))
    
    cnt = 0
    i = sa
    while i <= sb:
        if palin(i) and palin(i*i):
            cnt = cnt + 1
        i = i + 1
    return cnt

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for t in xrange(1, T+1):
        line = sys.stdin.readline().rstrip().split()
        A = int(line[0])
        B = int(line[1])
        ans = fair_and_square_numbers(A, B)
        print 'Case #%d: %d' % (t, ans)