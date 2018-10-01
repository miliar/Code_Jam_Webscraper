'''
GCJ problem: standing_ovation

Created on: 11 Apr 2015

@author: franovic
'''
class GCJ_standing_ovation(object):
    def solve(self):
        N = self.getInt()
        Ns = [int(x) for x in list(self.getString())]
        answer = 0
        clapping = 0
        for i in xrange(N+1):
            if Ns[i] > 0 and clapping < i:
                answer += i-clapping
                clapping += i-clapping
            clapping += Ns[i]
        return '%d' % answer

#I/O code start
    def __init__(self, fName):
        self.fNameIn = fName
        self.fNameOut = '.'.join(fName.split('.')[:-1]+ ['out'])
        self.input = open(fName, 'r')
        self.line=[]
        self.tCases = self.getInt()

    def writeSolution(self):
        out=''
        for t in xrange(1,self.tCases+1):
            out+="Case #%d: %s\n" % (t, str(self.solve()))
        fout = open(self.fNameOut, 'w+')
        fout.write(out.rstrip())

    def getString(self):
        if len(self.line)==0:
            self.line=self.input.readline().rstrip().split( )
        ret = self.line.pop(0)
        return ret
    def getInt(self):
        return int(self.getString())
    def getFloat(self):
        return float(self.getString())
    def getStrings(self):
        if len(self.line)==0:
            self.line=self.input.readline().rstrip().split( )
        ret = self.line[:]
        self.line=[]
        return ret
    def getInts(self):
        return [int(x) for x in self.getStrings()]
    def getFloats(self):
        return [float(x) for x in self.getStrings()]

import sys
if __name__ == '__main__':
    gcj = GCJ_standing_ovation(sys.argv[1])
    gcj.writeSolution()
#I/O code end