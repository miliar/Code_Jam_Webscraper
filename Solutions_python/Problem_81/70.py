inf = open("a.in", "r")
ouf = open("a.out", "w")
T = int(inf.readline())
for t in xrange(T):
    print >> ouf, "Case #" + str(t + 1) + ":"
    n = int(inf.readline())
    a = []
    for i in xrange(n):
        a.append(inf.readline())
    win = [0.0 for i in xrange(n)]
    tot = [0.0 for i in xrange(n)]
    wp = [0.0 for i in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            if a[i][j] == '1':
                win[i] += 1
                tot[i] += 1
            elif a[i][j] == '0':
                tot[i] += 1
        wp[i] = 1.0 * win[i] / tot[i]

#        print win[i], ' ', tot[i]
#        print wp[i]

    owp = [0.0 for i in xrange(n)]
    for i in xrange(n):
        cur = 0.0
        for j in xrange(n): 
            if a[i][j] <> '.':
                if a[i][j] == '1': 
                    cur += win[j] / (tot[j] - 1)
                else:
                    cur += (win[j] - 1) / (tot[j] - 1)
        owp[i] = cur / tot[i]
#        print owp[i]

    oowp = [0.0 for i in xrange(n)]
    for i in xrange(n):
        cur = 0.0
        for j in xrange(n):
            if a[i][j] <> '.':
                cur += owp[j]
        oowp[i] = cur / tot[i]

    res = [0.0 for i in xrange(n)]
    for i in xrange(n):
        res[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]
        print >> ouf, res[i]
inf.close()
ouf.close()    

