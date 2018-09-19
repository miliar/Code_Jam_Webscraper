'''
Created on May 7, 2010

@author: randy
'''

from Snapper import *

def main():
    file = raw_input("Please type in the file name: ")
    input = open(file)       # find nicer way to read a file 
    caseNum = eval(input.next())
    f = open('result.out', "w")
    for a in range(caseNum):
        n, k = input.next().split()
        snapper = Snapper(n, k)          # list of input map with altitude
        printResult(f, a+1, snapper.run())
    input.close()


def printResult(f, caseNum, result):
    answer ={ True : 'ON',
            False : 'OFF'
            }[result]
    print >>f, 'Case #%d: ' %caseNum, answer

if __name__ == '__main__':
    main()
    