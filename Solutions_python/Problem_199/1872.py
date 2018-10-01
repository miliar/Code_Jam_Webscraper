n=int(input())
for z in range(n):
    p,f=input().split()
    if p.find('-')==-1:
        print(r'CASE #'+str(z+1)+': '+str(0))
        continue
    p=list(p)
    count=0
    for x in range(len(p)-1,int(f)-2,-1):
        if p[x]=='-':
            count+=1
            for y in range(int(f)):
                if p[x-y]=='-':
                    p[x-y]='+'
                else:
                    p[x-y]='-'
    p=''.join(p)
    if p.find('-')!=-1:
        print(r'CASE #'+str(z+1)+': IMPOSSIBLE')
    else:
        print(r'CASE #'+str(z+1)+': '+str(count))
