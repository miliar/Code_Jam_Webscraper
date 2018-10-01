T=int(input())
for t in range(T):
    N=int(input())
    nstr=str(N)
    myint="0"
    for i in range(len(nstr)):
        best=0
        for j in range(10):
            if j>=int(myint[-1]):
                temp=myint+str(j)*(len(nstr)-i)
                if int(temp)<=N:
                      best=j
        myint+=str(best)
    print("Case #" + str(t+1) + ": " + str(int(myint)))
    
