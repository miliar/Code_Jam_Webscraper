#! /usr/bin/env python

from collections import defaultdict
from sys import stdin

class elements(object):
    def __init__(self):
        self.combinations = {}
        self.oppositions = defaultdict(set)
        self.stack = []
        
    def new_comb(self, e1, e2, result):
        self.combinations[(e1, e2)] = self.combinations[(e2, e1)] = result
        
    def new_opp(self, e1, e2):
        self.oppositions[e1].add(e2)
        self.oppositions[e2].add(e1)
        
    def invoke(self, element):
        self.stack.append(element)
        if tuple(self.stack[-2:]) in self.combinations:
            self.stack[-2:] = [self.combinations[tuple(self.stack[-2:])]]
        else:
            for i in self.oppositions[element]:
                if i in self.stack:
                    self.stack = []
                    break

t = input()

for test in range(t):
    s = elements()
    data = stdin.readline().strip().split()
    data.reverse()
    
    c = int(data.pop())
    for i in range(c):
        s.new_comb(*tuple(data.pop()))
    
    d = int(data.pop())
    for i in range(d):
        s.new_opp(*tuple(data.pop()))
        
    data.pop()
    elist = data.pop()
    
    for i in elist:
        s.invoke(i)
        
    print "Case #%d: [%s]" % (test+1, ', '.join(s.stack))
        
    