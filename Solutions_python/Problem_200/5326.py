t=int(input())

for cs in range(1,t+1):
    n=input()
    n+='9'
    l=len(n)
    result=''
    if n[0] != '1':
        for i in range(0,l-1):
            
            if n[i]<=n[i+1]:
                    result+=n[i]
            else:
                
                result+=str(int(n[i])-1)
                if result[i]<result[i-1]:
                    result=''
                    result=str(int(n[0])-1)
                    for j in range(1,l-1):
                        result+='9'
                    break
                else:
                    p=i
                    for j in range(p,l-2):
                        result+='9'
                    break
    else:
        for i in range(0,l-1):
            if n[i]>n[i+1] and n[i]=='1':
                for j in range(0,l-2):
                    result+='9'
                break
            elif n[i]<=n[i+1]:
                result+=n[i]
            else:
                result+=str(int(n[i])-1)
                p=i
                for j in range(p,l-2):
                    result+='9'
                break
    print("Case #" + str(cs) + ": "+ result)
                
            
        
                
