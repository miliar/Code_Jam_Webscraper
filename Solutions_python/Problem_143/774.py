t = int(input())
for ab in range(t):
    a, b, k = map(int, input().split())
    count = 0
    for i in range(a):
        for j in range(b):
            x = i & j
            if x < k :
                count += 1
    print("Case #%d: %d" %(ab+1, count))
