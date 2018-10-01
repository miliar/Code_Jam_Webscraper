from math import pi
tt = int(input())
for case in range(1,tt+1):
    n,k = list(map(int, input().split()))
    ck = []
    for i in range(n):
        r, h = list(map(float, input().split()))
        ck.append((2*pi*r*h, pi * r**2))
    ck = sorted(ck, key=lambda w: -w[1])
    use = [0.0]*(k+1)
    for it in ck:
        for b in range(k-1,-1,-1):
            if b == 0:
                use[1] = max(use[1], sum(it))
            else:
                use[b+1] = max(use[b+1], use[b]+it[0])
    print("Case #%d: %f"%(case, use[k]))
