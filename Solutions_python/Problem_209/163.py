import sys
import math

sys.setrecursionlimit(1200)

memo = {}
def best(i, N, K, Rs, Hs):
    if (i, K) in memo:
        return memo[i,K]
    if K == 0:
        return 0
    if K == 1:
        ret = max(Rs[j]*Hs[j] for j in xrange(i, N))
        memo[i,K] = ret
        #print i, N
        return ret
    if i == N - 1:
        ret = Rs[i] * Hs[i]
        memo[i, K] = ret
        return ret
    m2 = Hs[i]*Rs[i] + best(i+1, N, K-1, Rs, Hs)
    if N - i >= K:
        m1 = best(i+1, N, K, Rs, Hs)
        ret = max(m1, m2)
    else:
        ret = m2
    memo[i, K] = ret
    return ret


def solve(N, K, Rs, Hs):

    Both = sorted(zip(Rs, Hs), key=lambda x: -x[0])
    Rs = map(lambda x: x[0], Both)
    Hs = map(lambda x: x[1], Both)

    # print 'K = ', K

    # for i in xrange(0, N-K+1):
    #     print 'le best', best(i+1, N, K-1, Rs, Hs)
    #     print 'i=', i, 'got:', Rs[i]*Rs[i] + 2 * Hs[i] * Rs[i] + 2 * best(i+1, N, K-1, Rs, Hs)


    #return

    global memo
    memo = {}

    return math.pi * max(Rs[i]*Rs[i] + 2*Hs[i]*Rs[i] + 2*best(i+1, N, K-1, Rs, Hs) for i in xrange(0, N-K+1))

def main():
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        N, K = map(int, sys.stdin.readline().split())
        Rs, Hs = [], []
        for j in xrange(N):
            R, H = map(int, sys.stdin.readline().split())
            Rs.append(R)
            Hs.append(H)
        ans = solve(N, K, Rs, Hs)
        print 'Case #%s: %s' % (i+1, ans)

if __name__ == '__main__':
    main()
