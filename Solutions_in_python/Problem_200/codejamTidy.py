def readFile(flname):
    lines = open(flname).read().split("\n")
    outputfl = open("output.txt","w")
    testAmount = int(lines[0])
    for i in range(1,len(lines)-1):
        curTest = lines[i]
        curAns = solveSpecificRow(int(curTest))
        outputfl.write("Case #"+str(i)+": "+str(curAns)+"\n")
    outputfl.close()
def fillNines(digits,i,lngth):
    for j in range(i+1,lngth):
        digits[j]=9
def solveSpecificRow(n):
    digits = [int(x) for x in list(str(n))]
    ansInDigs = solveSpecificRowWithDigits(digits,len(digits))
    return int("".join([str(x) for x in ansInDigs]))
def solveSpecificRowWithDigits(digits,lngth):
    if len(digits)==1:
        return digits
    ##assumes we change last digit too
    for i in range(lngth-1):
        if digits[i]>digits[i+1]:
            digits[i]=digits[i]-1
            newNum = solveSpecificRowWithDigits(digits,i+1)
            fillNines(digits,i,lngth)
            break
    return digits
