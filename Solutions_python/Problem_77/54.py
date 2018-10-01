
import sys
import operator

def main():

    if len(sys.argv) == 2:
        filename = sys.argv[1] #input file name from command line
    else:
        filename = "testcases.txt"
    inputfile = open(filename, 'r')
    testcases = int(inputfile.readline())
    for i in xrange(testcases):
        inputfile.readline()
        print 'Case #%s: %s'%(i+1,jammit(inputfile.readline()))

def jammit(inputline):
    items = [int(i) for i in inputline.split()]
    sorteditems = [int(i) for i in inputline.split()]
    sorteditems.sort()
    outOfOrder = 0
    for i in xrange(len(items)):
        if items[i] != sorteditems[i]:
            outOfOrder += 1
    return outOfOrder



main()
