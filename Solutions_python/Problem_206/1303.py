t = int(input())
for i in range(1, t + 1):
    d, n = [int(a) for a in input().split(' ')]
    # print('Case #{}: {} {}'.format(i, d, n))
    times = []
    for j in range(1, n + 1):
        k, s = [int(b) for b in input().split(' ')]
        time = (d - k) / s
        times.append(time)
    print('Case #{0}: {1:.6f}'.format(i, d / max(times)))
