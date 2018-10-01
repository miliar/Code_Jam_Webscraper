from math import sqrt

def isPalindrome(inputInt):
    inputString = str(inputInt)
    letters = [c for c in inputString.lower()]
    return (letters == letters[::-1])

def isSquare(n):
    squareRootN = sqrt(n)
    if squareRootN.is_integer():
        if isPalindrome(int(squareRootN)):
            return True
    return False


numOfTests = int(input())
for j in range(1, numOfTests+1):
    inputString = input().split()
    a = int(inputString[0])
    b = int(inputString[1])
    count = 0
    for i in range(a,b+1):
        if isPalindrome(i) and isSquare(i):
            count = count + 1
            
    print("Case #%d: %d" % (j, count))