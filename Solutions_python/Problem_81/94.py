f = open('input.txt', 'r')

T = int(f.readline())

def cal_wp(x):
    win = 0
    n = 0
    for y in x:
        if y == '1':
            win += 1
        if y != '.':
            n += 1
    return float(win) / float(n)

for ttt in xrange(1, T + 1):

    N = int(f.readline())

    L = []

    for i in xrange(N):
        L.append(f.readline().strip())

    WP = [cal_wp(L[i]) for i in xrange(N)]
    OWP = [0 for i in xrange(N)]

    for i in xrange(N):
        n = 0
        for j in xrange(N):
            if L[i][j] != '.':
                n += 1
                t = L[j][:i] + '.' + L[j][i + 1:]
                OWP[i] += cal_wp(t)
        OWP[i] /= float(n)

    OOWP = [0 for i in xrange(N)]

    for i in xrange(N):
        n = 0
        for j in xrange(N):
            if L[i][j] != '.':
                n += 1
                OOWP[i] += OWP[j]
        OOWP[i] /= float(n)

    print 'Case #{}:'.format(ttt)

    for i in xrange(N):
        print 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]
