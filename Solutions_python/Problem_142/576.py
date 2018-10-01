import numpy

def importData(inputFileName):
    data = [i.strip() for i in open(inputFileName).readlines()]
    data = [x.split() for x in data]
    caseCount=int(data.pop(0)[0])   
    return data

def is_int(s):
        try:
            int(s[0])
            return True
        except ValueError:
            return False

def splitData(data):
    test=map(is_int, data)
    cases=[]
    while len(data) >0:
        case=[]
        isNum=False
        while not isNum:
            isNum=test.pop()
            case.append(data.pop())
        cases.append(case[::-1])
    return cases[::-1]

def in_order_tally(s):
    # counts the number of consecutive runs of elements
    strChars=[s[0]]
    tally=[0]
    for char in s:
        if char==strChars[-1]:
            tally[-1]+=1
        else:
            strChars.append(char)
            tally.append(1)
    return (strChars, tally)

def all_same(items):
    return all(x == items[0] for x in items)

def processCase(case):
    stringCount=case.pop(0)[0]
    strings=map(lambda x: x[0], case)
    tally_result=map(in_order_tally, strings)
    if not all_same([x[0] for x in tally_result]):
        return 'Fegla Won'
    else:
        counts=[x[1] for x in tally_result]
        return str(sum([int(sum(abs(x-round(numpy.mean(x))))) for x in numpy.transpose(counts)]))
    

def exportOutput(inputFileName):
    cases=splitData(importData(inputFileName))
    output='\n'.join(['Case #'+str(caseID+1)+': '+processCase(case) for (caseID, case) in enumerate(cases)])
    outputFileName=inputFileName.replace('.in','-output.txt')
    f=open(outputFileName, 'wb')
    f.write('')
    f.writelines(output)
    f.close()
