def parseFromFile(path):
    with open(path) as f:
        data = f.read()
    return parseInput(data)

def parseInput(inp):
    lines = inp.splitlines()
    cases = int(lines[0])
    lines = lines[1:]
    for case in range(cases):
        p = case * 10
        choice1, board1, choice2, board2 = fixTypes(lines[p], lines[p+1:p+5], lines[p+5], lines[p+6:p+10])
        firstLineSet = set(board1[choice1])
        secondLineSet = set(board2[choice2])

        intersect = firstLineSet & secondLineSet
        
        intersections = len(intersect)
        if intersections == 0:
            res = "Volunteer cheated!"
        elif intersections == 1:
            res = str(intersect.pop())
        else:
            res = "Bad magician!"
        print ("Case #%d: %s" % (case +1, res))
        
def fixTypes(choice1, board1, choice2, board2):
  
    return fixChoice(choice1), fixBoard(board1), fixChoice(choice2), fixBoard(board2)

def fixChoice(choice):
    return int(choice)-1

def fixBoard(board):
    return [[int(n) for n in line.split()] for line in board]
