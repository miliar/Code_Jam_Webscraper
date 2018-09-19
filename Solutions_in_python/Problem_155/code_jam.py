__author__ = 'prakaran'

import sys

def code_jam(tup):
    for i in xrange(1, int(tup[0]) + 1):
        result = 0
        no_people = 0
        smax, string = tup[i].split()
        smax = int(smax)
        for ind, j in enumerate(string):
            item = int(j)
            if item:
                if no_people < ind:
                    add = ind - no_people
                    result += add
                    no_people += add
                no_people += item
                if no_people >= smax:
                    break

        print "Case #" + str(i) + ": " + str(result)

inputs = open(sys.argv[1], 'r').readlines()
code_jam(inputs)