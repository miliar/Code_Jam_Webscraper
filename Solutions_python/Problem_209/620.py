import math
rd = input

def ints():
    return list(map(int, rd().split()))

def f(r, h):
    return r * r + 2 * r * h

def g(rh):
    return rh[0]*rh[1]

def solve(k, rhs):
    M = -1
    rhs = sorted(rhs, key=lambda rh: rh[0], reverse=True)
    for i in range(n-k+1):
        p = sorted(rhs[i+1:], key=g, reverse=True)[:k-1]
        assert len(p) == k-1
        M = max(M, f(*rhs[i]) + 2 * sum(g(rh) for rh in p))
    return math.pi * M

for t in range(int(rd())):
    n, k = ints()
    print('Case #{}: {}'.format(t+1,solve(k, [ints() for _ in range(n)])))
