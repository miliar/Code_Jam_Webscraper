def possible(lawn, N, M):
    L = [[100]*M for _ in range(N)]
    for i, row in enumerate(lawn): # rows
        L[i][:] = [max(row)]*M
    for j, col in enumerate(zip(*lawn)): # transpose
        m = max(col)
        for i in range(N):
            if L[i][j] > m:
                L[i][j] = m
    return L == lawn

for i in range(1, int(raw_input()) + 1):
    N, M = map(int, raw_input().split())
    lawn = [map(int, raw_input().split()) for _ in range(N)]
    print "Case #%d: %s" % (i, "YES" if possible(lawn, N, M) else "NO")
