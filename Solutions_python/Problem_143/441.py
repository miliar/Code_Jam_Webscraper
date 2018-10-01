import sys

def solve(c):
    print 'Case #%d:' % c,
    A, B, K = [int(n) for n in sys.stdin.readline().split()]
#    print A, B, K
    pairs = 0
    for a in xrange(A):
        for b in xrange(B):
            if a&b < K:
                pairs += 1
    print pairs


N = int(sys.stdin.readline())
for c in xrange(1, N+1):
    solve(c)
