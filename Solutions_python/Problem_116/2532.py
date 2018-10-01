import string

def winner(line):
    xWin = True
    yWin = True
    incomplete = False
    
    for character in line:
        if character == 'X':
            yWin = False
        if character == 'O':
            xWin = False
        if character == '.':
            incomplete = True
            xWin = False
            yWin = False
        

    if xWin:
        return 'X'
    if yWin:
        return 'O'
    if incomplete:
        return '.'
    else:
        return 'D'

attempt = open("A-large.in")
fileOut = open("A-large.out", 'w')

numBoards = int(attempt.readline())

for boardNum in range(numBoards):
    board = [[], [], [], []]
    for line in range(4):
        newLine = file.readline(attempt)
        for char in range(4):
            board[line].append(newLine[char])
        


    lines = [0,0,0,0,0,0,0,0,0,0]

    for line in range(4):
        lines[line] = board[line][0:4]

    for vertLine in range(4):
        lines[vertLine+4] = [0,0,0,0]
        for row in range(4):
            lines[vertLine+4][row] = board[row][vertLine]

    lines[8] = [board[0][0], board[1][1], board[2][2], board[3][3]]
    lines[9] = [board[0][3], board[1][2], board[2][1], board[3][0]]

    result = 'D'

    for line in lines:
        lineResult = winner(line)
        if lineResult == 'X':
            result = 'X'
        if lineResult == 'O':
            result = 'O'
        if result != 'X' and result != 'O' and lineResult == '.':
            result = '.'
            

    printString =  "Case #" + str((boardNum + 1)) + ": "

    if result == 'D':
        printString += "Draw"
    if result == '.':
        printString += "Game has not completed"
    if result == 'X':
        printString += "X won"
    if result == 'O':
        printString += "O won"

    printString += "\n"

    fileOut.write(printString)

    file.readline(attempt)

fileOut.close()
attempt.close()
        

        
