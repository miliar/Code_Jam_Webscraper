from functools import reduce
import operator

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

T = int(input())
for t in range(1, T+1):
    N, K = [int(_) for _ in input().split(" ")]
    U = float(input())
    P = [float(_) for _ in input().split(" ")]
    P.sort()
    prefix = P[0]
    ans = prod(P)
    for i in range(1, len(P)):
        diff = P[i] - prefix
        if diff > 0:
            amt = diff * i
            if amt >= U:
                to_add = U/i
                prefix += to_add
                U = 0
                ans = prefix**i * prod(P[i:])
                # print("Case #{}: {}".format(t, ans))
                break
            else:
                U -= amt
                prefix = P[i]
    if U > 0:
        ans = min((prefix + U / N)**N, 1)
    print("Case #{}: {}".format(t, ans))


            

