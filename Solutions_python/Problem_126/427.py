'''
Created on May 12, 2013

@author: ericdennison
'''

class Parser(object):
    def __init__(self, fname):
        self.lines = file(fname).readlines()
        self.index = 0

    def getnum(self, dtype):
        retval = dtype(self.lines[self.index])
        self.index += 1
        return retval

    def getlist(self, dtype):
        l = self.lines[self.index].split()
        self.index += 1
        return [dtype(x) for x in l]

    def getnnum(self, n, dtype):
        return [self.getnum(dtype) for i in range(0, n)]

    def getnlist(self, n, dtype):
        return [self.getlist(dtype) for i in range(0, n)]
        

p = Parser("A-small-attempt0.in")


cases = [(c[0], int(c[1])) for c in [p.getlist(str) for i in range(0,p.getnum(int))]]
vowels = ['a','e','i','o','u']

fo = file("out.txt",'w')

"""
4
quartz 3
straight 3
gcj 2
tsetse 2

Case #1: 4
Case #2: 11
Case #3: 3
Case #4: 11
"""

casenum = 0

for w,n in cases:
    cc = 0
    #print w,n
    lw = len(w)
    for s in range(0,lw-n+1):
        for l in range(n, lw-s+1):
            ss = w[s:s+l]
            #print ss
            c = 0
            for sn in range(0,l):
                if ss[sn] in vowels:
                    c = 0
                else:
                    c += 1
                    if c == n:
                        break
            if c >= n:
                #print "ss: ", w, ss
                cc += 1
    casenum += 1
    fo.write( "Case #{0}: {1}\n".format(casenum, cc))
fo.close()   


