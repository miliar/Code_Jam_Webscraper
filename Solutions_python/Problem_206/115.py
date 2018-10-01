
def solve(D, N, K, S):
    hours = 0
    for i in xrange(N):
        hours = max(hours, (D - K[i]) / S[i])
    return D / hours

T = int(raw_input())
for t in xrange(T):
    D, N = map(int, raw_input().split(' '))
    A = [map(float, raw_input().split(' ')) for _ in xrange(N)]
    K, S = zip(*A)
    res = solve(D, N, K, S)
    print 'Case #%d: %s' % (t + 1, res)
