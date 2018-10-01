import math

def getClosestGreater(theList,point):
    answer=100000000000
    for each in theList:
        if each>point and each < answer:
            answer=each
    if answer<100000000000:
        return answer
    return -1
def war(naomi,ken):
    points=0
    naomi.sort()
    ken.sort()
    while (len(naomi)>0):
        rock=naomi[-1]
        naomi.remove(rock)
        close=getClosestGreater(ken,rock)
        if close==-1:
            kenRock=ken[0]
        else:
            kenRock=close
        ken.remove(kenRock)
        if rock>kenRock:
            points+=1
    return points
def deceit(naomi,ken):
    points=0
    naomi.sort()
    ken.sort()
    while (len(naomi)>0):
        close=getClosestGreater(naomi,ken[0])
        if close==-1:
            naomiRock=naomi[0]
            kenRock=ken[-1]
        else:
            naomiRock=close
            kenRock=ken[0]
        if naomiRock>kenRock:
            points+=1
        ken.remove(kenRock)
        naomi.remove(naomiRock)
    return points
            
def copyList(l):
    newList=[]
    for each in l:
        newList.append(each)
    return newList

X=open("dlg.in")
z=open("output.txt","w")
case=0
cases=int(X.readline())
line=X.readline().split()
while case<cases:
    case+=1
    print case
    naomi=X.readline().split()
    ken=X.readline().split()
    for index in range(0,len(naomi)):
        naomi[index]=float(naomi[index])
        ken[index]=float(ken[index])
    z.write("Case #"+str(case)+": "+str(deceit(copyList(naomi),copyList(ken)))+" "+str(war(naomi,ken))+"\n")
    line=X.readline().split()
z.close()
