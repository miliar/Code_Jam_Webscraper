import sys
from collections import defaultdict

def run(t):
    N, K = map(int, raw_input().split())
    s = defaultdict(int)
    s[N] = 1
    while K > 0:
        n = max(s.keys())
        k = s[n]
        n1, n2 = (n - 1) / 2, n / 2
        del s[n]
        K -= k
        if K <= 0:
            print('Case #{}: {} {}'.format(t, n2, n1))
            return
        s[n1] += k
        s[n2] += k

T = int(raw_input())
for t in xrange(1, T + 1):
    run(t)
