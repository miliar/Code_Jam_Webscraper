#!/usr/bin/python3

import sys

tol = int(input())

def read_matrix():
    res = []
    for i in range(0,4):
        res.append([int(t) for t in input().split(' ')])
    return res
for i in range(1, tol+1):
    n1 = int(input())
    d1 = read_matrix()
    n2 = int(input())
    d2 = read_matrix()

    l1 = set(d1[n1-1])
    l2 = set(d2[n2-1])

    lt = l1.intersection(l2)

    if len(lt) == 1:
        out = str(lt.pop())
    elif len(lt) > 1:
        out = 'Bad magician!'
    else:
        out = 'Volunteer cheated!'

    print('Case #%d: %s' % (i, out))
