



t = int(input())
for case in range(1, t+1):
    d, n = map(int, input().split())


    def traveltime(k, s):
        return (d-k) / s

    t = max(traveltime(*map(int, input().split())) for _ in range(n))
    print(f"Case #{case}: {d/t}")


