#!/usr/bin/env python
#

import itertools
import math
import os
import sys

class Problem:
    cases = []
    results = []
    
    def __init__(self, filename):
        """
            Initialize the class, reading the test cases
            into the the self.cases property
        """
        self.filename = filename
        f = open(filename, 'r')
        input = [l[0:-1] for l in f]
        f.close()
        
        #s = (len(input) - 1) / int(input[0])
        #self.cases = [tuple(input[i:i+s]) for i in range(1, len(input), s)]
        n = int(input[0])
        x = 1
        for i in range(0, n):
            t = input[x].split(' ')
            csn = int(t[0])
            case = [(int(t[0]), int(t[1]))]
            for j in range(1, csn+1):
                case.append(list(input[x+j]))
            x = x + csn + 1
            self.cases.append(case)

    def write(self):
        """
            Write the results in a new file
        """
        f = open('results-'+filename.split('/')[-1], 'w')
        for i in range(0, len(self.results)):
            f.write('Case #{0}:\n{1}\n'.format(i+1, self.results[i]))
        f.close()
        return self

    def resolve(self):
        """
            Iterate over the test cases and process a result
            for each case
        """
        self.results = [self.__process(case) for case in self.cases]
        print self.results
        return self
    
    def __process(self, case):
        """
            Process a test case and return and array with
            the solution.
        """
        (R, C) = case[0]
        table = case[1:]
        
        for i in range(0, R):
            for j in range(0, C):
                if table[i][j] == '#' and j < (C-1) and table[i][j+1] =='#' and i < (R-1) and table[i+1][j] == '#' and table[i+1][j+1] == '#':
                    table[i][j] = '/'
                    table[i][j+1] = '\\'
                    table[i+1][j] = '\\'
                    table[i+1][j+1] = '/'
                elif table[i][j] == '#':
                    return 'Impossible'
        
        ts = []
        for t in table:
            ts.append(''.join(t))
        
        return '\n'.join(ts)
        

if __name__ == '__main__':
    # Check args
    if len(sys.argv) is not 2:
        print 'Usage: {0} input.txt'.format(sys.argv[0])
        exit(-1)
    
    filename = sys.argv[1]
    
    # Check if input file exists
    if not os.path.exists(filename):
        print 'Input file {0} doesn\'t exists'.format(filename)
        exit(-1)
    
    # Resolve the problem and write the results
    Problem(filename).resolve().write()