from math import pi
from itertools import combinations

T = int(input().strip())

for t in range(T):
    N, K = map(int, input().strip().split())
    P = []
    for _ in range(N):
        r, h = map(int, input().strip().split())
        P.append((r, h))

    ans = -1
    for c in combinations(P, K):
        max_rad = max(c, key=lambda x: x[0])[0]
        current_answer = pi * (max_rad ** 2)

        for p in c:
            current_answer += 2 * pi * p[0] * p[1]

        if current_answer > ans:
            ans = current_answer

    print(f'Case #{t+1}: {ans}')