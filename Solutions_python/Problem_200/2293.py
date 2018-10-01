import sys

def subOneBigNum(n, i):
    listN = [int(d) for d in str(n)]
    if listN[-i] != 0:
        listN[-i] -= 1
        n = int(''.join(str(e) for e in listN))
    else:
        for k in range(1,i+1):
            listN[-k] = 9
        n = subOneBigNum(int(str(''.join(str(e) for e in listN))), i+1)

    return n

def answer(inputs):
    n = int(inputs[0])
    
    ans = False

    while not ans:
        prevNum = 0
        ans = True
        nList = [int(d) for d in str(n)]
        for i, num in enumerate(nList):
            if num < prevNum:
                n = subOneBigNum(n, len(nList) - i)
                ans = False
                break
            prevNum = num
    
    return str(n)


filename = input("Enter filename: ")

with open(filename, 'r') as inputFile:
    with open(filename + '_out.o', 'w') as outputFile:
        sys.stdout = outputFile
        testCaseNum = int(inputFile.readline().replace('\n',''))

        for i in range(1, testCaseNum + 1):
            inputs = (inputFile.readline().replace('\n','')).split(' ')
            ans = answer(inputs)
            print("Case #" + str(i) + ": " + ans)
