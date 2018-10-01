from __future__ import division
from sys import stdin
from numpy import array
import numpy as np

n = 4

def solve(xs):
    def s():
        ys = []
        for i in xrange(n):
            ys.append(xs[:, i])
            ys.append(xs[i, :])
        ys.append(xs.diagonal())
        ys.append(np.fliplr(xs).diagonal())
        for y in ys:
            if all(map(lambda m: m in ['X', 'T'], y)):
                return 'x'
            if all(map(lambda m: m in ['O', 'T'], y)):
                return 'o'
        if '.' in xs:
            return 0
        return 1

    r = s()
    if r == 'x':
        return 'X won'
    if r == 'o':
        return 'O won'
    if r == 0:
        return 'Game has not completed'
    return 'Draw'
                
def main():
    t = int(stdin.next())
    for i in xrange(t):
        x = array([
            list(stdin.next().strip())
            for _ in xrange(n)
        ])
        print 'Case #%d: %s' % (i+1, solve(x))
        if i != t-1:
            stdin.next()

main()
