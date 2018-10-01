import sys
from collections import defaultdict

filename = sys.argv[1]

f = open('%s.in' % filename)
g = open('%s.out' % filename, 'w')

DEBUG = sys.argv[2] if len(sys.argv) >= 3 else False
def dlog(s, *n):
    if DEBUG:
        if n:
            print(s % tuple(n))
        else:
            print(s)

T = int(f.readline())
for t in range(T):
    dlog("Case %d", t)
    line = f.readline().strip().split()
    n = int(line[0])
    p = int(line[1])
    line = f.readline().strip().split()
    gs = defaultdict(int)
    for x in line:
    	gs[int(x) % p] += 1

    if p == 2:
    	ans = gs[0] + (gs[1] + 1) / 2

    if p == 3:
    	ans = gs[0]
    	match = min(gs[1], gs[2])
    	left = max(gs[1], gs[2]) - match
    	ans += match + (left + 2) / 3

    g.write('Case #%d: %d' % (t + 1, ans))
    g.write('\n')


