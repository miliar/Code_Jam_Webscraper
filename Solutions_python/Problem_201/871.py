from collections import defaultdict
import sys

def solve(K, N):
    a = defaultdict(int)
    a[N] = 1
    while True:
        k = max(a.keys())
        k2 = k//2
        k1 = (k-1)//2
        a[k1] += a[k]
        a[k2] += a[k]
        K -= a[k]
        if K <= 0:
            return k2, k1
        del a[k]

lines = open(sys.argv[1]).readlines()
cases = [[int(t) for t in  l.split()] for l in lines[1:]]
for i, (N, K) in enumerate(cases):
    k2, k1 = solve(K, N)
    print("Case #{}: {} {}".format(i+1, k2, k1))
