import sys

ifs = file("input.txt")
ofs = file("output.txt", "w")

def ReadInts(input = ifs):
  return list(map(int, input.readline().strip().split(" ")))

def GetMatrix(rows, cols, value=0):
    return [[value for i in range(rows)] for j in range(cols)]

def getNext(num):
    num = str(num)
    num = list(map(int, num))
    last = len(num)-1
    index = last-1
    while index >= 0:
        if num[index] < num[index+1]:
            break
        index -= 1
    
    if (index >= 0):
        index2 = last
        while(num[index2] <= num[index]):
            index2-=1
        num[index], num[index2] = num[index2], num[index]
        templist = num[index+1:]
        templist.sort()
        num[index+1:]=templist
    else:
        num.append(0)
        index = -1
        for q in range(1,10):
            if q in num:
                index = num.index(q)
                break
        num[0],num[index] = num[index],num[0]
        templist = num[1:]
        templist.sort()
        num[1:] = templist
    num = list(map(str, num))
    num = "".join(num)
    return int(num)
        
    

caseNo = ReadInts()[0]
for case in range(1, caseNo+1):
    ivalue = ReadInts()[0]
    result = getNext(ivalue)
    print  >> ofs, "Case #%d:" % case, result 

    



ifs.close()
ofs.close()



