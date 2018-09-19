class Problem:
    def __init__(self) :
        self.R = 0
        self.C = 0
        self.W = 0

def readProblem(input):
    problem = Problem()
    
    line = input.readline().split()
    problem.R = int(line[0])
    problem.C = int(line[1])
    problem.W = int(line[2])
    
    return problem

def oneRow(c, w):
    tries = 0 
    cells = c

    while (cells >= 2 * w): 
        tries += 1
        cells = cells - w
        
    if ((cells == w) or (w == 1)):
        tries += w
    elif (w >= cells/2):
        tries += w + 1
        
    return tries;
    
def solveProblem(problem):
    answer = "There is no solution."
    
    answer = problem.R * oneRow(problem.C, problem.W)
    
    return answer



input = open('input.in')
output = open('output.out', 'w')

cases = int(input.readline())
for i in range(cases):
    problem = readProblem(input)
    answer = solveProblem(problem)
    print answer
    output.write("Case #" + str(i+1) + ": " + str(answer) + "\n")

