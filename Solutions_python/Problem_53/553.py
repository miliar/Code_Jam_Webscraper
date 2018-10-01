#!/usr/bin/python

import math
import sys

def main():

    f = open(sys.argv[1])
    numTests = f.readline()

    i = 1
    for line in f:
        
        (n, k) = line.split(" ")
        n = int(n)
        k = int(k)

        on = k % (2 ** n) == (2 ** n) - 1

        print "Case #" + str(i) + (": ON" if on else ": OFF")
        i += 1
if __name__ == "__main__":
    main()
