T = input()
for t in xrange(1, T+1):
    N, V, X = raw_input().split()
    N = int(N)
    V, X = float(V), float(X)
    R, C = [0]*N, [0]*N
    for i in xrange(N):
        R[i], C[i] = map(float, raw_input().split())
    if N == 1:
        if C[0] == X:
            print 'Case #%d: %.9f' % (t, V / R[0])
        else:
            print 'Case #%d: IMPOSSIBLE' % t
    else:
        if C[0] < X and C[1] < X:
            print 'Case #%d: IMPOSSIBLE' % t
        elif C[0] > X and C[1] > X:
            print 'Case #%d: IMPOSSIBLE' % t
        else:
            res = float('inf')
            if C[0] != X or C[1] != X:
                a = 1.0 * V * (X - C[1]) / (C[0] - C[1])
                res = min(res, max(a / R[0], (V - a) / R[1]))
            if C[0] == X:
                res = min(res, V / R[0])
            if C[1] == X:
                res = min(res, V / R[1])
            if C[0] == C[1] == X:
                res = min(res, V / (R[0] + R[1]))
            print 'Case #%d: %.9f' % (t, res)
