t = int(raw_input().strip())

for tctr in xrange(t):
    c, f, x = (float(x) for x in raw_input().strip().split())
    best = float('inf')
    rate = 2.0
    genbest = True
    gentime = c / rate
    waittime = x / rate
    genwaittime = 0.0

    while genbest:
        genwaittime = gentime + x / (rate + f)
        if genwaittime < waittime:
            min = genwaittime
            genbest = True
        else:
            min = waittime
            genbest = False
        if min < best:
            best = min
        rate += f
        gentime += c / rate
        waittime = genwaittime
    print('Case #{}: {}'.format(tctr+1, best))


