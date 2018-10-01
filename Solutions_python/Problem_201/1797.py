a=int(input())
list1=[None]*a
for i in range(0,a):
    inpu=input()
    tempo=inpu.split()
    b=int(tempo[0])
    c=int(tempo[1])
    
    
    count=0
    lis=[b]
    result=[None,None]
    while(count!=c):
        b=max(lis)
        
        if(b%2==0):
            temp=b//2
            result=[temp,temp-1]
            lis[lis.index(b)]=temp
            lis.append(temp-1)
        else:
            temp=b//2
            result=[temp,temp]
            
            lis[lis.index(b)]=temp
            lis.append(temp)
        count=count+1
    list1[i]=result
    

for n in range(len(list1)):
    stre="Case #"+str((n+1))
    stre=str(stre)+": "+str(list1[n][0])+" "+str(list1[n][1])
    print(stre)
                       
        
        
    
    
