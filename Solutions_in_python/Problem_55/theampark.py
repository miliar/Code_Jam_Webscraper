'''
Created on May 8, 2010

@author: jagadeesh
'''

import sys
from sys import stdin

class Problem:
    
    def __init__(self):
        self.T = 0
        self.R = 0
        self.k = 0
        self.N = 0
        self.g = []
        
        self.case = 0
        self.cache = []
        self.cindex = 0
        
    
    def _readT(self):
        self.T = int(stdin.readline())
    
    
    def _readRkN(self):
        line = stdin.readline()
        self.R, self.k, self.N = [int(x) for x in line.split()]
    
    
    def _readN(self):
        line = stdin.readline()
        self.g = [int(x) for x in line.split()]
    
    
    def __call__(self):
        
        self._readT()
        self.case = 0
        for x in range(self.T):
            self._readRkN()
            self._readN()
            self.case += 1
            yield self.case
    
    
    
    def solve(self):
        
        self.precompute()
        
        self.compute()
        


    def precompute(self):
        self.cache = []
        
        lookup = {}
        index = 0

        while True:
            euro = 0
            sidx = index
            length = 0
            
            while True:
                idx = index % self.N
                euro += self.g[idx]
                
                if euro > self.k: # a ride cannot take more than k people
                    euro -= self.g[idx]
                    break
                
                length += 1
                index += 1
                
                if length == self.N: # a ride cannot take more than N groups
                    break
            
            idx = sidx % self.N
            if lookup.has_key((idx, length)):
                for x in range(len(self.cache)):
                    if idx == self.cache[x][0] and length == self.cache[x][1]:
                        self.cindex = x
                        break
                        
                #print "recomputed (%d, %d) = %d %d" % (idx, length, euro, self.cindex)
                break
            
            #print "(%d, %d) = %d" % (idx, length, euro)
            
            lookup[(idx, length)] = euro
            self.cache.append((idx, length, euro))
    
    
    def compute(self):
        
        cindex = self.cindex
        clength = len(self.cache)
        repeatable = clength - cindex
        
        total = 0
        # initial residue
        for x in range(0, cindex):
            total += self.cache[x][2]
        
        #print "one: %d" % total
        
        rtotal = 0
        for x in range(cindex, clength):
            rtotal += self.cache[x][2]
        
        #print "two: %d" % rtotal
        
        total_repetable = self.R - cindex
        
        q = int(total_repetable / repeatable)
        r = total_repetable % repeatable
        
        #print "q r %d %d" % (q, r)
        
        total += q * rtotal
        #print "three: %d" % total
        for x in range(r):
            total += self.cache[x + cindex][2]
        
        print "Case #%d: %d" % (self.case, total)

    
if __name__ == "__main__":
    
    problem = Problem()
    for case in problem():
        problem.solve()
    

