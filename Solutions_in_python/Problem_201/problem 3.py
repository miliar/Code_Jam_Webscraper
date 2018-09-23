from math import log
from bisect import bisect
from time import time



def generate(M):#generate the Mth lowest solution
    return (M/2,(M-1)/2)
    

def finalMMpattern(N,K):
    
    l=2**int(log(K,2))#power of 2 lower than K
    #h=l*2

    lowerBound=N/l
    if l==K:
        return generate(lowerBound)
    #higherBound=N/h

    if N<=(lowerBound+1)*l-2:
        a=lowerBound*l-1
        other=l+(N-a)
        if K>=other:
            return generate(lowerBound-1)

    return generate(lowerBound)



t=time()

f=open("prob3small2.txt","r")
T=int(f.readline())

ans=[]
for line in f:
    l=line.split(' ')
    N=int(l[0])
    K=int(l[1])
    r=finalMMpattern(N,K)

    ans.append(r)

f.close()

b=open("ans3small2.txt","w")
for i in xrange(len(ans)):
    b.write("Case #"+str(i+1)+": "+str(ans[i][0])+" "+str(ans[i][1])+"\n")


b.close()
print time()-t

