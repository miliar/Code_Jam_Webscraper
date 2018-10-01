#!/usr/bin/python

import sys, getopt
from isFairAndSquare import *

def solveFairAndSquare(strInputFile, strOutputFile):
    fi = open(strInputFile, 'r')
    fo = open(strOutputFile, 'w')
    
    numTestCases = fi.readline().strip()
    for i in range(1, int(numTestCases) + 1):
        numFairAndSquare = 0
        #arrFairAndSquare = []
        [low, upp] = fi.readline().strip().split()[:2]
        for j in range(int(low), int(upp)+1):
            if isFairAndSquare(str(j)):
                numFairAndSquare+=1
                #arrFairAndSquare.append(j)
        
        fo.write('Case #{0}: {1}\n'.format(i, numFairAndSquare))
        #for num in arrFairAndSquare:
        #    print '\t{0}'.format(num)
    
    fi.close()
    fo.close()


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'solveFairAndSquare.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'solveFairAndSquare.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print 'Input File : {0}'.format(inputfile)
    print 'Output File : {0}'.format(outputfile)
    solveFairAndSquare(inputfile, outputfile)

if __name__ == '__main__':
    main(sys.argv[1:])

