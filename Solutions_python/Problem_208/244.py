def solve_small(distances, staminas, speeds):
    best_times = [None for _ in distances]
    best_times[-1] = distances[-1]/speeds[-2]
    best_times.append(0.)

    # print('distances:', distances)
    # print('staminas:', staminas)
    # print('speeds:', speeds)

    for i in range(len(distances)-2, -1, -1):
        # print('i:', i)
        remaining_stamina = staminas[i]

        best = float('inf')
        for j in range(i+1, len(distances) + 1):
            # print('j:', j)
            remaining_stamina -= distances[j-1]
            if remaining_stamina < 0:
                break
            time = sum(distances[i:j])/speeds[i] + best_times[j]
            # print('time:', time)
            if time < best:
                best = time
        assert best < float('inf')
        best_times[i] = best

    # print('best_times', best_times)

    return best_times[0]


T = int(input())

for i in range(T):
    N, Q = [int(x) for x in input().split(' ')]

    assert Q == 1
    staminas = []
    speeds = []
    for j in range(N):
        E, S = [int(x) for x in input().split(' ')]
        staminas.append(E)
        speeds.append(S)

    # Cities
    distances = []
    for j in range(N):
        ds = [int(x) for x in input().split(' ')]
        assert all(d == -1 for d in ds[:j+1])
        assert all(d == -1 for d in ds[j+2:])
        if j < N-1:
            distances.append(ds[j+1])
    # print('distances', distances)

    query = input()
    assert query == '1 {}'.format(N)

    print('Case #{}: {}'.format(i+1, solve_small(distances, staminas, speeds)))



