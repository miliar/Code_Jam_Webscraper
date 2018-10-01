#!/usr/bin/python3
# B_tidy_numbers.py
#
# Last Updated: 2017.04.08
# Jun Go gojun077@gmail.com
#
# GCJ 2017 QR Tidy Numbers
# https://code.google.com/codejam/contest/3264486/dashboard#s=p1


def isTidy(mystr):
    """
    str -> Boolean

    Given a str 'myint', return 'True' if each digit is greater than
    or equal to the previous digit going from left-to-right.

    Return 'False' otw

    >>> isTidy('129')
    True
    >>> isTidy('7')
    True
    >>> isTidy('100')
    False
    """
    for char_index in range(len(mystr) - 1):
        if mystr[char_index] > mystr[char_index + 1]:
            return False
    return True


def maxTidy(mystr):
    """
    str -> str

    Given an integer string 'mystr', return a tidy integer string
    that is as close as possible to 'mystr'. The algorithm to use
    is as follows:

    (1) Convert 'mystr' to ListOfInt, i.e. '1110' -> [1, 1, 1, 0]
    (2) Starting from second digit (i.e. index 1), if the current digit
        is less than the previous digit, subtract 1 from the previous
        digit and change all the remaining digits to '9'

        [1, 1, 1, 0] -> [1, 1, 0, 9] -> [1, 0, 9, 9] -> [0, 9, 9, 9]

    (3) Convert ListOfInt to string and remove all zeroes

    (4) Return answer str

    >>> maxTidy('132')
    '129'

    >>> maxTidy('7')
    '7'

    >>> maxTidy('1110')
    '999'
    """
    tidyFlag = isTidy(mystr)

    while not tidyFlag:
        numarray = [int(char) for char in mystr]

        for i in range(1, len(numarray)):
            if numarray[i] < numarray[i - 1]:
                numarray[i - 1] -= 1
                for j in range(i, len(numarray)):
                    numarray[j] = 9
                break
        # convert to 'str' type
        numarray = [str(x) for x in numarray]
        # convert list to str
        mystr = ''.join(numarray)
        # remove leading zeroes from string
        mystr = mystr.lstrip('0')
        tidyFlag = isTidy(mystr)

    return mystr


# MAIN PROGRAM
if __name__ == '__main__':
    import doctest
    doctest.testmod()

caseL = []
num_cases = int(input())
for i in range(num_cases):
    caseL.append(input())

case_num = 1
for j in caseL:
    ans = maxTidy(j)
    print("Case #%d: %s" % (case_num, ans))
    case_num += 1
