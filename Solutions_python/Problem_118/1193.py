def palain(j):
    t=str(j)
    rr=True
    for x in range(len(t)//2):
        rr=rr and t[x]==t[len(t)-1-x]
    return rr
            

T=int(input())

for i in range(T):
    l=input().split()
    a=int(l[0])
    b=int(l[1])
    r=0
    for j in range(a,b+1):
        if((j//(j**0.5)==j**0.5)and(palain(j))and(palain(int(j**0.5)))):
            r+=1
                    
    print("Case #"+str(i+1)+": "+str(r))
