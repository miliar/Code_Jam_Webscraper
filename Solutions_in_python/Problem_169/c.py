import scipy.optimize
import numpy as np

t = input()


def solve(n, rs, cs, v, x):
    obj = [0] * n
    obj.append(-1)

    equalities = np.zeros( (4, n+1) )
    for i in xrange(n):
        equalities[0][i] = cs[i] * rs[i]
        equalities[1][i] = rs[i]
        equalities[2][i] = -cs[i] * rs[i]
        equalities[3][i] = -rs[i]
    equalities[0][n] = -x
    equalities[1][n] = -1
    equalities[2][n] = x
    equalities[3][n] = 1
    b = [0, 0, 0, 0]

    bounds = [(0,1)] * n
    bounds.append( (0, None) )
    #print equalities

    q = scipy.optimize.linprog(obj, A_ub = equalities, b_ub = b, bounds=bounds)
    val = np.dot(equalities, q.x)
    if sum(abs(np.dot(equalities, q.x))) <= 10 ** -10:
        return q.fun
    return 0

for case in range(1, t+1):
    n, v, x = map(float, raw_input().split())
    n = int(round(n))
    all = [map(float, raw_input().split()) for _ in xrange(n)]
    rs = [all[i][0] for i in xrange(n)]
    cs = [all[i][1] for i in xrange(n)]
    k = -solve(n, rs, cs, v, x)
    s = None
    #print k
    if k != 0:
        print 'Case #%d: %.12f' % (case, v/k)
    else:
        s = 'IMPOSSIBLE'
        print 'Case #%d: %s' % (case, s)

