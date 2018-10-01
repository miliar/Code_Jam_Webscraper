def execute(K, N):
    dist = [N]

    dl = 0
    dr = 0

    for k in range(0, K):
        i, n = max(enumerate(dist), key=lambda e: e[1])

        dr = n // 2
        dl = dr - 1 * ((n + 1) % 2)
        dist[i] = dl
        dist.insert(i + 1, dr)

    return max(dl, dr), min(dl, dr)

numTests = int(input())
for i in range(1, numTests + 1):
    n, k = [int(s) for s in input().split(" ")]
    mi, ma = execute(k, n)
    print("Case #{}: {} {}".format(i, mi, ma))
