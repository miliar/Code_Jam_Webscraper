T = int(raw_input())
for t in range(1, T+1):
    N, K = map(int, raw_input().split())
    U = float(raw_input())
    P = map(float, raw_input().split())
    P = sorted(P, reverse=True)
    start_i = 0
    while True:
        mean_U = (sum(P[start_i:]) + U) / (N-start_i)
        #print start_i, mean_U, P[start_i]
        for i, p in enumerate(P[start_i:], start_i):
            if p <= mean_U:
                break
        if start_i == i:
            ans = 1.0
            #print P, start_i, mean_U
            #for j in range(start_i, N):
            #    P[i] = mean_U
            for j in range(start_i):
                ans *= P[j]
            ans *= mean_U**(N-start_i)
            break
        else:
            start_i = i

    print 'Case #{}: {}'.format(t, ans)


