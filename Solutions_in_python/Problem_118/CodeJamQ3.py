# Brendan Wreford
import os
import math

# Create Output file
f = open('output.txt', "w")
f.close()

def is_palindrome(s):
    return all(s[i] == s[-(i + 1)] for i in range(len(s)/2))

def number_palindrome(n):
    return is_palindrome(str(n))

# Read Input file
f = open('C-small-attempt0.in', "rb")
numOfTestCases = f.readline()
numOfTestCases = int(numOfTestCases)

g = open('output.txt', "a")

for i in range(0,numOfTestCases):
    case = f.readline()
    case = case.split()
    Lower = int(case[0])
    Upper = int(case[1])

    Lower = int(math.ceil(Lower**0.5))
    Upper = int(Upper**0.5)
    
    counter = 0
    for j in range(Lower,Upper+1):
        if number_palindrome(j):
            if number_palindrome(j**2):
                counter = counter+1
    g.write("Case #" + repr(i+1) + ": " + repr(counter) + "\n")
