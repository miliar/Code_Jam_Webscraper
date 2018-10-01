def check(num):
    x=[]
    while(num%10 or num/10):
        x.insert(0,num%10)
        num=int(num/10)
        l=len(x)
    for i in range(l-1):
        if(x[i]>x[i+1]):
            return 0 
    return 1


T=int(input())
for i in range(T):
    x=int(input())
    while(check(x)==0):
        x-=1
    print("Case #"+str(i+1)+":",x)
