import sys

t = int(sys.stdin.readline())

for c in xrange(t):
    r, k, n = map(int, sys.stdin.readline().split())
    g = map(int, sys.stdin.readline().split())
    tmp = g+g

    s = [[0 for i in xrange(n)] for i in xrange(n)]

    result = 0

    for i in xrange(r):
        p = 0
        j = 0
        while j < n and p+g[j] <= k:
            p += g[j]
            j += 1

        result += p
        g = g[j:]+g[:j]

    print "Case #%d: %d" % (c+1, result)
