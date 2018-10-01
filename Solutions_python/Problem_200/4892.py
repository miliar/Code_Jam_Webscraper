t=int(raw_input())
for j in range(1,t+1):
    n=int(raw_input())
    a=[]
    for i in range(n+1):
        ascending = int("".join(sorted(str(i))))
        if ascending<=n+1:
            a.append(ascending)
    print "case #"+str(j)+":",max(a)
            
