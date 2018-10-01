t = int(input())
for i in range(t):
    n = input()
    n = int(n)
    for j in range(n,0,-1):
        c=0
        m = list(str(j))
        for k in range(len(m)-1):
            if m[k]>m[k+1]:
                c =1
        if c==0:
            print("Case #{}: {}".format(i+1, j))
            break
