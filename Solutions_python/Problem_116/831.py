msquare = [[9, 6, 3, 16],
           [4, 15, 10, 5],
           [14, 1, 8, 11],
           [7, 12, 13, 2]]

tries = raw_input()

for i in range(0, int(tries)):
    updown = []
    
    for x in range(0, 4):
        across = []
        line = raw_input()
        for y in range(0, 4):
            across.append(line[y])
        updown.append(across)

    raw_input()

    xscore = 0
    oscore = 0
    dotcount = 0
    
# left and right
    for x in range(0, 4):
        xscore = 0
        oscore = 0
        for y in range(0, 4):
            if (updown[x][y] == "X" or updown[x][y] == "T"):
                xscore += msquare[x][y]
                    
            if (updown[x][y] == "O" or updown[x][y] == "T"):
                oscore += msquare[x][y]

            if (updown[x][y] == "."):
                dotcount += 1
                
        if (oscore == 34): break
        elif (xscore == 34): break

# up and down
    if (xscore != 34 and oscore != 34):

        for y in range(0, 4):
            xscore = 0
            oscore = 0
            for x in range(0, 4):
                if (updown[x][y] == "X" or updown[x][y] == "T"):
                    xscore += msquare[x][y]
                        
                if (updown[x][y] == "O" or updown[x][y] == "T"):
                    oscore += msquare[x][y]
                    
            if (oscore == 34): break
            elif (xscore == 34): break
            
    if (xscore != 34 and oscore != 34):
        xscore = 0
        oscore = 0

        for z in range (0, 4):
            if (updown[z][z] == "X" or updown[z][z] == "T"):
                xscore += msquare[z][z]
                        
            if (updown[z][z] == "O" or updown[z][z]== "T"):
                oscore += msquare[z][z]

    if (xscore != 34 and oscore != 34):
        xscore = 0
        oscore = 0

        for z in range (0, 4):
            if (updown[z][3-z] == "X" or updown[z][3-z] == "T"):
                xscore += msquare[z][3-z]
                        
            if (updown[z][3-z] == "O" or updown[z][3-z] == "T"):
                oscore += msquare[z][3-z]

    s = "Case #"
    s += str(i+1)
    s += ": "

    if (xscore == 34): s += "X won"
    elif (oscore == 34): s+= "O won"
    elif (dotcount > 0): s += "Game has not completed"
    else: s += "Draw"

    print s
