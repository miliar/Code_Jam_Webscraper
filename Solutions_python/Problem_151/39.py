from itertools import product
T = int(raw_input())
for C in xrange(T):
    m, n = map(int, raw_input().strip().split())
    s = [raw_input().strip() for i in xrange(m)]
    ans = 0
    ways = 0
    for dist in product(range(n), repeat=m):
        cur = 0
        for i in xrange(n):
            l = [s[j] for j in xrange(m) if dist[j] == i]
            cur += len(set(j[:k] for j in l for k in xrange(len(j)+1)))
        if cur > ans:
            ans = cur
            ways = 1
        elif cur == ans:
            ways += 1
    print "Case #%d: %d %d" % (C+1, ans, ways % 1000000007)
