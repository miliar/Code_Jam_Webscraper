f = open('ans.txt', 'w')
n = int(input())
for i in range(1,n+1):
    D, N = map(int, input().split())
    t = 0
    for j in range(N):
        o, k = map(int, input().split())
        t = max(t, (D-o)/k)
    u = D/t
    f.write(f"Case #{i}: {u}\n")