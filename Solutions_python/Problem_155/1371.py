data = []
fr = open('a.txt')
count = 1
for line in fr.readlines()[1:]:

    curLine = line.strip().split(' ')
    data = map(int,curLine[1])
    sumData = 0
    result = 0
    for i in range(len(data)):
        if sumData >= i:
            sumData = sumData + data[i]
        else:
            result = result + i - sumData
            sumData = i + data[i]
        
    print 'Case #' + str(count)+': '+str(result)
#    print data
    count = count + 1
    data = []
        
fr.close()