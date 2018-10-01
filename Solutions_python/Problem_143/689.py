T=int(input())
for t in range(0,T):
    print("Case #%d: "%(t+1),end="")
    L=input().split()
    A=int(L[0])
    B=int(L[1])
    K=int(L[2])
    a1=int(A/K)
    a2=A%K
    b1=int(B/K)
    b2=A%K
    c=0
    for a in range(0,A):
        for b in range(0,B):
            if a&b<K:
                c+=1
    print(c)
