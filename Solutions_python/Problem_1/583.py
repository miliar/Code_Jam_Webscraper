#!/usr/bin/env python
# encoding: utf-8
"""
save_the_universe.py

Created by Kyle Jensen on 2008-07-17.
"""

import sys
import os

class TestCase(object):
    """docstring for TestCase"""
    def __init__(self, search_engines, queries):
        super(TestCase, self).__init__()
        self.search_engines = search_engines
        self.queries = queries

    @property
    def total_len(self):
        """docstring for total_len"""
        return len(self.search_engines) + len(self.queries) + 2


    def solve(self):
        """ Dynamic programmin shizzle
        """
        
        def non_none_min(x):
            return min(pss for pss in x if pss != None)
            
        # init to zero
        previous_step = [0] * len(self.search_engines)

        # step through queries
        for i,q in enumerate(self.queries):
            this_step = [None] * len(self.search_engines)

            for j,s in enumerate(self.search_engines):
                if q==s:
                    # Can't use this search engine for this
                    # query
                    pass
                else:
                    if previous_step[j] == None:
                        this_step[j] = non_none_min(previous_step) + 1
                    else:
                        this_step[j] = previous_step[j]
            previous_step = this_step
        return non_none_min(previous_step)
                    
    
    def __str__(self):
        """docstring for __str__"""
        return "Engines(%s) / Queries(%s)" % ( \
                ",".join(self.search_engines),
                ",".join(self.queries),
        )
        
    
class TestCaseSet(object):
    """docstring for TestCaseSet"""
    def __init__(self, infile):
        super(TestCaseSet, self).__init__()
        self.cases = []

        lines = [line.strip() for line in open(infile)]
        self.num_cases = int(lines[0])

        for i in range(self.num_cases):
            ffwd = sum(c.total_len for c in self.cases)
            num_search_engines = int(lines[ffwd+1])
            num_queries = int(lines[ffwd+1+num_search_engines+1]) 
            new_case = TestCase( \
                            lines[ffwd+2 : ffwd+2+num_search_engines],
                            lines[ffwd+3+num_search_engines : ffwd+3+num_search_engines+num_queries],
            )
            self.cases.append(new_case)
    
    def solve(self):
        """docstring for solve"""
        for i,c in enumerate(self.cases):
            print "Case #%d: %d" % (i+1, c.solve())
    
    def __str__(self):
        """docstring for __str__"""
        return "\n".join(str(case) for case in self.cases)
        

def main():
	tsc = TestCaseSet(sys.argv[1])
	tsc.solve()

if __name__ == '__main__':
	main()

