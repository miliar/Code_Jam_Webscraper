def parse(a):
    down=0
    up=0
    for i in range(1,len(a)):
        if a[i]>a[i-1]:
            up=i
        if a[i]<a[i-1]:
            down=i
            break
    if down ==0:
        return a
    elif up==0 and a[0]=='1':
        return '9'*(len(a)-1)
    else:
        return a[:up]+str(int(a[up])-1)+'9'*(len(a)-1-up)
#N=int(input())
#for c in range(1,N+1):
#   a=input()
#   print("Case #{}: {}".format(c,parse(a)))

    
import math


def sol(N,K):
    cp2=pow(2,int(math.log(K,2)))
    divi=(N-cp2+1)//cp2
    modu=(N-cp2+1)%cp2
    if K-cp2+1 <=modu:
        L= ((divi+1+1)//2)-1
        R= divi+1-L-1
    else:
        L= ((divi+1)//2)-1
        R= divi-L-1
        
    return (max(L,R),min(L,R))
#T=int(input())
#for c in range(1,T+1):
#    n,m=[int(s) for s in input().split(" ")]
#    n,m=sol(n,m)
#    print("Case #{}: {} {}".format(c,n,m))
    



def suc(s,k,i):
    #print('lol'+str(i)+"    "+s)
    if s in d and d[s][0]==1:
        if d[s][1]>i:
            d[s][1]=i
        return
    else:
        if s in d and d[s][1]<=i:
            return
        else:
            d[s]=[1,i]
        for j in range(len(s)-k+1):
            suc(s[:j]+s[j:j+k].replace('+','m').replace('-','+').replace('m','-')+s[j+k:],k,i+1)
        d[s][0]=0
    return

T=int(input())
for c in range(1,T+1):
    a=input().split(" ")
    s=a[0]
    k=int(a[1])
    wanted = '+'*len(s)
    d={}
    suc(s,k,0)
    if wanted in d:
        print("Case #{}: {}".format(c,d[wanted][1]))
    else:
        print("Case #{}: IMPOSSIBLE".format(c))

        
#def solve(k):
 #   if k == 0 return 'NOT POSSIBLE'
    
