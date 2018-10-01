t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n=[int(e) for e in list(input())]    
    l=len(n) 
    ty=0
    m=0
    jm=-1
    b=False
    for j,a in enumerate(n):
        if(a<m):
            n=n[:j-1]+[n[j-1]-1]+[9]*(l-j)
            b=True
            break
        m=a
        jm=j
    if (b): 
        for j in range(jm-1,-1,-1):
            if(n[j]==m):
                n[j]=m-1
                n[j+1]=9
    if (n[0]==0):
        del n[0]
    print("Case #{}: {}".format(i, "".join([str(e) for e in n]))) 