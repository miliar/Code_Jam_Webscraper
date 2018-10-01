from sys import *
from pulp import *
import numpy as np


def readval(fi, ty): return ty(fi.readline())


def readtab(fi, ty): return tuple(map(ty, fi.readline().split()))


fi = open(argv[1], 'r')
T = readval(fi, int)
outfile = open('out.txt', 'w')
for k in range(T):
    N, V, X = readtab(fi, float)
    N = int(N)
    R = []
    C = []
    for _ in range(N):
        r, c = readtab(fi, float)
        R.append(r)
        C.append(c)
    prob = LpProblem('test' + str(k), LpMinimize)
    if max(C)<X or min(C)>X:
        outfile.write("Case #" + str(k + 1) + ': IMPOSSIBLE\n')
    else:
        # Variables
        a = []
        for i in range(N):
            a.append(LpVariable('a' + str(i), 0, 1))
            M = LpVariable('mmm', 0, 1000000)

        # Objective
        prob += M

        # Constraints
        prob += sum(a[i] * C[i] for i in range(N)) == X
        for i in range(N):
            prob += a[i] <= M * R[i]
        prob += sum(a[i] for i in range(N)) == 1

        prob.solve()

        # Solution
        for v in prob.variables():
            print v.name, "=", v.varValue

        outfile.write("Case #" + str(k + 1) + ": " + str(V * value(prob.objective)) + '\n')
