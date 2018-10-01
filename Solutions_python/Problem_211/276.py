from collections import Counter
T = int(input())

for i in range(1, T+1):

    N, K = map(int, input().split())
    U = float(input())
    P = list(map(float, input().split()))
    P.sort()

    c = Counter(P)

    while U > 0:
        k1 = min(c.keys())
        v1 = c[k1]
        del c[k1]

        if len(c) == 0:
            c[k1 + U / v1] += v1
            break
        else:
            k2 = min(c.keys())
            v2 = c[k2]

            needed = (k2 - k1) * v1
            if U >= needed:
                U -= needed
                c[k2] += v1
            else:
                c[k1 + U / v1] += v1
                break

    answer = 1
    for k, v in c.items():
        answer *= k**v
    print(f'Case #{i}: ', end='')
    print("%.6f" % min(1, answer))
