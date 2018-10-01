t= int(input())
for i in range(t):
    m=0
    d,n=map(int,input().split())
    for j in range(n):
        k,s=map(int,input().split())
        if k<=d:
            yo=(d-k)/s
            if yo > m:
                m=yo

    time=d/m
    print("Case #"+str(i+1)+": "+str(time))
    
        
        
    
