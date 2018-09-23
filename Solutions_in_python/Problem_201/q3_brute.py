from math import ceil, floor

T = int(input().strip())
for i in range(T):
    N, K = map(int, input().strip().split())
    res_arr = [N]
    maxS,minS = 0,0
    for _ in range(K):
        b = max(res_arr)
        maxS = ceil((b - 1) / 2)
        minS = floor((b - 1) / 2)
        res_arr.remove(b)
        res_arr.append(minS)
        res_arr.append(maxS)

    print("Case #%d: %d %d" % (i+1, maxS, minS))
