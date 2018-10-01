T = int(input())
for t in range(1, T + 1):
    D, N = [int(x) for x in input().split()]
    horses = []
    for i in range(N):
        k, s = [int(x) for x in input().split()]
        horses.append((D - k) / s)
    print('Case #%d: %.6f' % (t, D / max(horses)))
