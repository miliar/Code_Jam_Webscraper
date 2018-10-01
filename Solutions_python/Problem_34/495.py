#!/usr/bin/env python
import re

class Alien(object):
    def __init__(self,filename):
        with open(filename) as f:
            state = 'first'
            
            for line in f.readlines():
                line = line.strip()
                if state == 'first':
                    cols = line.split(' ')
                    self.token_count = int(cols[0])
                    self.word_count = int(cols[1])
                    self.test = int(cols[2])
                    self.dict = []
                    self.tests = []
                    state = 'dict'
                elif state == 'dict':
                    self.dict.append(line)
                    if len(self.dict) == self.word_count:
                        state = 'tests'
                elif state == 'tests':
                    self.tests.append(line)
    def solve(self):
        i=0
        for test in self.tests:
            i+=1
#            print test
            test=test.replace('(','[')
            test=test.replace(')',']')
            regex = re.compile(test)
            
            matches = 0
            for word in self.dict:
                if regex.match(word):
                    matches +=1
#                    print word
            print "Case #%s: %s" % (i,matches)
            
            
if __name__ == '__main__':
    import sys
    Alien(sys.argv[1]).solve()