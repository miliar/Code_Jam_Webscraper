import sys

def solve(D, horses):
    T = []
    for K, S in horses:
        T.append((D - K) / S)
    return D / max(T)

with open(sys.argv[1]) as fh:
    T = int(next(fh))
    for i in range(T):
        D, N = map(int, next(fh).split())
        horses = []
        for j in range(N):
            K, S = map(int, next(fh).split())
            horses.append((K, S))
        print("Case #{}: {}".format(i+1, solve(D, horses)))
