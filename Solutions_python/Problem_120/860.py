__author__ = 'michal'

import sys
import math

def bullseye(r, t):

    i = 0
    last = r*r
    farb = t
    blacks = 0
    sum = last

    i = 1
    blacks = 1
    while True:
        val = (r+i)*(r+i) - (r+i-1)*(r+i-1)

        farb -= val

        if farb < 0:
            return blacks - 1

        blacks += 1
        i += 2

if __name__=="__main__":

    file_out = None
    if len(sys.argv) >= 2:
        file = open(sys.argv[1])
        if len(sys.argv) == 3:
            file_out = open(sys.argv[2], 'w')
    else:
        file = sys.stdin

    cases = int(file.readline())

    for case in range(cases):

        line = file.readline()
        params = map(lambda x: int(x), line.split())

        r = params[0]
        t = params[1]

        result = bullseye(r, t)

        out = "Case #%i: %s" % (case + 1, result)

        print out
        if file_out != None:
            file_out.write(out + '\n')



