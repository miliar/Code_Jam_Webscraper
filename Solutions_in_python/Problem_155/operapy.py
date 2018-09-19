__author__ = 'roohy'

FILE = open("test.txt", 'r')
output = open("result.txt",'w')
Testnumber = int(FILE.readline())
for i in range(0,Testnumber):
    line = FILE.readline()
    set = line.split(' ')
    levels = int(set[0])
    if set[1][-1] == '\n':
        levelList = list(set[1][:-1])
    else:
        levelList = list(set[1])
    minGuest = 0
    cheeringNumber = 0
    levelList = [int(x) for x in levelList]
    print("list is ",levelList)
    for j in range(0,len(levelList)):
        if cheeringNumber+minGuest < j:
            minGuest += j-cheeringNumber-minGuest

        cheeringNumber+=levelList[j]
    output.write("Case #"+str(i+1)+": "+str(minGuest)+'\n')
output.close()
FILE.close()