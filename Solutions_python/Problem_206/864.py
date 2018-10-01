t = int(raw_input())

for i in range(t):
    D, N = map(int, raw_input().split())
    K = []
    S = []
    for j in range(N):
        kj, sj = map(int, raw_input().split())
        K.append(kj)
        S.append(sj)
    slowest_in_seconds = 0
    for x in range(N):
        time_to_end = float(D-K[x])/S[x]
        if time_to_end > slowest_in_seconds:
            slowest_in_seconds = time_to_end
    answer = float(D)/slowest_in_seconds
    print "Case #{}: {}".format(i+1, answer)