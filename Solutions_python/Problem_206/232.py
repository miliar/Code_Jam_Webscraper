T = int(input())
for t in range(1, T+1):
    d, n = map(int, input().split())
    L = [tuple(map(int, input().split())) for i in range(n)]
    res = max((d-x[0])/x[1] for x in L)
    print("Case #%d: %.10f" %(t, d/res))
