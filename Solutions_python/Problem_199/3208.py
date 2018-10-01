
def getNumberOfIternationForLineBeginningWithMinus(listOfPlusMinus, numberOfCookies, numberOfLastIterations):
    listOfPlusMinus = getListFromFirstMinus(listOfPlusMinus)
    lengthOfLine = len(listOfPlusMinus)
    if lengthOfLine == 0:
        return numberOfLastIterations
    elif lengthOfLine < numberOfCookies:
        return 'IMPOSSIBLE'
    else:
        newListOfCookies = upsideDownForList(listOfPlusMinus, numberOfCookies)
        newListOfCookiesFromFirstMinus = getListFromFirstMinus(newListOfCookies)
        return getNumberOfIternationForLineBeginningWithMinus(newListOfCookiesFromFirstMinus, numberOfCookies, numberOfLastIterations+1)

def getListFromFirstMinus(listOfPlusMinus):
    result = []
    isFirstMinusPassed = False
    for element in listOfPlusMinus:
        if isFirstMinusPassed:
            result.append(element)
        else:
            if element == '-':
                isFirstMinusPassed = True
                result.append(element)
    return result

def upsideDownForList(listOfPlusMinus, numberOfCookies):
    result = []
    for index, plusOrMinus in enumerate(listOfPlusMinus):
        if index < numberOfCookies:
            result.append(inversePlusMinus(plusOrMinus))
        else:
            result.append(plusOrMinus)
    return result

def inversePlusMinus(plusOrMinus):
    if plusOrMinus == '-':
        return '+'
    else:
        return '-'


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    listOfPlusMinus, m = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
    listOfPlusMinus = list(listOfPlusMinus)
    m = int(m)
    print("Case #{}: {}".format(i, getNumberOfIternationForLineBeginningWithMinus(listOfPlusMinus, m, 0)))
  # check out .format's specification for more formatting options
