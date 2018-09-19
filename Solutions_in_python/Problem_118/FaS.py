#   CodeJam 2013
#   Nick: mnganesh
#   Description: Problem C. Fair and Square

__author__ = 'Ganesh'

import fileIO
import math

ifileName = "i.txt"
ofileName = "3AOutput.txt"

def getInputsArray(iFDump):
    nCases = int(iFDump[0])
    inputArr = []
    for i in xrange(nCases):
        inputArr.append(map(int,iFDump[i+1].split()))
    return inputArr


def main():
    ifDump = fileIO.readFile(ifileName)
    inputArr = getInputsArray(ifDump)
    solArr = []
    for input in inputArr:
        solArr.append(FAS(input).count())

    fileIO.outFile(ofileName,solArr)

class FAS:
    def __init__(self,inp):
        start,end = inp
        self.__start = int(math.ceil(math.sqrt(start)))
        self.__end = int(math.floor(math.sqrt(end)))
        # print self.__start,self.__end

    def count(self):
        counter = 0
        for i in xrange(self.__start, self.__end+1):
            # print i
            if self.__isPalindrome(str(i)):
                square = i*i
                # print i,square
                if self.__isPalindrome(str(square)):
                    counter+=1
        return counter


    def __isPalindrome(self,x):
        return all(x[a]==x[-a-1] for a in xrange(len(x)>>1))

if __name__== '__main__':
    main()