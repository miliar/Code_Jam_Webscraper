
t = int(raw_input())
for i in xrange(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]
    ingre = [int(s) for s in raw_input().split(" ")]
    have = []
    for _ in xrange(n):
        have.append([int(s) for s in raw_input().split(" ")])
    for j in xrange(n):
        have[j] = sorted(have[j])
    for j in xrange(n):
        for k in xrange(m):
            have[j][k] = (int(float(have[j][k])/(1.1*ingre[j])+0.999999), int(float(have[j][k])/(0.9*ingre[j])))
    has = [[False for _ in xrange(m)] for _ in xrange(n)]
    for j in xrange(n):
        for k in xrange(m):
            if have[j][k][0] > have[j][k][1]:
                has[j][k] = True
    res = 0
    for j in xrange(m):
        found = False
        for num in xrange(have[0][j][0],have[0][j][1] + 1):
            choose = []
            for k in xrange(1, n):
                for t in xrange(m):
                    if not has[k][t] and have[k][t][0] <= num <= have[k][t][1]:
                        choose.append(t)
                        break
            if choose.__len__() == n - 1:
                for k in xrange(1, n):
                    has[k][choose[k-1]] = True
                res += 1
                found = True
            if found:
                break

    print "Case #{}: {}".format(i, res)