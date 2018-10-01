t=int(raw_input().strip())
for i in xrange(t):
    n=int(raw_input().strip())
    if n<=9:
        print '{} #{}: {}'.format('Case',i+1,n)
    else:
        temp=1
        N=n
        while N>=0:
           k=str(N)
           for j in xrange(len(k)-1):
               if int(k[j])<=int(k[j+1]):
                   temp=0
               else:
                   temp=1
                   break
           if temp==0:
                print '{} #{}: {}'.format('Case',i+1,N)
                break
           N-=1
