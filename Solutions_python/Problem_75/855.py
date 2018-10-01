'''
Created on May 7, 2011

@author: jagadeesh
'''

from sys import stdin
import re
    
class Problem:
    
    def __init__(self):
        self.T = 0
        self.C = 0
        self.combines = {}
        self.D = 0
        self.oppose = {}
        self.oppose_pattern_list = []
        self.oppose_pattern = None
        self.N = 0
        self.input = ''

        self.case = 0
        
        
    def _readT(self):
        self.T = int(stdin.readline())
    
    
    def _readLine(self):
        self.combines = {}
        self.oppose = {}
        self.oppose_pattern_list = []
        self.oppose_pattern = ''

        line = stdin.readline()
#        print "line: %s" % line 
        parts = line.split()
        parts.reverse()

        self.C, c_strings = self._readSegment(parts)
        self._parseCombines(c_strings)
        
        self.D, d_strings = self._readSegment(parts)
        self._parseOppose(d_strings)
        self.oppose_pattern = re.compile('|'.join(self.oppose_pattern_list))
#        print "pattern: %s" % '|'.join(self.oppose_pattern_list)

        self.N = int(parts.pop())
        self.input = parts.pop()
#        print "input: %s" % self.input
        
    
    def _readSegment(self, parts):
        n = int(parts.pop())
        n_string = []
        if n:
            for _ in range(n):
                n_string.append(parts.pop())
#        print "%s %s" % (n, n_string)
        return (n, n_string)


    def _parseCombines(self, c_strings):
        for s in c_strings:
            c1 = s[0]
            c2 = s[1]
            self.combines[c1+c2] = s[2]
            self.combines[c2+c1] = s[2]
#        print "combines: %s" % self.combines
    
    
    def _parseOppose(self, d_strings):
        for s in d_strings:
            d1 = s[0]
            d2 = s[1]
            self.oppose_pattern_list.append("(%s.*%s)" % (d1, d2))
            self.oppose_pattern_list.append("(%s.*%s)" % (d2, d1))
#        print "oppose: %s" % self.oppose
    
        
    def __call__(self):
        
        self._readT()
        self.case = 0
        for _ in range(self.T):
#            print "Case #%s: " % (self.case+1)
            self._readLine()
            self.case += 1
            yield self.case
    
    
    def solve(self):
        element_list = ' '
        for x in self.input:
            #invoke
#            print "Invoke===="
            element_list += x
#            print "elementList: |%s" % element_list
            
            #comibine
            cs = element_list[-2:]
            if self.combines.has_key(cs):
                ns = self.combines[cs]
                element_list = element_list[:-2] + ns
                
#            print "elementList: |%s" % element_list
            #oppose
            if self.oppose_pattern_list and self.oppose_pattern.search(element_list):
                element_list = ' '
#            print "elementList: |%s" % element_list
        
        element_list = element_list[1:]
        lst = [x for x in element_list]
        output = '[' + ', '.join(lst) + ']'
        print "Case #%s: %s" % (self.case, output)
    
if __name__ == "__main__":
    
    problem = Problem()
    for case in problem():
        problem.solve()
    
