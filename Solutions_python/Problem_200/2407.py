t=int(raw_input())
for j in range(0,t):
    num=map(int,list(raw_input()))
    n=len(num)
    i=0
    flag=0
    for i in range(1,n):
        if num[i]<num[i-1]:
            flag=1
            break
    if(flag):
        i-=1
        while(i>=1 and num[i-1]==num[i]):
            i-=1   
        num[i]-=1
        for i in range(i+1,n):
            num[i]=9
    num=map(str,num)
    sol=int("".join(num))
    print "Case #"+str(j+1)+": "+str(sol)
    
        
        
