#!/usr/bin/python

import warnings

def isPalindrome(n):
    s = str(n)
    return s == s[::-1]

def printFairAndSquare(n):
    sqr = n ** 2
    if isPalindrome(str(sqr)):
        print sqr

# just check upto the square root of 10^100 since we are
# looking for a palindrome that squared is less than 10^100
# and is also a palindrome. We only need the first half of that
# number since we are mirroring to only iterate palindromes.
e50d2 = 10 ** 24
# The numbers before 121 were added with a simpler program
# that took too long to run
i = 1
while i <= e50d2:
    strI = str(i)
    l = len(strI)
    n = strI + strI[::-1]
    printFairAndSquare(int(n))
    for j in range(0, 9):
        n = strI + str(j) + strI[::-1]
        printFairAndSquare(int(n))
    i = i + 1
