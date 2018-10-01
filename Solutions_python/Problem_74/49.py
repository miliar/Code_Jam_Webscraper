for t in range(int(raw_input())):
    raw = raw_input().split()
    n = int(raw.pop(0))
    pos = {'B':1, 'O':1}
    time = {'B':0, 'O':0}
    res = 0
    for b, r in zip(map(int,raw[1::2]), raw[::2]):
        x = max(abs(pos[r] - b) - (res - time[r]), 0) + 1
        res += x
        time[r] = res
        pos[r] = b

    print 'Case #%d: %d' % (t+1, res)