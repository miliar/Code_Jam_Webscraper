def isTidyNumber(number):
    listNum = list(str(number))
    listNum = [int(x) for x in listNum]
    isTidy = True
    for i in range(1, len(listNum)):
        if listNum[i] < listNum[i-1]:
            isTidy = False
    return isTidy

def lastTidyNumber(number):
    listNum = list(str(number))
    listNum = [int(x) for x in listNum]
    numberOfNines = 0
    for i in range(1, len(listNum)):
        if listNum[i] < listNum[i-1]:
            listNum[i] = 9
            listNum[i-1] = listNum[i-1] - 1
            numberOfNines = len(listNum) - i - 1
            listNum = listNum[:i+1]
            break
    tidyNumStr = ""
    for j in listNum:
        tidyNumStr += str(j)
    tidyNumStr += numberOfNines * "9"
    tidyNumStr = tidyNumStr.strip("0")
    return tidyNumStr

'''
numberTestCase = int(input())
resultList = []
for i in range(numberTestCase):
    resultList.append(int(input()))
for j in range(numberTestCase):
    while not isTidyNumber(resultList[j]):
        resultList[j] = lastTidyNumber(resultList[j])
    print("Case #" + str(j+1) + ": " + lastTidyNumber(resultList[j]))
'''

file = open("B-large.in")
output = open("Output File.txt", "w")
numberTestCase = int(file.readline())
resultList = []
for i in range(numberTestCase):
    resultList.append(int(file.readline()))
for j in range(numberTestCase):
    while not isTidyNumber(resultList[j]):
        resultList[j] = lastTidyNumber(resultList[j])
    output.write("Case #" + str(j+1) + ": " + lastTidyNumber(resultList[j]) + "\n")

file.close()
output.close()
