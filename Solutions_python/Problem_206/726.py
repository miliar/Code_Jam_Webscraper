T = int(input())
for i in range(T):
    D, N = (int(n) for n in input().split())
    Ks = []
    Ss = []
    for j in range(N):
        K, S = (int(n) for n in input().split())
        Ks.append(K)
        Ss.append(S)
    Hs = []
    for K, S in zip(Ks, Ss):
        Hs.append((D-K)/S)
    print('Case #%s: %s' % (i + 1, D/max(Hs)))
