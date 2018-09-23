import math

with open("A-small-attempt0.in") as f:
    T = int(f.readline())

    for test in range(T):
        N, K = [int(e) for e in f.readline().split(" ")]

        pans = []
        for i in range(N):
            R, H = [float(e) for e in f.readline().split(" ")]
            pans.append((R, H))

        pans.sort()
        pans = list(reversed(pans))

        d = list()
        d.append([0] * N)

        d.append([])
        for i in range(N):
            best_prev = pans[i][0] * pans[i][0] + 2.0 * pans[i][0] * pans[i][1]
            for j in range(i):
                if d[1][j] > best_prev:
                    best_prev = d[1][j]
            d[1].append(best_prev)

        for height in range(2, K + 1):
            d.append([])

            for i in range(N):
                best = d[height - 1][0]
                for j in range(i):
                    if d[height - 1][j] + 2.0 * pans[i][0] * pans[i][1] > best:
                        best = d[height - 1][j] + 2.0 * pans[i][0] * pans[i][1]
                for j in range(i):
                    if d[height][j] > best:
                        best = d[height][j]
                d[height].append(best)

        # print(d)
        print("Case #{0}: {1}".format(test + 1, d[K][N - 1] * math.pi))
