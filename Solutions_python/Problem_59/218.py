#!/usr/bin/python

import sys
from math import *

C = int(sys.stdin.readline())

class directory:
    def __init__(self,name,root):
        self.children = {}
        self.name = name
        self.root = root
    def search(self,name):
        if name in self.children:
            return True
        else:
            return False

    #"" is root
    def add(self,name):
        #print name
        if name == '':
            return 0
        pos = 0
        now = name.split("/")[0]

        for pos in range(len(name)+1):
            if pos == len(name):
                break
            if name[pos] == '/':
                pos = pos+1
                break

        if self.search(now):
            return self.children[now].add(name[pos:])
        else:
            self.children[now] = directory(now,self)
            return 1 + self.children[now].add(name[pos:])
        
for testcase in range(C):
    line = sys.stdin.readline().strip().split()
    N = long(line[0])
    M = long(line[1])

    root = directory("/",None)
    for i in range(N):
        line = sys.stdin.readline().strip()
        root.add(line[1:])

    result = 0
    for j in range(M):
        line = sys.stdin.readline().strip()
        result += root.add(line[1:])

    print "Case #%d: %d" % (testcase+1,result)
    
    
        
