inf = open("a.in", "r")
ouf = open("a.out", "w")
T = int(inf.readline())
for t in range(T):
    print >> ouf, "Case #" + str(t + 1) + ":",
    [X, W, R, total, n] = [int(i) for i in inf.readline().split()]
    total *= 1.0
    k = 2*n + 1
    s = [0.0 for i in xrange(k)]
    w = [0 for i in xrange(k)]
    last = 0
    for i in xrange(n):
        ii = 2 * i + 1
        [beg, end, w[ii]] = [int(j) for j in inf.readline().split()]
        s[ii] = end - beg
        s[ii - 1] = beg - last
        w[ii - 1] = 0
        last = end
    s[k - 1] = X - last
    w[k - 1] = 0

    time = 0.0
    INF = 1000
    for i in xrange(k):
        minW = INF
        minIW = -1
        for j in xrange(k):
            if minW > w[j]:
                minW = w[j]
                minIW = j
        c = minIW
        if total < 0.0:
            raise Error
        if s[c] <= 1.0 * total * (R + w[c]):
            curTime = 1.0 * s[c] / (R + w[c])
            time += curTime
            total -= curTime
            s[c] = 0.0
            w[c] = INF            
        else:
            curTime = 1.0 * total
            time += curTime
            total = 0.0
            s[c] -= 1.0 * curTime * (R + w[c])
            break
    for i in xrange(k): 
        if w[i] == INF:
            if s[i] <> 0.0:
                raise Error
        if s[i] < 0.0:
            raise Error
        time += 1.0 * s[i] / (W + w[i])
    print >> ouf, time
inf.close()
ouf.close()
