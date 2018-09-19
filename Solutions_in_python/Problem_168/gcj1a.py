import os
import sys

__author__ = 'dkopiychenko'


def check(i,j,l):
    for x in range(len(l)):
        if x != i and l[x][j] != '.': return True
    for y in range(len(l[0])):
        if y != j and l[i][y] != '.': return True
    return False


def solve(r,c,l):
    s = 0
    for i in range(r):
        j = 0
        while j < c and l[i][j] == '.':
            j += 1
        if j == c: continue
        if l[i][j] == '<':
            if check(i,j,l):
                s += 1
            else: return 'IMPOSSIBLE'

        j = c - 1
        while j >= 0 and l[i][j] == '.':
            j -= 1
        if j == -1: continue
        if l[i][j] == '>':
            if check(i,j,l):
                s += 1
            else: return 'IMPOSSIBLE'

    for j in range(c):
        i = 0
        while i < r and l[i][j] == '.':
            i += 1
        if i == r: continue
        if l[i][j] == '^':
            if check(i,j,l):
                s += 1
            else: return 'IMPOSSIBLE'

        i = r - 1
        while i >= 0 and l[i][j] == '.':
            i -= 1
        if i == -1: continue
        if l[i][j] == 'v':
            if check(i,j,l):
                s += 1
            else: return 'IMPOSSIBLE'

    return s


with open(os.path.expanduser("~/Downloads/A-large (3).in")) as f:
# with open(os.path.expanduser("~/gcj2015/A-test.in.txt")) as f:
    m = int(f.readline().strip())
    print m
    for i in range(m):
        r,c = [int(nn) for nn in f.readline().strip().split(' ')]
        l = []
        for j in range(r):
            l.append(f.readline().strip())
        res = solve(r,c,l)
        print 'Case #' + str(i+1) + ': ' + str(res)

