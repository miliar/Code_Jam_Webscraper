from sys import stdin
import sys
if len(sys.argv) > 1:
    sys.stdout = open(sys.argv[1], 'w')

def multi(x, y): return x*y

def each_case():
    N, K = map(int, stdin.readline().split())
    U = float(stdin.readline())
    P = map(float, stdin.readline().split())

    assert N == K
    P.sort()
    P.append(1)
    for i in xrange(1, len(P)):
        u = (P[i] - P[i-1])*i
        if U >= u:
            U -= u
            for j in xrange(i):
                P[j] = P[i]
        else:
            x = P[i-1] + U/i
            for j in xrange(i):
                P[j] = x
            break

    return reduce(multi, P)

T = int(stdin.readline())
for t in xrange(1,T+1):
    print 'Case #{}: {}'.format(t, each_case())
