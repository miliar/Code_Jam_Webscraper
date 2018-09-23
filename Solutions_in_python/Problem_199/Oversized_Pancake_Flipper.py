import sys
T=int(sys.stdin.readline());z=[];f=open('abrakabra.txt','w')
for i in range(T):
    z,k=sys.stdin.readline().split();b=[]
    k=int(k);os=0;blr=0
    for el in z:
        b.append(el)
    for li in range(len(b)):
        if b[li]=='-':
            if len(b)-li>=k:
                blr+=1
                for j in range(k):
                    if b[li+j]=='-':
                        b[li+j]='+'
                    else:
                        b[li+j]='-'
            else:
                f.write('Case #{}: '.format(i+1)+"IMPOSSIBLE"+'\n')
                os=1
                break
    if os==0:
        f.write('Case #{}: '.format(i+1)+str(blr)+'\n')


