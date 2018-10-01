#!/usr/bin/env python

def solve(A, motes):
    actions = 0
    while len(motes) > 0:
        if motes[0] < A:
            A = A + motes[0]
            motes = motes[1:]
        else:
            if A > 1:
                return actions + min(solve(A, list([A - 1] + motes)),
                    solve(A, list(motes[1:]))) + 1
            else:
                return actions + solve(A, list(motes[1:])) + 1
    return actions


from sys import argv
from os.path import splitext, basename

if __name__ == "__main__":
    infname = argv[1]
    oufname = splitext(basename(infname))[0] + '.out'
    with open(infname, 'r') as inf:
        with open(oufname, 'w') as ouf:
            T = int(inf.readline())
            for i in range(T):
                (A, N) = (int(x) for x in inf.readline().strip().split(' '))
                motes = sorted([int(x) for x in inf.readline().strip().split(' ')])
                ouf.write('Case #{0}: {1}\n'.format(i + 1, solve(A, motes)))
