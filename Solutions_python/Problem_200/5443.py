import sys

def isTidyNumber(number):
    number = str(number)
    previousDigit = 0
    for digit in number:
        digit = int(digit)
        if (digit < previousDigit):
            return False
        previousDigit = digit
    return True

def findTidyNumberLessThanEqualTo(number):
    number = int(number)
    while(isTidyNumber(number) is False):
        number -= 1
    return number

cases = int(input())

for i in range(cases):
    upper = input()
    print("Case #" + str(i + 1) + ":", findTidyNumberLessThanEqualTo(upper))
