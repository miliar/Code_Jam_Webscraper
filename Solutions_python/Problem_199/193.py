__author__ = 'dkopiychenko'

import os

def flip(s,i,k):
    for j in xrange(i, i+k):
        s[j] = - s[j]

def g(s,k):
    n = len(s)
    res = 0
    for i in xrange(n - k + 1):
        if s[i] == -1:
            flip(s, i, k)
            res += 1
    if -1 in s[n - k + 1:]: res = 10**8
    return res

def solve(l, k):
    a = g(list(l), k)
    b = g(l[::-1], k)
    c = min(a,b)
    if c < 10**5: return c
    return 'IMPOSSIBLE'




# with open(os.path.expanduser("~/Downloads/A-small.in")) as f:
with open(os.path.expanduser("~/PycharmProjects/gcj/2017/qualify/A.in")) as f:
    m = int(f.readline().strip('\n'))
    print m
    for i in range(m):
        s,k = f.readline().strip().split(' ')
        l = [1 if x == '+' else -1 for x in s]
        res = solve(l,int(k))
        print 'Case #' + str(i+1) + ': ' + str(res)