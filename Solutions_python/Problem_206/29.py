import sys


def compute(D, N, K, M):
    tmax = 0.0
    for i in xrange(N):
        t = float(D - K[i]) / M[i]
        if t > tmax:
            tmax = t
    return "%.6f" % (D / tmax)


def parse():
    D, N = map(int, sys.stdin.readline().strip().split())
    K = []
    M = []
    for i in xrange(N):
        k, m = map(int, sys.stdin.readline().strip().split())
        K.append(k)
        M.append(m)
    return D, N, K, M


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        data = parse()
        result = compute(*data)
        print "Case #%d: %s" % (i + 1, result)
