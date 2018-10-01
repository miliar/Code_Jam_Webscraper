def profit(n):
    l=0;x=0
    for x in range(len(n)-1):
        k=int(n[x]);z=int(n[x+1])
        if k > z:
            n[x]=int(n[x])-1
            l=1
            break
    for i in range(1,len(n)-x+l-1):
        n[x+i]=9
    if l==1:
        if n[0]==0:
            profit(n[1:])
        else:
            profit(n)
    if n[0]==0:
        n.pop(0)
    return n
f=open('asss.txt','w')
T=input();u=[];b=''
for i in range(T):
    k=str(input())
    for el in k:
        u.append(el)
    k=profit(u)
    for el in k:
        b+='{}'.format(el)
    f.write('Case #{}: '.format(i+1)+b+'\n')
    u=[];b=''
