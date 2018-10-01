
FILE = open("B-large.in","r")
OUTPUT = open("B-large.out","w")

cases = FILE.readline()

for i in range(0,int(cases)):
    temp = FILE.readline().split(" ")
    n = int(temp[0])
    k = int(temp[1])
    b = int(temp[2])
    t = int(temp[3])
    chickenX = FILE.readline().rstrip('\n').split(" ")
    chickenV = FILE.readline().rstrip('\n').split(" ")
    chickenList = []
    for j in range(0,n):
        chickenList.append([int(chickenX[j]),int(chickenV[j])])
    makeIt = 0
    notMakeIt = 0
    scoops = 0
    for j in range(0,n):
       if makeIt < k:
           if b <= chickenList[n-j-1][0] + chickenList[n-j-1][1]*t:
               makeIt +=1
               scoops += notMakeIt
           else:
               notMakeIt += 1
   
    writeLine = "Case #" + str(i+1) + ": "
    if makeIt < k:
        writeLine = writeLine + 'IMPOSSIBLE\n'
    else:
        writeLine = writeLine + str(scoops) + '\n'
    OUTPUT.write(writeLine)

FILE.close()
OUTPUT.close()

