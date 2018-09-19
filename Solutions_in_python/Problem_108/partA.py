import math

def recJungle(vineHeld,placeHeld,vines,end):
    global known
    currentTag=str(vineHeld)
    if known.has_key(currentTag):
        if placeHeld<=known[currentTag][0]:
            return known[currentTag][1]
    
    startIndex=vineHeld+1
    currentLocation=vines[vineHeld][0]
    if currentLocation+placeHeld>=end:
        return "YES"

    if vineHeld==len(vines)-1:
        return "NO"
    for endIndex in range(startIndex,len(vines)):
        if vines[endIndex][0]>currentLocation+placeHeld:
            break
        else:
            if endIndex==len(vines)-1:
                endIndex+=1
    if startIndex==endIndex:
        return "NO"

    for vine in range(startIndex,endIndex):
        horizontalDistance=vines[vine][0]-currentLocation
        grabPoint=horizontalDistance
        if grabPoint>vines[vine][1]:
            grabPoint=vines[vine][1]

        answer=recJungle(vine,grabPoint,vines,end)
        if answer=="YES":
            return answer
    known[currentTag]=[placeHeld,"NO"]
    return "NO"

def jungle(vines,end):
    return recJungle(0,vines[0][0],vines,end)
    

X=open("test3.in")
z=open("output.txt","w")
case=0
currentline=X.readline()
currentline=X.readline().rstrip().lstrip()
while currentline:
    case+=1
    print case
    vines=int(currentline)
    vineList=[]
    while vines:
        vines-=1
        vineList.append(map(int,X.readline().rstrip().lstrip().split()))
    known={}
    final=int(X.readline())
    z.write("Case #"+str(case)+": "+jungle(vineList,final)+"\n")
    currentline=X.readline().rstrip().lstrip()
z.close()
