from io import *
from math import *

def isPalindrome(i):
    i = str(i)
    for j in range(int(len(i)/2)):
        if(i[j] != i[len(i)-j-1]):
            return False
    return True

def runFile(file):
    f = open(file)
    g = open("output"+file,'w')
    num = int(f.readline().rstrip('\n'))
    for i in range(num):
        count = 0
        line = str.split(f.readline().rstrip('\n'))
        sBound = ceil(int(line[0])**.5)
        lBound = int(int(line[1])**.5)
        for j in range(sBound,lBound+1):
            if(not isPalindrome(j)):
                continue
            if(isPalindrome(j**2)):
                count += 1
        g.write("Case #" + str(i+1) + ": " + str(count)+ "\n")
