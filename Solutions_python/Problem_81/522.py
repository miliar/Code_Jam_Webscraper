#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import math
#import psyco
import numpy

def readnumbers(f, dtype=int):
    return [dtype(x) for x in f.readline().strip().split()]

class Solution:
    def main(self, filename):
        self.dataset_stream = open(filename, 'r')
        line = self.dataset_stream.readline()
        self.cases_left = int(line)
        print "File contains %d testcases." % (self.cases_left)

        self.caseno = 1
        while self.cases_left > 0:
            self.cases_left -= 1
            self.readcase()
            self.printcase()
            self.solve()
            self.printsolution()
            self.caseno += 1

    def readcase(self):
        N = readnumbers(self.dataset_stream)[0]
        table = numpy.zeros((N, N), 'i')
        for i in xrange(N):
            line = self.dataset_stream.readline().strip()
            for j, c in enumerate(line):
                if c == '.':
                    table[i][j] = -1
                elif c == '1':
                    table[i][j] = 1
        self.N = N
        self.table = table
    
    def printcase(self):
        print repr(self.table)

    
    def solve(self):
        N = self.N
        table = self.table

        def calc_wp(tbl):
            result = numpy.zeros(len(tbl))
            for i in xrange(len(tbl)):
                wp = 0
                n = 0
                for k, p in enumerate(tbl[i]):
                    if p == 1:
                        wp += 1
                    if p != -1:
                        n += 1
                result[i] = float(wp) / float(n)
            return result
        
        WP = calc_wp(table)
        OWP = numpy.zeros(N)
        OOWP = numpy.zeros(N)
        RPI = numpy.zeros(N)
        for i in xrange(N):
            without_i = calc_wp(numpy.delete(table, i, 1))
            s = 0.0
            n = 0.0
            for j in xrange(N):
                if table[i][j] != -1:
                    s += without_i[j]
                    n += 1
            OWP[i] = s / n

        for i in xrange(N):
            s = 0.0
            n = 0.0
            for j in xrange(N):
                if table[i][j] != -1:
                    s += OWP[j]
                    n += 1
            OOWP[i] = s / n

        for i in xrange(N):
            RPI[i] = 0.25 * WP[i] + 0.5*OWP[i] + 0.25*OOWP[i]

        print "WP =", repr(WP)
        print "OWP =", repr(OWP)
        print "OOWP =", repr(OOWP)
        print "RPI = ", repr(RPI)
        self.RPI = RPI
        
    def printsolution(self):
        sys.stdout.flush()
        #print >>sys.stderr, "Case #%d: %d" % (self.caseno, self.switches)
        print >>sys.stderr, "Case #%d:" % (self.caseno)
        for val in self.RPI:
            print >>sys.stderr, "%.10f" % val
        sys.stderr.flush()

if __name__ == '__main__':
    #psyco.full()
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
