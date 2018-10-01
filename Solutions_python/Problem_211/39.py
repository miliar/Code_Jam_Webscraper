T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())
    u = float(input())
    ps = list(map(float, input().split()))

    ps.sort(reverse=True)
    
    acc_p = 1

    for i, p in enumerate(ps):
        if sum(ps[i:])+u >= (n-i)*p:
            acc_p *= ((sum(ps[i:])+u)/(n-i))**(n-i)
            break
        else:
            acc_p *= p

    print("Case #%d:" % t, min(acc_p, 1.0))

