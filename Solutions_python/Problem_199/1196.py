for yu in range (int(input())):
    y,n=input().strip().split(' ')
    y=[i for i in y]
    n=int(n)
    c=0
    k=9
    i=0
    while i<len(y):
        p=y[i]
        if p=='-':
            j=i
            c+=1
            if i+n<=len(y):
                while j<i+n :
                    if y[j]=='+':
                        y[j]='-'
                    else:
                        y[j]='+'
                    j+=1
            else:
                k=0
                break
        if k==0:
            break
        i+=1
    if k==0:
        print('Case #'+str(yu+1)+':','IMPOSSIBLE')
    else:
        print('Case #'+str(yu+1)+':',c)
       
