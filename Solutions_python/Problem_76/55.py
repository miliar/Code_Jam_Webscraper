
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
    bits = [0]*20
    bitlist = []
    candies = [int(i) for i in inputline.split()]

    if reduce(operator.xor, candies) != 0:
        return 'NO'
    else:
        bro = candies.index(min(candies))
        nibble = min(candies)
        del(candies[bro])
        if reduce(operator.xor,candies) != nibble:
            print 'HOW COULD THIS POSSIBLY HAVE FAILED'
            sys.exit(-1)
        return sum(candies)

main()
