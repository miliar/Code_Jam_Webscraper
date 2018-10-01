
import sys
def bathroom(n,k):
    if n==k:
        return (0,0)
    for m in range(len(twos)):
        if twos[m]>n:
            if twos[m-1]<=k:
                return (0,0)
            elif twos[m-2]<=k:
                b=twos[m-1]+twos[m-2]
                if n>=b:
                    dif=n-b
                    if (k-twos[m-2])>=(dif+1):
                        return (1,0)
                    if (k-twos[m-2])<(dif+1):
                        return (1,1)
                    
                else:
                    dif=n-twos[m-1]
                    if (k-twos[m-2])>=(dif+1):
                        return (0,0)
                    if (k-twos[m-2])<(dif+1):
                          return (1,0)
            elif twos[m-3]<=k:
                b=twos[m-1]+3*twos[m-3]
                if n>=b:
                    dif=n-b
                    if (k-twos[m-3])>=(dif+1):
                        return (3,2)
                    if (k-twos[m-3])<(dif+1):
                        return (3,3)
                
            
                        
                    
    lis=[]
    lis.append(n)
    for m in range(k):
        n=max(lis)
        if n%2==0:
            hlf=n/2
            prt=hlf-1
            prt2=hlf
        else:
            hlf=n/2
            prt=hlf
            prt2=hlf
        indx=0
        for m in range(len(lis)):
            if lis[m]==n:
                indx=m

        lis=lis[0:indx]+[prt,prt2]+lis[indx+1:len(lis)]

    return(max([prt,prt2]),min([prt,prt2]))


n=2
twos=[2]
while n<1000000:
    n=n*2
    twos.append(n)
with open(sys.argv[1]) as f:
    lis1 = f.readlines()
lis=[m.strip() for m in lis1[1:len(lis1)]]
cs=0
f=open('op.txt','w')
for m in lis:
    cs=cs+1
    b=m.strip().split(" ")
    
    ans1,ans2=bathroom(int(b[0]),int(b[1]))
    f.write("Case #"+str(cs)+": "+str(ans1)+' '+str(ans2)+'\n')
f.close()
