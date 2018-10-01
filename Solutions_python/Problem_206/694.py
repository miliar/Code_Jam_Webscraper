T = int(input())

for x in range(T):
    D, N = map(int, input().split(" "))
    slow = 0
    for y in range(N):
        H, S = map(int, input().split(" "))
        T = (D - H) / S
        if T > slow:
            slow = T
    ans = D/slow
    print("Case #" + str(x+1) + ": "+str("%.6f" % ans))
    
