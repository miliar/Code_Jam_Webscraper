#!/usr/bin/env python

import fileinput

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-05-04"

class Problem:
    __debug = False

    def __calcSolutionByDeep(self, inSize, inMotes, inOps):
        if len(inMotes) == 0:
            if self.__minOps == None or self.__minOps > inOps:
                self.__minOps = inOps
            return 

        if inSize > inMotes[0]:
            self.__calcSolutionByDeep(inSize + inMotes[0], inMotes[1:], inOps)
        else:
            if inSize > 1:
                self.__calcSolutionByDeep((inSize * 2) - 1, inMotes, inOps + 1)

            # Remove the first mothes
            self.__calcSolutionByDeep(inSize, inMotes[1:], inOps + 1)

    def resolve(self):
        self.__calcSolutionByDeep(self.__size, self.__motes, 0)

        return self.__minOps

    def __init__(self, inSize, inMotes):
        self.__minOps = None
        self.__size = inSize
        self.__motes = sorted(inMotes)

        if self.__debug:
            print "Size: %s" % (self.__size) 
            print "Motes: %s" % (self.__motes) 

if __name__ == "__main__":
    problems = int(raw_input())

    for problem in range(problems):
        info = map(int, raw_input().split())
        motes = map(int, raw_input().split())

        print "Case #%d: %s" % (problem + 1, Problem(info[0], motes).resolve())
