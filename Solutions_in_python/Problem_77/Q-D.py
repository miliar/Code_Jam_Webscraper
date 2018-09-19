#!/usr/bin/python -tt

import sys

def main():
    inFile = open(sys.argv[1], 'rU')
    outFile = open(sys.argv[2], 'w')
    aLine = inFile.readline()
    T = eval(aLine)
    for case in range(T):
        aLine = inFile.readline()
        N = eval(aLine)
        aline = inFile.readline()
        n = aline.split()
        for i in range(N):
            n[i] = eval(n[i])
        oldN = []
        oldN.extend(n)
        n.sort()
        ans = 0.0
        print n
        print oldN
        for i in range(N):
            if oldN[i] != n[i]:
                ans += 1
        print ans
        outFile.write("Case #%d: %.6f\n" %(case+1, ans))
    inFile.close()
    outFile.close()


if __name__ == '__main__':
    main()
