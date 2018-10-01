def last_tidy(a):# n is a list of , seperated numbers
    k=len(a)
    while(a!=sorted(a)):
        for i in range(k-1):
            if a[i]>a[i+1]:
                a[i]-=1
                for j in range(i+1,k):
                    a[j]=9
    return a

tt=int(input())
for t in range(1,tt+1):
    n=list(input())
    n=list(map(int,n))
    ans=last_tidy(n)
    ans=list(map(str,ans))
    ans=("").join(ans)
    ans=int(ans)
    print("Case #"+str(t)+":",ans)