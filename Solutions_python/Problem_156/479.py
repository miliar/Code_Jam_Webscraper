'''
Problem B: Infinite House of Pancakes
'''
import operator
import math

def readInput(filename, parser):
    with open(filename, 'r') as infile:
        data = infile.readlines()
        return parser(data)

def writeOutput(filename, solver, data):
    with open(filename, 'w') as outfile:
        for i, case in enumerate(data):
            outfile.write("Case #{0}: ".format(i+1) + str(solver(case)) + '\n')
            
def pancakeParser(data):
    numcases = 0
    cases = []
    for i, line in enumerate(data):
        if i == 0:
            numcases = i
        elif (i%2 == 1):
            ndiners = int(line)
            cases.append(Case(ndiners, [int(x) for x in data[i+1].split(' ')]))
    return cases    

def Solve(case):
    secondlist = case.dinerlist[:]
    maxval = max(case.dinerlist)
    bestguess = maxval
    stepcounter = 0
    
    while maxval > 0:
        maxval -= 1
        stepcounter += 1
        index, value = max(enumerate(case.dinerlist), key=operator.itemgetter(1))
        case.dinerlist.append(int(math.floor((math.floor(math.sqrt(case.dinerlist[index]))-1)*case.dinerlist[index] / math.floor(math.sqrt(case.dinerlist[index])))))
        case.dinerlist[index] = int(math.ceil(case.dinerlist[index]/math.floor(math.sqrt(case.dinerlist[index]))))
        objectivevalue = int(stepcounter) + int(max(case.dinerlist))
        print objectivevalue
        if objectivevalue < bestguess:
            bestguess = objectivevalue
            
    maxval = max(secondlist)
    #bestguess = maxval
    stepcounter = 0

    while maxval > 0:
        maxval -= 1
        stepcounter += 1
        index, value = max(enumerate(secondlist), key=operator.itemgetter(1))
        secondlist.append(int(math.floor(secondlist[index] / 2.0)))
        secondlist[index] = int(math.ceil(secondlist[index]/2.0))
        objectivevalue = int(stepcounter) + int(max(secondlist))
        print objectivevalue
        if objectivevalue < bestguess:
            bestguess = objectivevalue    
    
    print bestguess
    return bestguess
        
    

class Case(object):
    
    ndiners = 0
    dinerlist = []
    
    def __init__(self, nDiners, dinerList):
        self.ndiners = nDiners
        self.dinerlist = dinerList

if __name__ == "__main__":
    filename = 'B-small-attempt3.in'
    outfile = 'pancakeSmall3.out'

    data = readInput(filename, pancakeParser)
    writeOutput(outfile, Solve, data)