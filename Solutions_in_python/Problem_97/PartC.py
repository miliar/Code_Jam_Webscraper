def binarySearch(start,end,searchList,item):
    if start>end:
        return False
    if start==end:
        if searchList[start]!=item:
            return False
        return start
    mid=(end+start)/2
    if item==searchList[mid]:
        return mid
    elif item>searchList[mid]:
        return binarySearch(mid+1,end,searchList,item)
    return binarySearch(start,mid-1,searchList,item)

def permuteRotations(number):
    number=str(number)
    answers=[]
    for index in range(len(number)-1,0,-1):
        answers.append(number[index:]+number[0:index])
    return list(set(map(int,answers)))

def numberRotations(A,B):
    if len(str(A))<2:
        return "0"
    numbers=range(A,B+1)
    answer=0
    for current in numbers:
        curRotations=permuteRotations(current)
        for each in curRotations:
            if each>current:
                if each in numbers:
                    answer=answer+1
                
    return str(answer)

print numberRotations(1111,2222)

x=open("test6.in")
z=open("output.txt","w")

case=0
currentline=x.readline()

currentline=x.readline().rstrip().lstrip().split()
while currentline:
    case=case+1
    print case
    a=int(currentline[0])
    b=int(currentline[1])
    z.write("Case #"+str(case)+": "+numberRotations(a,b)+"\n")
    currentline=x.readline().rstrip().lstrip().split()
z.close()

