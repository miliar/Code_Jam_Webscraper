#!/usr/bin/python
import string
import sys

def main():
    infile = open(sys.argv[1], "r")

    for case in range(1, int(infile.readline())+1):
        values = [ int(x) for x in infile.readline().split(" ") ]

        mini = min(values[0], values[1])
        maxi = max(values[0], values[1])

        a = mini
        b = maxi

        k = values[2]

        win = 0
        for a1 in range(a):
            for a2 in range(b):
                if a1 & a2 < k:
                    win += 1

        print("Case #{0}: {1}".format(case, win))

if __name__ == "__main__":
        main()