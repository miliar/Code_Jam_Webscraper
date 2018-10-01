from sys import stdin
import sys
if len(sys.argv) > 1:
    sys.stdout = open(sys.argv[1], 'w')
from math import pi

def each_case():
    AC, AJ = map(int, stdin.readline().split())
    A = []
    for i in xrange(AC):
        C, D = map(int, stdin.readline().split())
        assert C < D
        A.append((C, D, 0))
    for i in xrange(AJ):
        J, K = map(int, stdin.readline().split())
        assert J < K
        A.append((J, K, 1))
    A.sort(key=lambda a:a[0])

    C, CX, J, JX, X, exch = 0, [], 0, [], 0, 0
    last_j, last_k = A[-1][1] - 1440, A[-1][2]
    for i, j, k in A:
        assert i >= last_j
        if k == 0:
            C += (j-i)
            if last_k == 0:
                CX.append(i - last_j)
            else:
                X += (i - last_j)
                exch += 1
        elif k == 1:
            J += (j-i)
            if last_k == 1:
                JX.append(i - last_j)
            else:
                X += (i - last_j)
                exch += 1
        else:
            assert False

        last_j, last_k = j, k

    C_sum, J_sum = C + sum(CX), J + sum(JX)
    assert C <= 720 and J <= 720 and C_sum + J_sum + X == 1440 and exch % 2 == 0
    if C_sum > 720:
        J_sum += X
        for cx in sorted(CX, reverse=True):
            J_sum += cx
            C_sum -= cx
            exch += 2
            if C_sum <= 720:
                break
        else:
            assert False
    elif J_sum > 720:
        C_sum += X
        for jx in sorted(JX, reverse=True):
            C_sum += jx
            J_sum -= jx
            exch += 2
            if J_sum <= 720:
                break
        else:
            assert False

    return exch

T = int(stdin.readline())
for t in xrange(1,T+1):
    print 'Case #{}: {}'.format(t, each_case())
