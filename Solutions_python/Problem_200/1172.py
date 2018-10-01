t=input()
for z in range(1,int(t)+1):
    n=input()
    a=[]
    for i in n:
        a.append(int(i))
    for i in range(len(a)-1,0,-1):
        if a[i]<a[i-1]:
            a[i]=9
            a[i-1]=a[i-1]-1
            for j in range(i+1,len(a)):
                a[j]=9
    temp=[]
    for i in range(len(a)):
        temp.append(str(a[i]))
    ans=int(''.join(temp))
    print("Case #%d: %d"%(z,ans))
