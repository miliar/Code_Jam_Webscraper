#!/usr/bin/python
import sys

def additionsToEat(A, X):
    i = 0
    if A == 1:
        return A, 1000
    while A <= X:
        A += A - 1
        i += 1
    return A + X, i

def eatSmaller(A, motes):
    while True:
        eaten = sum(x for x in motes if x < A)
        motes = list(x for x in motes if x >= A)
        A += eaten
        if eaten == 0: break
    return A, motes

def solve(A, motes):
    changes = 0
    A, motes = eatSmaller(A, motes)
    while len(motes) > 0:
        newA, x = additionsToEat(A, motes[0])
        if x >= len(motes):
            motes.pop(0)
            changes += 1
        else:
            changes += x
            A = newA
            motes.pop(0)
        A, motes = eatSmaller(A, motes)
    return changes

T = int(sys.stdin.readline())
for i in range(T):
    A, N = map(int, sys.stdin.readline().split(' '))
    motes = list(sorted(map(int, sys.stdin.readline().split(' '))))
    print "Case #{}: {}".format(i+1, solve(A, motes))
