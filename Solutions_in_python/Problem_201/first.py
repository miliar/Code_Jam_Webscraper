import numpy as np

def check(ls,rs):
    final=0
    arr=np.vstack((ls,rs)).T
    minind=[]
    maxind=[]
    maxi=[]
    for x in arr:
        minind.append(min(x))
    ma=max(minind)    
    malist=[i for i, j in enumerate(minind) if j == ma]
    if(len(malist)==1):
        return malist[0]
    else:
        for x in arr[malist]:
            maxi.append(max(x))
        mi=max(maxi)
        for x in arr:
            maxind.append(max(x))
        milist=[i for i, j in enumerate(maxind) if j == mi]
    flag=0
    if(len(milist)==1):
        return milist[0]
    else:        
        for x in malist:
            for y in milist:
                if(x==y):
                    final=x
                    flag=-1
                    break
            if(flag==-1):
                break
            
    return final
    
def fill(ls,rs,final):
    ls[final]=-1
    rs[final]=-1
    le=len(ls)
    count=0
    count1=0
    
    for x,y in zip(range(le),reversed(range(le))):
        if(ls[x]==-1):
            count=0
        else:
            ls[x]=count
            count=count+1
            
        if(rs[y]==-1):
            count1=0
        else:
            rs[y]=count1
            count1=count1+1 
    return ls,rs
    
with open('test.txt','r') as f:
    line=(f.read().splitlines())
 #   int(line[0])+1
one=[]
two=[]
final=0
for x in range(1,int(line[0])+1):
    n=int(line[x].split(' ')[0])
    k=int(line[x].split(' ')[1])
    if(k==n):
        one.append(0)
        two.append(0)
    else:
        ls=np.arange(n)
        rs=n-1-np.arange(n)
        for y in range(k-1):
            final=(check(ls,rs)) 
            ls,rs=fill(ls,rs,final)
        final=(check(ls,rs)) 
        te=[ls[final],rs[final]]
        one.append(max(te))
        two.append(min(te))
    
with open('final.txt','w') as fi:
    for x in range(int(line[0])):
        fi.write('Case #'+str(x+1)+': '+str(one[x])+' '+str(two[x])+'\n')
