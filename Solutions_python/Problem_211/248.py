from math import pi
tt = int(input())
for case in range(1,tt+1):
    n,k = list(map(int, input().split()))
    u = float(input())
    pb = sorted(list(map(float, input().split())))
    pb.append(1.00)
    tu = u
    i = 1 
    while tu > 0 and i <= n:
#        print(pb, tu)
        if tu - i*(pb[i]-(pb[i-1])) > 0:
            tu -= i*(pb[i]-(pb[i-1]))
            for j in range(i):
                pb[j] = pb[i]
        else:
            for j in range(i):
                pb[j] += tu/i
            break
        i+=1
    ans = pb[0]
    for j in range(1, n):
        ans *= pb[j]
    print("Case #%d: %f"%(case, ans))
