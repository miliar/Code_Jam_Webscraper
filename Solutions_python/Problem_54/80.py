def outputline(casenumber, diff, outlist):
    result = "Case #" + str(casenumber) + ": " + str(diff)
    outlist.append(result + '\n')

class Problem:
    def __init__(self):
        self.greateventlist = list()

class ProblemXform:
    def __init__(self):
        self.recentgreatevent = None
        self.greateventdiffs = list()

def xformer(problem,problemxform):
    prevval = problem.greateventlist[0]
    diffs = list()
    for val in problem.greateventlist[1:]:
        diffs.append(abs(val - prevval))
        prevval = val
    problemxform.recentgreatevent = problem.greateventlist[0]
    problemxform.greateventdiffs = diffs

def inputline(string, problemlist):
    args = string.split(' ')
    p = Problem()
    greatevents = list()
    for greatevent in args[1:]:
        greatevents.append(int(greatevent))
    p.greateventlist = greatevents
    x = ProblemXform()
    xformer(p,x)
    problemlist.append(x)

import fractions

def compute(problem):
    gcd = problem.greateventdiffs[0]
    for diff in problem.greateventdiffs[1:]:
        gcd = fractions.gcd(gcd,diff)
    return (-problem.recentgreatevent) % gcd

def solution(inputfile,outputfile):
    inp = open(inputfile)
    p = Program()
    for line in inp:
        p.takeline(line)
    inp.close()
    p.compute()
    out = open(outputfile,'w')
    for line in p.outlines():
        out.write(line)
    out.close()

class Program:
    def __init__(self):
        self.count = None
        self.limit = None
        self.probs = []
        self.anss = []
        
        d = dict()
        def readT(string, program):
            program.curfunc = d["readP"]
            program.limit = int(string)
            program.count = 1
        def readP(string, program):
            inputline(string,program.probs)
            if(program.count > program.limit):
                raise Exception
            if(program.count == program.limit):
                program.curfunc = d["readT"]
            program.count += 1

        d["readT"] = readT
        d["readP"] = readP
        self.curfunc = d["readT"]

    def takeline(self,string):
        self.curfunc(string, self)

    def compute(self):
        casenum = 0
        for prob in self.probs:
            casenum += 1
            outputline(casenum,compute(prob),self.anss)

    def outlines(self):
        return self.anss
