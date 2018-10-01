import string
#print 'Hello World'
input = open ('C-small-attempt0.in')
output = open ('C-small-attempt0.out','w+')
line = input.readline()
line = string.atoi(line)
for i in range(1,line+1):
    data1 = input.readline()
    data2 = input.readline()
    data1 = data1.split(' ')
    data2 = data2.split(' ')
    R = string.atoi(data1[0])
    K = string.atoi(data1[1])
    N = string.atoi(data1[2])
    
    arrayList = []    
    
    for j in range(0,N):
        arrayList.append(string.atoi(data2[j]))
    
    M = 0
    
    for r in range(1,R+1):
        k = arrayList[0]
#        print arrayList
        tempList = []
        tempList.append(arrayList[0])
        del arrayList[0]
#        arrayList.append(temp)
        while (k<=K):
            if (len(arrayList) != 0):
                k = k + arrayList[0]
#                print k
                if (k>K):
                    k = k - arrayList[0]
                    arrayList.extend(tempList)
                    break
                else :
                    tempList.append(arrayList[0])
                    del arrayList[0]
            else:
                arrayList.extend(tempList)
                break
        M = M+k
#        print k
#    print M
    output.write("Case #%d: %d\n" %(i,M))
input.close()
output.close()
