from sys import stdin

T = int(stdin.readline())
for t in xrange(0, T):
    N = int(stdin.readline())
    WP = [0.0] * N
    numPlay = [0.0] * N
    OWP = [0.0] * N
    numOppPlay = [0.0] * N
    OOWP = [0.0] * N
    RPI = [0.0] * N # (0.25 * WP) + (0.50 * OWP) + (0.25 * OOWP)
    arr = [''] * N
    for n in xrange(0, N):  
        arr[n] = stdin.readline().strip()
        for i in xrange(0, N):
            if (i != n and arr[n][i] != '.'):
                numPlay[n] = numPlay[n] + 1
                if (arr[n][i] == '1'):
                    WP[n] = WP[n] + 1
    for i in xrange(0, N):
        count = 0
        for j in xrange(0, N):
            if (i != j):
                if (arr[j][i] != '.'):
                    OWP[i] = OWP[i] + ((WP[j] - float(arr[j][i])) / (numPlay[j] - 1))
                    count = count + 1
        OWP[i] = OWP[i] / count
    for i in xrange(0, N):
        count = 0
        for j in xrange(0, N):
            if (i != j and arr[i][j] != '.'):
                OOWP[i] = OOWP[i] + OWP[j]
                count = count + 1
        OOWP[i] = OOWP[i] / count
    print 'Case #%d:' % (t + 1)
    for i in xrange(0, N):
        WP[i] = WP[i] / numPlay[i]
        RPI[i] = (0.25 * WP[i]) + (0.50 * OWP[i]) + (0.25 * OOWP[i])
        print RPI[i]
