T = int(input())
for case in range(1, T+1):
    d, n = map(int, input().split())
    max_time = 0
    for i in range(n):
        k, s = map(int, input().split())
        max_time = max(max_time, (d-k)/s)
    result = d/max_time
    print(f"Case #{case}: {result:.10f}")
