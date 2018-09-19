from itertools import islice
import numpy as np
import scipy as sp

class OneA:

    n = 0 #number of cases
    currcase = 0
    filedata = []


    A = []
    B = []
    wires = []
    
    inputfile = "onea.in"
    outputfile = "onea.out"
    
    def __init__(self):
        self.solvetheproblem()

    def solvetheproblem(self):
        f = open(self.inputfile)
        g = open(self.outputfile,'a')
        
        with open(self.inputfile) as myfile:
            cases=list(islice(myfile,1))
            self.n = int(cases[0])

        for lines in f:
            self.filedata.append(lines[0:len(lines)-1])

        #Use this when cases span multiple lines:
        #for i in range(1,2*self.n,2):

        case = 1
        t = 1

        for i in range(1,self.n+1):

            with open(self.inputfile) as myfile:

                info=list(islice(myfile,t,t+1))
                lines = info[0][0:len(info[0])-1].split(" ")
                print lines
                N = int(lines[0])
                print "N = " + str(N)
                for j in range(1,N+1):
                    z = []
                    x = self.filedata[t+j]
                    y = x.split(" ")
                    self.A.append(int(y[0]))
                    self.B.append(int(y[1]))
                    z.append(int(y[0]))
                    z.append(int(y[1]))
                    self.wires.append(z)
                    y = []
                    print x
                print self.A
                print self.B
                print self.wires
                t = t + N + 1
                        
                self.currcase = case
                a = self.solvesingle()
                case = case+1
                self.A = []
                self.B = []
                self.wires = []
                print "ans = " + str(a)
                g.write("Case #" + str(self.currcase) + ": " + str(a) + "\n")
            
    def solvesingle(self):
        ans = 0
        for w in self.wires:
            a = w[0]
            b = w[1]
            for p in self.A:
                if self.B[self.A.index(p)] > b and p < a:
                    ans = ans + 1
                if self.B[self.A.index(p)] < b and p > a:
                    ans = ans + 1
        return ans/2
                    
