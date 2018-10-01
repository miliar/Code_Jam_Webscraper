import math
import copy
numCases = int(raw_input())
for n in range(numCases):
    xwon = False
    owon = False
    notfinished = False
    gamestate = []
    BLAN = 0
    XWON = 1
    OWON = 2
    NDOT = 4
        
    
    def check(input):
        BLAN = 0
        XWON = 1
        OWON = 2
        NDOT = 4
        
        won = True
        ranonce = False

        for char in input:
            if char == ".":
                return BLAN
                
        for char in input:        
            if char == "T":
                temp = "temp"
            elif ranonce:
                if char != charcheck:
                    return NDOT
                    
            else:
                charcheck = char
                ranonce = True
        if won:
            if charcheck == "X":
                return XWON
                
            else:
                return OWON
    
    
    for i in range(4):
        row = raw_input()
        gamestate.append(row)
    if n < numCases-1:
        raw_input()
        
    #Builds a transpose and appends to gamestate
    gamestate2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):
            gamestate2[i][j] = gamestate[j][i]
    gamestate3 = []
    for row in gamestate2:
        x = ""
        for char in row:
            x += char
        gamestate.append(x)
     
    #check
    
    #Vert check
    
    #Diagonal check
    row = ""
    for i in range(4):
        row += gamestate[i][i]
    gamestate.append(row)

    row = ""
    for i in range(4):
        row += gamestate[i][3-i]
    gamestate.append(row)
    
    for row in gamestate:
        state = check(row)
        if state == XWON:
            xwon = True
        elif state == OWON:
            owon = True
        elif state == BLAN:
            notfinished = True
        
    
    
    #Output check
    if xwon:
        outputstring = "X won"
    elif owon:
        outputstring = "O won"
    elif notfinished:
        outputstring = "Game has not completed"
    else:
        outputstring = "Draw"
    
    print "Case #{0}: ".format(str(n+1)) + outputstring
