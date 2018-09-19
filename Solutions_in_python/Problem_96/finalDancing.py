#Jaime Marquinez

inputFile=open("B-large.in.txt",'r')
outputFile=open("B-large.out.txt",'w') 

def isPossibleWithNoSurprise(suma,n):
    return ((suma>=3*n-1)or(suma>=3*n-2)or(suma>=3*n))

def isPossibleWithSurprise(suma,n):
    condition1 = (suma >= 3*n - 3) or (suma >= 3*n - 2) or (suma >= 3*n - 4)
    condition2 = (n - 1 >= 0) and (n - 2 >=0) and (n >= 0)
    return (condition1 and condition2)

def evalCase(case):
    maxPos = 0
    dataSet=inputFile.readline().split()
    long=len(dataSet)
    i=0
    while i<long:
        dataSet[i]=int(dataSet[i])
        i += 1
    nGooglers = dataSet.pop(0)
    nSurprises = dataSet.pop(0)
    targetScore = dataSet.pop(0)
    totalPoints = dataSet
    for suma in totalPoints:
        if isPossibleWithNoSurprise(suma,targetScore):
            maxPos += 1
        elif isPossibleWithSurprise(suma,targetScore) and nSurprises>0:
            nSurprises -= 1
            maxPos += 1
    outputFile.write('Case #'+str(case)+': '+str(maxPos)+'\n')

def main():
    nCases = int(inputFile.readline())
    i = 1
    while i <= nCases:
        evalCase(i)
        i += 1
    
main()
inputFile.close()
outputFile.close()

