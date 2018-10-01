

for trial in range(int(raw_input())):
    raw = raw_input().split()
    n = int(raw.pop(0))
    b,o = 1,1
    p = {'B':1, 'O':1}
    t = {'B':0, 'O':0}
    r = 0
    for c, u in zip(raw[::2], map(int,raw[1::2])):
        time = max(abs(p[c] - u) - (r - t[c]), 0) + 1
        r += time
        # print '%s %d time=%d r=%d' % (c,u,time,r)
        t[c] = r
        p[c] = u

    print 'Case #%d: %d' % (trial+1, r)



