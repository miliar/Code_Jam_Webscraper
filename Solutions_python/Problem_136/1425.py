__author__ = 'cheungkt'

import sys


def main():
    with open(sys.argv[1], 'r') as test:
        for i in range(1, int(test.readline()) + 1):
            temp = test.readline()
            C, F, X = [float(x) for x in temp.split(' ', 2)]
            production = 2.0
            time = 0.0
            while X/production > C/production + X/(production + F):
                time += C/production
                production += F
            time += X/production
            print "Case #%i: %.7f" % (i, time)


if __name__ == '__main__':
    main()