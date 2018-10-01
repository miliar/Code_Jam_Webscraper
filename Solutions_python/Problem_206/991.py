def solve(D,N,horses):
    time_needed = []
    for (k,s) in horses:
        time_needed.append((D-k)/s)
    time = max(time_needed)
    return D/time


t = int(input())
for t_i in range(1,t+1):
    dn = [int(x) for x in input().split()]
    D = dn[0]
    N = dn[1]
    horses = []
    for i in range(N):
        horses.append([int(x) for x in input().split()])
    print("Case #{}: {:.6f}".format(t_i, solve(D,N,horses)))

