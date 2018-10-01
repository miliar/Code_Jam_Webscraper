#!/usr/bin/python

fp = open('p1.in')

games = int(fp.readline())
trial = 0

def hasWon(grid, player):


    tt = 0
    mmatch = 0
    
    for i in range(4):
        if grid[i][4-i-1] == 'T':
            tt = tt + 1
        elif grid[i][4-i-1] == player:
            mmatch = mmatch + 1

    if mmatch == 4: 
            return True
    elif mmatch == 3 and tt == 1:
            return True

    # Forward Diagonal 
    tt = 0
    mmatch = 0
    
    for i in range(4):
        if grid[i][i] == 'T':
            tt = tt + 1
        elif grid[i][i] == player:
            mmatch = mmatch + 1

    if mmatch == 4: 
            return True
    elif mmatch == 3 and tt == 1:
            return True            

    # Vertical
    for i in range(4):
        t = 0
        match = 0
        for j in range(4):
            if grid[j][i] == 'T':
                t = t + 1
            elif grid[j][i] == player:
                match = match + 1
        if match == 4: 
            return True
        elif match == 3 and t == 1:
            return True 
   
    # Horizontal
    for i in range(4):
        t = 0
        match = 0
        for j in range(4):
            if grid[i][j] == 'T':
                t = t + 1
            elif grid[i][j] == player:
                match = match + 1
        if match == 4: 
            return True
        elif match == 3 and t == 1:
            return True 

    
    return False

def hasEmpty(grid):
    for row in grid:
        for item in row:
            if item == '.':
                return True 
    return False


while games > 0:
    trial = trial + 1
    c = 0
    grid = []
    while c < 4:
        grid.append(fp.readline()[:-1])
        c = c + 1
        
    if hasWon(grid, 'X'):
        print "Case #%d: X won" % (trial)
    elif hasWon(grid, 'O'):
        print "Case #%d: O won" % (trial)
    elif hasEmpty(grid):
        print "Case #%d: Game has not completed" % (trial)
    else:
        print "Case #%d: Draw" % (trial)
    
    fp.readline()
    games = games - 1

#print games