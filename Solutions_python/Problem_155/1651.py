fname = "A-large.in"

def sumPrevPpl(listOfCrap, indice):
    totalSum = 0
    for thing in range(indice):
        if(totalSum >= thing):
            totalSum += int(listOfCrap[thing])
    return(totalSum)
        
with open(fname) as f:
    content = f.readlines()
    N = int(content[0])
    content.pop(0)
    for caseNo in range(0,N):
        #eachCase if they stand up then you add
        stuffInside = content[caseNo].split()
        nShynessLvl = int(stuffInside[0])
        eachNumber = list(stuffInside[1])
        toPrint = "Case #"+str(caseNo+1)+": "
        
        solved = False
        howManyRequired = 0
        while(not solved):
            if(sumPrevPpl(eachNumber,nShynessLvl) >= nShynessLvl):
                solved = True
            else:
                eachNumber[0] = int(eachNumber[0]) + 1
                howManyRequired += 1
        toPrint += str(howManyRequired)
        print(toPrint)