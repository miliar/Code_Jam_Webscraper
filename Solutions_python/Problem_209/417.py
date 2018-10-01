import math
t=int(input())
for tt in range(1,t+1,1):
    n,k=[int(x) for x in input().split()]
    r=[]
    for i in range(n):
        ri,hi=[int(x) for x in input().split()]
        r.append((ri,hi))

    print("Case #"+str(tt)+": ",end="")
    r=sorted(r, key=lambda x: x[0],reverse=True)
    max_area=0
    for i in range(0,n-k+1,1):
        cur_area=r[i][0]*r[i][0]
        x=[y[0]*y[1] for y in r[i+1:]]
        x=sorted(x, reverse=True)
        if(k>1):
            cur_area+=2*(sum(x[0:k-1])+r[i][0]*r[i][1])
        else:
            cur_area+=2*r[i][0]*r[i][1]
        max_area=max(max_area,cur_area)

    print(math.pi*max_area)

