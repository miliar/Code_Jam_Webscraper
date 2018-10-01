n=int(input())
for p in range(n):
    t=int(input())
    for i in range(t,0,-1):
        a=[j for j in str(i)]
        if a==sorted(a):
            b="".join(a)
            print(" Case #{}: {}".format(p+1,b))
            break
