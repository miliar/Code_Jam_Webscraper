import sys
from datetime import datetime


def debug(x):
    sys.stderr.write('{} DEBUG: {}\n'.format(datetime.now().time(), x))

MAXD = 1e18

def solve(N, Q):
    energy = [0]*N
    speed = [0]*N
    source = [0]*Q
    dest = [0]*Q
    adj = []
    best = []
    path = [0]
    for i in xrange(N):
        energy[i], speed[i] = map(int, raw_input().split())
    for i in xrange(N):
        adj.append(map(int, list(raw_input().split())))
        best.append(list([MAXD]*N))
    for i in xrange(Q):
        source[i], dest[i] = map(int, raw_input().split())

    best[0][0] = 0.
    # Solve small
    for i in xrange(1, N):
        path.append(path[i-1]+adj[i-1][i])

    dist = lambda x, y: path[max(x,y)] - path[min(x,y)]

    for i in xrange(1, N):
        # debug((i,best))
        for j in xrange(0, i-1):
            if dist(j, i) > energy[j]:
                best[i][j] = MAXD
            else:
                best[i][j] = best[i-1][j] + float(adj[i-1][i])/float(speed[j])
        best[i][i-1] = min(best[i-1]) + float(adj[i-1][i])/float(speed[i-1])
    return min(best[N-1])




    # Solve large


def main():
    T = int(raw_input())
    for tc in xrange(1, T+1):
        debug("Running test #{}...\n".format(tc))
        N, Q = map(int, raw_input().split())
        print "Case #{}: {:.8f}".format(tc, solve(N, Q))


if __name__ == "__main__":
    main()
