for case in range(1, int(input())+1):
    d,n = map(int, input().split())
    times = []
    for i in range(n):
        k,s = map(int, input().split())
        times.append((d-k)*1.0/s)
    velocity = d * 1.0 / max(times)
    print("Case #%d: %.6f"%(case, velocity))
