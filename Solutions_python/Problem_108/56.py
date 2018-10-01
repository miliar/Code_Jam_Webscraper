T = int(input())
for t in range(T):
    N = int(input())
    a = []
    for n in range(N):
        d, l = map(int, input().split())
        a += [[d, l, -1]]
    D = int(input())
    a[0][2] = 2 * a[0][0]
    for i in range(N):
        for j in range(i + 1, N):
            if a[i][2] >= a[j][0]:
                tmp = min(a[j][1], a[j][0] - a[i][0]) + a[j][0]
                a[j][2] = max(a[j][2], tmp)
    ans = False
    for i in range(N):
        if a[i][2] >= D:
            ans = True
    print("Case #%d: %s"%(t + 1, {True: "YES", False: "NO"}[ans]))
                
    
    
