import sys

n = int(sys.stdin.readline())

def solve(N, K):
    snappers = [False] * N
    for i in range(K):
        snappers[0] = not snappers[0]
        for j in range(1, N):
            if snappers[j-1] == 0:
                # Now off, was on
                snappers[j] = not snappers[j]
            else:
                # Was off, none of the following snappers get affected
                break
        # print snappers
    return all(snappers)

def solve2(N, K):
    size = 2**N
    value = K % size
    # print K, value, size
    return value + 1 == size

for i in range(n):
    # i = int(sys.stdin.readline())
    # s = sys.stdin.readline().strip('\n')
    N, K = sys.stdin.readline().strip('\n').split()
    N, K = int(N), int(K)
    result = solve2(N, K)
    print >>sys.stderr, '.', 
    print 'Case #%s: %s' % (i+1, ['OFF', 'ON'][result])
