T = int(raw_input())

def solve(N, K):
    if N == K:
        return 0, 0

    a = (N - 1) / 2
    b = (N - 1) - a

    k1 = (K - 1) / 2
    k2 = (K - 1) - k1

    if K == 1:
        return b, a
    if K == 2:
        return solve(b, 1)
    if (N - 1) % 2 == 0:
        return solve(b, k2)
    if (K - 1) % 2 == 0:
        return solve(a, k1)
    return solve(b, k2)

for t in xrange(1, T + 1):
    N, K = map(int, raw_input().split())
    print 'Case #{}: {}'.format(t, ' '.join(map(str, solve(N, K))))
