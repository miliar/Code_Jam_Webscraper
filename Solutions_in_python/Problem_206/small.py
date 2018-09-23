def solve(D, N, horses):
    horses.sort(key=lambda horse: horse[0], reverse=True)
    K = [horses[i][0] for i in range(N)]
    S = [horses[i][1] for i in range(N)]

    K_0, S_0 = K[0], S[0]
    for i in range(1, N):
        if S_0 == S[i]:
            K_0, S_0 = K[i], S[i]
        else:
            if K[i] * S_0 + (D - K_0) * S[i] < D * S_0:
                K_0, S_0 = K[i], S[i]

    return D * S_0 / (D - K_0)

T = int(input())
for t in range(T):
    D, N = [int(x) for x in input().split()]

    horses = list(range(N))
    for n in range(N):
        horses[n] = tuple([int(x) for x in input().split()])

    max_speed = solve(D, N, horses)
    print("Case #%d: %.9f" % (t+1, max_speed))
