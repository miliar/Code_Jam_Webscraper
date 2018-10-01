import math
t=int(raw_input(''))

for i in range(1,t+1,1):
    s=raw_input('')
    s=str(s)
    indx=0
    x=0
    
    for j in range(0,len(s)-1,1):
        if s[j]>s[j+1]:
            x=1
            break
    
    if x==0:
        print 'Case #%d: %d'%(i,int(s))
    
    else:
        flag=0
        for j in range(0,len(s)-1,1):
            if (s[j])>=(s[j+1]):
                indx=j
                flag=1
                break
        
        if flag==1:
            p=int(pow(10,len(s)-indx-1))
            s=int(s)
            s=s-(s%p)
            print 'Case #%d: %d'%(i,s-1)
        else:
            print 'Case #%d: %d'%(i,int(s))