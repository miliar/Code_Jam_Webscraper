# 1 = 0, i = 1, j= 2, k = 3

positives = [[0,1,2,3],[1,4,3,6],[2,7,4,1],[3,2,5,4]]

mults = [[0 for x in range(8)] for y in range(8)]

translate = { 'i':1,'j':2,'k':3}

invs = [ 0,5,6,7,4,1,2,3]

for i in range(8):
    for j in range(8):
        if i <4:
            if j<4:
                mults[i][j]=positives[i][j]
            else:
                mults[i][j] = (positives[i][j-4]+4)%8
        elif j<4:
            mults[i][j] = (positives[i-4][j]+4)%8
        else:
            mults[i][j] = positives[i-4][j-4]

def check(rep,times):
    if not prodIsOne(rep,times):
        return False
    partials = [translate[c] for c in rep]
    for x in range(1,len(partials)):
        partials[x]=mults[partials[x-1]][partials[x]]
    (got,start,left) = find(1,0,partials,times)
    if not got:
        return False
    extra = times-left
    delta = invs[partials[-1]]
    target = 3
    for qq in range(extra):
        target = mults[target][delta]
    (got2,start2,left2) = find(3,start,partials,left)
    return got2

def find(target,startind,partials,times):
    allowed = partials[startind:]
    if target in allowed:
        return (True, allowed.index(target)+startind,times)
    elif times>0:
        total = allowed[-1]
        newgoal = mults[target][invs[total]]
        if newgoal in partials:
            return (True, partials.index(newgoal),times-1)
        elif times>1:
            newgoal = mults[newgoal][invs[total]]
            if newgoal in partials:
                return (True,partials.index(newgoal),times-2)
            elif times>2:
                newgoal = mults[newgoal][invs[total]]
                if newgoal in partials:
                    return (True,partials.index(newgoal),times-3)
                else:
                    return (False,0,0)
    return (False,0,0)

def prodIsOne(rep,times):
    cur = 0
    for c in rep:
        cur = mults[cur][translate[c]]
    if cur==0:
        return False
    elif cur==4:
        return (times%2)==1
    else:
        return (times%4)==2

def dofile(name):
    f = open(name)
    out = open('dijksol.txt','w+')
    num = int(f.readline())
    for q in range(num):
       vals= map(int,f.readline().split())
       base = f.readline()[:-1]
       if check(base,vals[1]):
           out.write("Case #"+str(q+1)+": YES\n")
       else:
            out.write("Case #"+str(q+1)+": NO\n")
