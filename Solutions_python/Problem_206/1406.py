cases = int(input())

for case in range(cases):
    D, N = [int(x) for x in input().split(' ')]

    times = []

    for horse in range(N):
        K, S = [int(x) for x in input().split(' ')]

        time = (D - K) / S

        times.append(time)

    print('Case #{}: {}'.format(case + 1, D / max(times)))

