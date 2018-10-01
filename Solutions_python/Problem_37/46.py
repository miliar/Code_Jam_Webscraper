def getAllNum(i,r):
    ret=[]
    while i!=0:
        if (i%r)!=0:
            ret.append(i%r)
        i=int(i/r)
    ret.sort()
    return ret
    
def ishappy(mset,r,retset):
    sum=0
    if mset==None or len(mset)==0:
        return False
    for num in mset:
        sum+=num*num
    if sum==1:
        return True
    newset=getAllNum(sum,r)
    if retset.count(newset)>0:
        return False
    retset.append(newset)
    return ishappy(newset,r,retset)
    
T=int(raw_input())
for t in range(T):
    case= raw_input().split()
    icase=[]
    num=2
    retset=[]
    while True:
        flag=True
        for c in case:
            myset=getAllNum(num,int(c))
            retset=[]
            if not ishappy(myset,int(c),retset):
                flag=False
                break
        if flag:
            print "Case #%d: %d"%(t+1,num)
            break
        num+=1