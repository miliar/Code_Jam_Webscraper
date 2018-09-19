import copy
inFile = open("C:\\Users\\Eric\\Downloads\\infile.in", "r")
outFile = open("C:\\Users\\Eric\\Downloads\\outfile.out", "w")
inString = inFile.readline()
numOfTestCase = int(inString)

mapping = [['1', 'i', 'j', 'k', '-1'], ['i', '-1', 'k', '-j', '-1'], ['j', '-k', '-1', 'i', '-j'],
           ['k', 'j', '-i', '-1', '-k'], ['-1', '-i', '-j', '-k', '1']]
index = ['1', 'i', 'j', 'k', '-1']

def mapFunc(a, b):
    neg = (a.count('-') % 2) * '-'
    if a.count('-') == 1:
        a = a[1:]
    if a.count('-') == 2:
        a = a[2:]

    result = neg + mapping[index.index(a)][index.index(b)]
    if result.count('-') == 2:
        result = result[2:]
    return result

for i in range(numOfTestCase):
    numChar, multi = inFile.readline()[:-1].split(' ')
    multi = int(multi)
    inputString = inFile.readline()[:-1] * multi
    resultList = list(inputString)
    inputList = list(inputString)
    tmpResult = ''
    result = ''
    #print(inputString)
    for j in resultList:
        if tmpResult == '':
            tmpResult = j
        else:
            tmpResult = mapFunc(tmpResult, j)
        del inputList[0]
        if tmpResult == 'i':
            result += 'i'
            break
    
    tmpResult = ''
    resultList = copy.deepcopy(inputList)
    for j in resultList:
        if tmpResult == '':
            tmpResult = j
        else:
            tmpResult = mapFunc(tmpResult, j)
        del inputList[0]
        if tmpResult == 'j':
            result += 'j'
            break
    tmpResult = ''
    resultList = copy.deepcopy(inputList)
    for j in resultList:
        if tmpResult == '':
            tmpResult = j
        else:
            tmpResult = mapFunc(tmpResult, j)
        del inputList[0]
        if tmpResult == 'k':
            result += 'k'
            break
    tmpResult = ''
    resultList = copy.deepcopy(inputList)
    for j in resultList:
        if tmpResult == '':
            tmpResult = j
        else:
            tmpResult = mapFunc(tmpResult, j)
        del inputList[0]
        if len(inputList) == 0:
            result += tmpResult
            break
    print("Result:", result)
    if result == "ijk1":
        outFile.write("Case #"+str(i+1)+": "+"YES" + '\n')
    elif len(resultList) == 0 and result == "ijk":
        outFile.write("Case #"+str(i+1)+": "+"YES" + '\n')
    else:
        outFile.write("Case #"+str(i+1)+": "+"NO" + '\n')
            
outFile.close()
inFile.close()
