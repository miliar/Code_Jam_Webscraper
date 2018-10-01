#!/usr/bin/python -tt

import sys

def main():
    inFile = open(sys.argv[1], 'rU')
    outFile = open(sys.argv[2], 'w')
    aLine = inFile.readline()
    T = eval(aLine)
    for case in range(T):
        aLine = inFile.readline()
        C = eval(aLine)
        aLine = inFile.readline()
        aLine = aLine.split()
        for i in range(C):
            aLine[i] = eval(aLine[i])
        candy = aLine
        OK = 0
        for i in candy:
            OK = OK^i
        if OK:
            outFile.write("Case #%d: NO\n" %(case+1))
        else:    
            outFile.write("Case #%d: %d\n" %(case+1, sum(candy) - min(candy)))

    inFile.close()
    outFile.close()


if __name__ == '__main__':
    main()
