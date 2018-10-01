#!/usr/bin/python

from pprint import pprint
import time
from sys import stdout, stdin, stderr
import sys

def read_int(strLine):
    return map(int, strLine)

def rsreadline():
    return inputfile.readline().rstrip('\r\n')

S = 'abcabcabcabc'
K = 4

class MinDict(dict):
    def __setitem__(self, item, val):
        if not self.has_key(item) or self[item] > val:
            dict.__setitem__(self, item, val)

def sorted_insert_t(t, i):
    return filter(lambda x: x<=i, t) + (i,) + filter(lambda x: x>i, t)

def score(prevlast, newlast):
    sum = 0
    for j in range(0, len(S), K):
        if S[j+prevlast] != S[j+newlast]:
            sum += 1
    return sum

def endscore(last, first):
    sum = 0
    for j in range(0, len(S)-K, K):
        if S[j+last] != S[j+K+first]:
            sum += 1
    return sum+1

def step(state):
    global S, K
    nextstate = MinDict()
    for (last, all),(v, first) in state.iteritems():
        for j in range(0, K):
            if j not in all:
                nextstate[j, sorted_insert_t(all,j)] = (v + score(last, j), first)
    return nextstate

def middle(x1,y1,z1,p1, x2,y2,z2,p2):
    return (
        (x1*p2+x2*p1)/(p1+p2),
        (y1*p2+y2*p1)/(p1+p2),
        (z1*p2+z2*p1)/(p1+p2)
        )

# def res(rgShips, x, y, z):
#     r = []
#     for (xi, yi, zi, pi) in rgShips:
#         r.append((abs(xi - x) + abs(yi - y) + abs(zi - z)) / pi)
#     return max(r)

def res(rgShips, i, c):
    return max(map(lambda x: abs(c - x[i])/x[3], rgShips))

def subcoord(rgShips, i):
    return map(lambda x: x[i], rgShips)

def main():
    cCase = int(rsreadline())
    for iCase in range(0, cCase):
        cRows = int(rsreadline())
        matrix = []
        for i in range(0, cRows):
            matrix.append(read_int(rsreadline()))
        s = 0
        for i in range(0, cRows):
            for j in range(0, len(matrix)):
                if sum(matrix[j][i+1:]) == 0: break
            s += j
            del matrix[j]
        print 'Case #%d: %d' % (iCase + 1, s)
        stdout.flush()

inputfile = stdin

if __name__ == '__main__' and not sys.argv[0] == '-c':
    main()
elif sys.argv[0] == '-c':
    print time.strftime('%Y%m%d %H%M%S') + ' loaded'
    print '--'
    inputfile = file('input')
    main()
    print '--'
