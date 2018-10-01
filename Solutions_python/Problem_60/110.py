
for case in range(1, int(input()) + 1):
    (N,K,B,T) = map(int, input().split())
    pos = list(map(int, input().split()))
    speed = list(map(int, input().split()))
    time = [(B - pos[i]) / speed[i] for i in range(N)]

    (k, swaps, stragglers) = (0, 0, 0)
    for i in range(N-1, -1, -1):
        if k == K:
            break
        if time[i] <= T:
            k += 1
            swaps += stragglers
        else:
            stragglers += 1

    print('Case #%d: %s' % (case, 'IMPOSSIBLE' if k < K else swaps))
