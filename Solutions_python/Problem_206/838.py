def solve(D, Hs):
    Hs.sort(reverse=True)
    tm = 0
    for K, S in Hs:
        d = D - K
        t = d / S
        tm = max(t,tm)
    return D / tm

for t in range(1, int(input())+1):
    D, N = map(int, input().split())
    Hs = []
    for n in range(N):
        K, S = map(int, input().split())
        Hs.append((K,S))
    print("Case #{}: {}".format(t, solve(D, Hs)))
