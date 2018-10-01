
a=int(input())
lis=[None]*a
i=0
for i in range(a):
    count=0
    tr=input()
    arr=tr.split()
    b=arr[0]
    c=int(arr[1])
    d=list(b)
    for j in range(len(d)):
        if((j==len(d)-1) and (d[j])=='+'):
            lis[i]=count
        elif((j==len(d)-1) and (d[j])=='+'):
            lis[i]="IMPOSSIBLE"
            break
        else:
            if(d[j]=='-'):
                if((len(d)-j+1)>c):
                    for k in range(j,j+c):
                        if d[k]=='+':
                            d[k]='-'
                        else:
                            d[k]='+'
                    count=count+1    
                    
                else:
                    lis[i]="IMPOSSIBLE"
                    break
    
                    
                    
for n in range(len(lis)):
    stre="Case #"+str((n+1))
    stre=str(stre)+": "+str(lis[n])
    print(stre)
                
            
                       
