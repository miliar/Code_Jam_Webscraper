#
# problemA.py
#

# Import
import sys
sys.dont_write_bytecode = True
sys.path.append('../')
from gcj import Problem
from gcj.utils import Timer

from math import pi
import itertools

def expAreaSide(r,h):
    return 2*pi*r*h

def expAreaTop(r):
    return r*r*pi

def totalArea(R,H):
    s = R[0]**2
    for r,h in zip(R,H):
        s += 2*r*h
    return s*pi

# Parser
def parser(fin):
    N,K = fin.readInts()
    R = []
    H = []

    for _ in xrange(N):
        r,h = fin.readInts()
        R.append(r)
        H.append(h)

    return N,K,R,H


def solver(data):

    N,K,R,H = data

    P = [(r,h) for r,h in zip(R,H)]
    P = sorted(P)[::-1]

    area = 0
    for p in itertools.combinations(P,K):
        R = [p[i][0] for i in xrange(K)]
        H = [p[i][1] for i in xrange(K)]

        A = totalArea(R,H)
        if A > area:
            area = A

    return '{0:.6f}'.format(area)


# Main
if __name__ == '__main__':
    with Timer('Problem A'):
        Problem(parser, solver).run()
