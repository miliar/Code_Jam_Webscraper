from sys import stdin

testcases = int(stdin.readline())

N = M = 0


for testcase in xrange(1, testcases + 1):
    ans = True
    N, M = map(int, stdin.readline().split())
    A = []
    for i in xrange(0, N):
        line = map(int, stdin.readline().split())
        A.append(line)
    r_max = [0] * N
    c_max = [0] * M
    for i in xrange(0, N):
        for j in xrange(0, M):
            r_max[i] = max(r_max[i], A[i][j])
            c_max[j] = max(c_max[j], A[i][j])
    for i in xrange(0, N):
        for j in xrange(0, M):
            if A[i][j] < r_max[i] and A[i][j] < c_max[j]:
                ans = False
    print 'Case #%d: %s' % (testcase, 'YES' if ans else 'NO')
