PATH = r"C:\Users\Gil\Documents\jam\input3.txt"
OUTPATH = r"C:\Users\Gil\Documents\jam\output3.txt"

START_RATE = 2

solutionDict = {}

# stupid bug with 3 4 3, 3 5 4 made it all wrong :(.... solved by hand

def getNeighbourNum(r,c,board,i,j):
    num = 0
    for k in (i-1,i,i+1):
        if k >= r or k < 0:
            continue
        for l in (j-1,j,j+1):
            if l >= c or l < 0:
                continue
            if board[k][l] == "*":
                num += 1
    return str(num)

def neighbourZero(r,c,board,i,j):
    for k in (i-1,i,i+1):
        if k >= r or k < 0:
            continue
        for l in (j-1,j,j+1):
            if l >= c or l < 0:
                continue
            if k==i and l==j:
                continue
            if board[k][l] == "0":
                return True

    if board[i][j] == "0":
        return "maybeC"
    return False

def boardFromBoardStr(r,c,boardStr):
    return [list(boardStr[i*c:(i+1)*c]) for i in range(r)]

def checkBoard(r,c,m,board):
    maybeC = False
    
    if (m == (r*c-1)):
        return True
   
    for i in range(r):
        for j in range(c):
            if board[i][j] != "*":
                board[i][j] = getNeighbourNum(r,c,board,i,j)
    
    for i in range(r):
        for j in range(c):
            if board[i][j] != "*":
                neighbour = neighbourZero(r,c,board,i,j)
                if "maybeC" == neighbour and maybeC == False:
                    maybeC = True
                elif (False == neighbour or "maybeC" == neighbour):
                    return False

    return True

def generateAllBoards5(m):
    r=c=5
    boards = ["*" * 10]
    for i in range(r*c - 10):
        boards = [board + "." for board in boards] + [board + "*" for board in boards if (board.count("*") < m)]

    boards = [board for board in boards if (board.count("*") == m)]
    return [boardFromBoardStr(r,c,boardStr) for boardStr in boards]

def generateAllBoards(r,c,m):
    boards = [""]
    for i in range(r*c):
        boards = [board + "." for board in boards] + [board + "*" for board in boards if (board.count("*") < m)]

    boards = [board for board in boards if (board.count("*") == m)]
    return [boardFromBoardStr(r,c,boardStr) for boardStr in boards]

def adjustBoard(board):
    newBoard = ""
    startFound = False
    for row in board:
        for cell in row:
            if cell == "*":
                nextCell = "*"
            elif (cell == "0") and (startFound == False):
                startFound = True
                nextCell = "c"
            else:
                nextCell = "."

            newBoard += nextCell
            
        newBoard += "\n"

    # if m=r*c-1
    if (newBoard.count(".") == 1) and (startFound == False):
        newBoard = newBoard.replace(".","c")

    return newBoard

# in the small version i can use brute force... no need to think of an algorithm :D
# add some 5X5 at the end 
def bruteForce(r,c,m):
    boards = generateAllBoards(r,c,m)
    for board in boards:
        if checkBoard(r,c,m,board):
            board = adjustBoard(board)
            print board
            return board
    print "N"
    return "Impossible\n"

def bruteForce5(m):
    boards = generateAllBoards5(m)
    for board in boards:
        if checkBoard(5,5,m,board):
            board = adjustBoard(board)
            print board
            return board
    print "N"
    return "Impossible\n"

def bruteForce5Rest():
    for m in range(16,25):
        solutionDict[(5,5,m)] = bruteForce5(m)
        

def allBruteForce():
    for r in range(1,6):
        for c in range(1,6):
            print r,c
            for m in range(r*c):
              #  if (r==5) and (c==5) and m >= 10:
              #      solutionDict[(r,c,m)] = bruteForce5(m)    
              #  else:
                solutionDict[(r,c,m)] = bruteForce(r,c,m)

    print "ABOUT TO PRINT DICT!!!\n\n\n"
    print solutionDict


def solveGame(data):
    r,c,m = data


    return solDict2[r,c,m]
                
execfile(r"solDict2.py")

data = open(PATH,"r").readlines()
data = [x.replace("\n","") for x in data]
data = [[int(i) for i in x.split(" ") ] for x in data]

numOfGames = int(data[0][0])

output = ""

for i in range(numOfGames):
    output += "Case #%s:\n" % (i+1)
    output += solveGame(data[1+i])

output = output.rstrip("\n")

print output
open(OUTPATH,"w").write(output)
