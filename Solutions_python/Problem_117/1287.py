#!/usr/bin/env python3

T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())

    grid = [list(map(int, input().split())) for i in range(N)]

    rows_max = [max(grid[i][j] for j in range(M)) for i in range(N)]
    cols_max = [max(grid[i][j] for i in range(N)) for j in range(M)]

    valid = True

    for i in range(N):
        for j in range(M):
            if not (rows_max[i] <= grid[i][j] or cols_max[j] <= grid[i][j]):
                valid = False

    print("Case #{}: {}".format(case, "YES" if valid else "NO"))
