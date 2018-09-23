n=int(input())
for k in range(n):
    x,y=input().split(' ')
    y=int(y)
    count=0
    i=0
    while(i<=len(x)-y):
        if(x[i]=='+'):
            i+=1
        else:
            for j in range(i,i+y):
                if x[j]=='+':
                    x=x[0:j]+'-'+x[j+1:]
                else:
                    x=x[0:j]+'+'+x[j+1:]
            count+=1
            i+=1
    flag=0
    for a in range(len(x)):
        if x[a]=='-':
            print('Case #'+str(k+1)+': IMPOSSIBLE')
            flag=1
            break
        else:
            continue
    if flag==0:
        print('Case #'+str(k+1)+': '+str(count))
