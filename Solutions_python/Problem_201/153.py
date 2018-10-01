import heapq as hq

def lr(n):
    r = (n - 1) // 2
    l = n - 1 - r
    return (max(l, r), min(l, r))

T = int(input())
for x in range(1, T + 1):
    N, K = map(int, input().split())
    pq = [-N]
    dict = {}
    dict[N] = 1
    while 0 < K:
        tmp = -hq.heappop(pq)
        cnt = dict[tmp]
        y = lr(tmp)[0]
        z = lr(tmp)[1]
        if 0 < y and y not in dict:
            hq.heappush(pq, -y)
            dict[y] = cnt
        elif y in dict:
            dict[y] += cnt
        if 0 < z and z not in dict:
            hq.heappush(pq, -z)
            dict[z] = cnt
        elif z in dict:
            dict[z] += cnt
        K -= cnt
        del dict[tmp]
    print("Case #%d: %d %d" % (x, y, z))
