t=int(input())
for i in range(0,t):
    s,a=map(str,input().split())
    count=0
    l=[]
    for j in a:
        l.append(int(j))
    total=0
    for j in range(0,len(l)):
        if(l[j]==0 and j==0):
            count=1
            l[j]=1
        else:
            if(l[j]==0):
                total=total+l[j]
            else:
                if(j>total):
                    count=count+(j-total)
                    total=total+(j-total)
        total+=l[j]
    print("Case #%d: %d"%(i+1,count))
            
    
