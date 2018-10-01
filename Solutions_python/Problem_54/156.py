from sys import *
from re import *

C = int(stdin.readline())

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)

def gcd_list(X):
    g = X[0]
    for x in X[1:]:
        g = gcd(x, g)
    return g

for c in range(1, C + 1):
    inp = split(' ', stdin.readline())
    N = int(inp[0])
    t = [0] * N
    for n in range(N):
        t[n] = int(inp[n + 1])

    t.sort()
    tt = t[:]
    tt[0] = 0
    for i in range(1, len(t)):
        tt[i] = t[i] - t[0]
    lpa = gcd_list(tt)

    ans = (t[-1] / lpa) * lpa - t[-1]
    if ans < 0:
        ans += lpa

    print 'Case #%d: %d' % (c, ans)
