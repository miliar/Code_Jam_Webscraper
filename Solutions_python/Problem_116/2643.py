def masterClass(Cases):
    numberOfCases = int(Cases[0:Cases.find("\n")])
    Cases = Cases[Cases.find("\n"):]
    for x in range(1,numberOfCases+1):
        a,Cases = extractTestCase(Cases)
        Cases = Cases[1:]
        a=makeList(a)
        Output = "Case #" + str(x) + ": " + solveBoard(a)
        print Output
    return Cases
        

def makeList(List):
    foo = []
    List = List[1:]
    for x in range(4):
        foo.append(List[0:4])
        List = List[5:]
    return foo

def extractTestCase(Cases):
    testCase = Cases[:20]
    Cases = Cases[20:]
    return testCase, Cases


def solveBoard(board):
    results = ["X won","O won","Draw","Game has not completed"]
    Xvic,Ovic = False, False

    if isVictoryX(board[0]):
        Xvic = True
    if isVictoryX(board[1]):
        Xvic = True
    if isVictoryX(board[2]):
        Xvic = True
    if isVictoryX(board[3]):
        Xvic = True

    if isVictoryO(board[0]):
        Ovic = True
    if isVictoryO(board[1]):
        Ovic = True
    if isVictoryO(board[2]):
        Ovic = True
    if isVictoryO(board[3]):
        Ovic = True

    transposedBoard = transposeBoard(board)

    if isVictoryX(transposedBoard[0]):
        Xvic = True
    if isVictoryX(transposedBoard[1]):
        Xvic = True
    if isVictoryX(transposedBoard[2]):
        Xvic = True
    if isVictoryX(transposedBoard[3]):
        Xvic = True

    if isVictoryO(transposedBoard[0]):
        Ovic = True
    if isVictoryO(transposedBoard[1]):
        Ovic = True
    if isVictoryO(transposedBoard[2]):
        Ovic = True
    if isVictoryO(transposedBoard[3]):
        Ovic = True

    diagonal1 = board[0][0]+board[1][1]+board[2][2]+board[3][3]
    diagonal2 = board[0][3]+board[1][2]+board[2][1]+board[3][0]

    if isVictoryX(diagonal1):
        Xvic = True
    if isVictoryX(diagonal2):
        Xvic = True

    if isVictoryO(diagonal1):
        Ovic = True
    if isVictoryO(diagonal2):
        Ovic = True
        
    dotOnBoard = False
    for line in board:
        if "." in line:
            dotOnBoard = True
    if Xvic:
        return results[0]
    if Ovic:
        return results[1]
    if dotOnBoard:
        return results[3]
    return results[2]

    return False

def isVictoryX(line):
    if line[0] == line[1] == line[2] == line[3] == "X":
        return True
    if line[0] == "T" and line[1] == line[2] == line[3] == "X":
        return True
    if line[1] == "T" and line[0] == line[2] == line[3] == "X":
        return True
    if line[2] == "T" and line[0] == line[1] == line[3] == "X":
        return True
    if line[3] == "T" and line[0] == line[1] == line[2] == "X":
        return True
    return False

def isVictoryO(line):
    if line[0] == line[1] == line[2] == line[3] == "O":
        return True
    if line[0] == "T" and line[1] == line[2] == line[3] == "O":
        return True
    if line[1] == "T" and line[0] == line[2] == line[3] == "O":
        return True
    if line[2] == "T" and line[0] == line[1] == line[3] == "O":
        return True
    if line[3] == "T" and line[0] == line[1] == line[2] == "O":
        return True
    return False

def transposeBoard(board):
    return [board[0][0]+board[1][0]+board[2][0]+board[3][0],
            board[0][1]+board[1][1]+board[2][1]+board[3][1],
            board[0][2]+board[1][2]+board[2][2]+board[3][2],
            board[0][3]+board[1][3]+board[2][3]+board[3][3]]


testcases = str(raw_input("Case:"))
masterClass(testcases)
