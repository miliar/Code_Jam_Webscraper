import pprint
pp = pprint.PrettyPrinter(indent=4)

def ParseInput(filename):
    problems = []
    with open(filename, "r") as f:
        num_problems = int(f.readline())
        for i in range(num_problems):
            current_problem = []
            (height, width) = (int(x) for x in f.readline().split(" "))
            lawn = []
            for j in range(height):
                lawn.append([int(x) for x in f.readline().split(" ")])
            problems.append(lawn)
            
    return problems
        

def SolveProblem(problem):
    lawn = problem
    height = len(problem)
    width = len(problem[0])
    
    heights = []
    widths = []
    
    for i in range(height):
        max_height = 0
        for j in range(width):
            if lawn[i][j] > max_height:
                max_height = lawn[i][j]
        heights.append(max_height)
        
    for j in range(width):
        max_width = 0
        for i in range(height):
            if lawn[i][j] > max_width:
                max_width = lawn[i][j]
        widths.append(max_width)
        
        
    for i in range(height):
        for j in range(width):
            if lawn[i][j] != min(heights[i], widths[j]):
                return "NO"
    
    return "YES"
                
    

def SolveAndPrint(problems):
    current_problem = 1
    for problem in problems:
        answer = SolveProblem(problem)
        print ("Case #%d:" % current_problem), answer
        current_problem += 1
    
    
SolveAndPrint(ParseInput("B-large.in"))