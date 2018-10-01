def solve():
    N,Q = [int(v) for v in input().split()]
    E = []
    S = []
    for i in range(N):
        ei,si = [int(v) for v in input().split()]
        E.append(ei)
        S.append(si)
    D = []
    for i in range(N):
        di = [int(v) for v in input().split()]
        D.append(di)
    DST = []
    for i in range(Q):
        uk,vk = [int(v) for v in input().split()]
        DST.append([uk,vk])
    T = [[10**18 for i in range(N)] for i in range(N)]
    dist = [0 for i in range(N)]
    for i in range(1,N):
        dist[i] = dist[i-1] + D[i-1][i]
    for i in range(1,N):
        if dist[i] <= E[0]:
            T[0][i] = dist[i] / S[0]
    for i in range(1,N):
        for j in range(i+1,N):
            if E[i] >= dist[j]-dist[i]:
                T[i][j] = min(T[k][i] for k in range(N)) + (dist[j]-dist[i])/S[i]
    # print('\n'.join(','.join(str(v) for v in di) for di in T))
    return (min(T[k][N-1] for k in range(N)))

T = int(input())
for t in range(1, T + 1):
    print('Case #%d: %.7f' % (t,solve()))


