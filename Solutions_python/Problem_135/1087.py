T = input()
for t in xrange(T):
    d = {}
    for i in xrange(17): d[i] = 0
    for i in xrange(2):
        r = input()
        c = [map(int,raw_input().split()) for j in xrange(4)]
        for x in c[r-1]:
            d[x] += 1
    res = []
    for i in xrange(17):
        if d[i] == 2:
            res.append(i)
    if len(res) > 1:
        ans = 'Bad magician!'
    elif len(res) == 0:
        ans = 'Volunteer cheated!'
    else:
        ans = str(res[0])
    print 'Case #%d: %s' % (t+1, ans)
