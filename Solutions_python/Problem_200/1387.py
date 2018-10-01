inputFile = open("B-large(1).in",'r')
outputFile = open("output.out",'w')
testCases = int(inputFile.readline())

for testCase in range(1,testCases+1):
    N = int(inputFile.readline())
    if N <= 20:
        if N == 20 or N==10:
            tidyNumber = N-1
        else:
            tidyNumber = N
    else:
        number = N
        isTidy = False
        if number%10 ==0:
            number-=1
        digitList = list(map(int,str(number)))
        listLength = digitList.__len__()
        #make tidy
        index = 1
        while index < listLength:
            if digitList[index-1]>digitList[index]:
                digitList[index-1]-=1
                for i in range(index,listLength):
                    digitList[i]=9
                index = 0
            index+=1
        tidyNumber = int(''.join(list(map(str,digitList))))
    print("Case #" + str(testCase) + ": " + str(tidyNumber)+" "+str(N))
    outputFile.write("Case #" + str(testCase) + ": " + str(tidyNumber) + "\n")
outputFile.close()
