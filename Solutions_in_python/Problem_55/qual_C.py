f=open("C.in",'r')
g=open("C.out",'w')

t=int(f.readline())
print t
for ind in range(t):
    a = [long(x) for x in f.readline().split()]
    r=a[0];k=a[1];n=a[2]
    b=[long(x) for x in f.readline().split()]
    
    dp=[]
    for x in range(n):
        dp.append(0)
    tot=0L
    for i in range(n):
        sum=b[i]
        j=(i+1)%n
        many = 1
        while sum+b[j]<=k and many<n:
            sum+=b[j]
            j=(j+1)%n
            many+=1
        dp[i]=[(j-i)%n,sum]
        
    cur =0
    for i in range(r):
        tot+=dp[cur][1]
        cur=(cur+dp[cur][0])%n
    #print dp
    print r,k,n,tot
    g.write("Case #"+str(ind+1)+": "+str(tot)+"\n")