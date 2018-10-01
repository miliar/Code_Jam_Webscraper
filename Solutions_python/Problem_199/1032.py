



T = raw_input()
T = int(T)

for i in range(T):
    line = raw_input()
    S, K = line.split()
    K = int(K)
    #print(S)
    #print(K)
    bing = [c == '+' for c in S]
    if all(bing):
        print("Case #%d: 0" % (i+1))
        continue

    l = len(S)
    count = 0
    for j in range(l-K+1):
        if bing[j]:
            continue
        else:
            # flip bing
            for k in range(K):
                bing[j+k] = not bing[j+k]
            count = count + 1

    if all(bing):
        print("Case #%d: %d" % (i+1, count))
    else:
        print("Case #%d: IMPOSSIBLE" % (i+1))


