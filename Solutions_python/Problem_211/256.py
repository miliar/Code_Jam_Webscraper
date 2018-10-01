from __future__ import division

from math import floor, ceil

import math
import operator

# f_name = 'sample.in'
f_name = 'C-small-1-attempt2.in'

f_out_name = f_name[:-2] + 'out'


def solve(N, K, U, P):
    # for_sum = [j for j, p in enumerate(P) if p < a]
    # add = (sum(P[j] for j in for_sum) + U)/len(for_sum)
    # resP = [p + add if j in for_sum else p for j, p in enumerate(P)]
    P = sorted(P)
    while U > 0.00000001:
        pmin = min(P)
        if pmin == max(P):
            a = (sum(P) + U) / float(N)
            P = [a] * N
            break

        nextp = min(p for p in P if p > pmin)
        nummin = len([p for p in P if p == pmin])
        a = min(nextp - pmin, U / nummin)
        U -= a * nummin
        P = [p + a if p == pmin else p for p in P]

    res = reduce(operator.mul, P, 1)
    # res = pow(a, N)
    return str(res)


with open(f_name) as f_in, open(f_out_name, 'w') as f_out:
    T = int(f_in.readline())
    for i in xrange(T):
        N, K = map(int, f_in.readline().split())
        U = float(f_in.readline())
        P = map(float, f_in.readline().split())
        out = solve(N, K, U, P)
        f_out.write('Case #{0}: {1}\n'.format(i + 1, out))
