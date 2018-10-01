'''
Created on Apr 13, 2013

@author: Sean Groathouse
'''

fin = open('A-large.in', 'r')
finput = fin.readlines()
fin.close()
it = iter(finput)
numbCases = (int)(it.next())
output = ""

for case in xrange(numbCases):
    grid = list()
    for i in range(4):
        row = (it.next()).rstrip()
        grid.append(row)
    if case < numbCases-1:
        it.next() # Get rid of the blank line
    winner = -1 # 0 for O winning, 1 for X winning
    
    # Test the rows
    for row in range(4):
        numX = 0
        numO = 0
        numT = 0
        for column in range(4):
            if grid[row][column] == 'T':
                numT += 1
            elif grid[row][column] == 'O':
                numO += 1
            elif grid[row][column] == "X":
                numX += 1
        if (numX == 4) or (numX == 3 and numT == 1):
            winner = 1
            break
        elif (numO == 4) or (numO == 3 and numT == 1):
            winner = 0
            break
    
    # If no winner, check the columns
    if winner == -1:
        for column in range(4):
            numX = 0
            numO = 0
            numT = 0
            for row in range(4):
                if grid[row][column] == 'T':
                    numT += 1
                elif grid[row][column] == 'O':
                    numO += 1
                elif grid[row][column] == "X":
                    numX += 1
            if (numX == 4) or (numX == 3 and numT == 1):
                winner = 1
                break
            elif (numO == 4) or (numO == 3 and numT == 1):
                winner = 0
                break
    
    # If no winner, check the first diagonal
    if winner == -1:
        numX = 0
        numO = 0
        numT = 0
        for i in range(4):
            if grid[i][i] == 'T':
                numT += 1
            elif grid[i][i] == 'O':
                numO += 1
            elif grid[i][i] == "X":
                numX += 1
        if (numX == 4) or (numX == 3 and numT == 1):
            winner = 1
        elif (numO == 4) or (numO == 3 and numT == 1):
            winner = 0
    
    # If no winner, check the second diagonal
    if winner == -1:
        numX = 0
        numO = 0
        numT = 0
        for i in range(4):
            if grid[i][3-i] == 'T':
                numT += 1
            elif grid[i][3-i] == 'O':
                numO += 1
            elif grid[i][3-i] == "X":
                numX += 1
        if (numX == 4) or (numX == 3 and numT == 1):
            winner = 1
        elif (numO == 4) or (numO == 3 and numT == 1):
            winner = 0
    
    # If still no winner, determine if game is over
    if winner == -1:
        finished = True
        for i in range(4):
            for j in range(4):
                if grid[i][j] == ".":
                    finished = False
    
    # Determine the status string
    if winner == 1:
        status = "X won"
    elif winner == 0:
        status = "O won"
    elif finished:
        status = "Draw"
    else:
        status = "Game has not completed"
    
    output += "Case #%d: %s\n" % (case+1, status)
    
    
fout = open('large.txt', 'w')
fout.write(output)
fout.close