import math

def isPalindrome(strNum):
    if ( len(strNum) == 1 ):
        return True
    else:
        end = len(strNum) - 1
        mid = len(strNum) / 2
        for i in range(0, mid):
            if strNum[i] == strNum[end - i]:
                continue
            else:
                return False
        
        return True
    
def isSquareOfPalindrome(num):
    sqr = math.sqrt(num)
    if math.floor(sqr) == sqr:
        if isPalindrome(str(int(sqr))):
            return True
        else:
            return False
    else:
        return False
    
def isFairAndSquare(strNum):
    if isPalindrome(strNum) and isSquareOfPalindrome(float(strNum)):
        return True
    else:
        return False
