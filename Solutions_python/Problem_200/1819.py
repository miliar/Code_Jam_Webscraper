
T = int(raw_input().strip())

for idx in range(1, T+1):
    N = map(int, list(raw_input().strip()))
    N.reverse()

    if len(N) == 1:
        print "Case #%d: %d" % (idx, N[0])
        continue

    cur = 0
    nxt = 1
    while nxt < len(N):
        if N[nxt] <= N[cur]:
            cur = nxt
            nxt += 1
            continue
        N[nxt] -= 1
        for i in range(cur+1):
            N[i] = 9

        cur = nxt
        nxt += 1

    N.reverse()
    val = int("".join(map(str, N)))

    print "Case #%d: %d" % (idx,val)


