from math import floor

TC = int(input())

for tc in range(1, TC + 1):
    D, N = map(int, input().split())

    mx_time = -1
    for _ in range(N):
        K, S = map(int, input().split())
        need = (D - K) / S
        mx_time = max(mx_time, need)

    speed = D / mx_time
    print('Case #{}: {}'.format(tc, speed))
