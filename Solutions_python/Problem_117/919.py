cases = int(raw_input())
case = 1

while case <= cases:
    
    rows, cols = [int(i) for i in raw_input().split()]
    game = []
    rowmax = [0 for i in range(rows)]
    colmax = [0 for i in range(cols)]
    
    for row in range(rows):
        game.append([int(i) for i in raw_input().split()])
        
    for row in range(rows):
        rowmax[row] = max(game[row])
        
    for col in range(cols):
        m = 0
        for row in range(rows):
            if game[row][col] > m:
                m = game[row][col]
        colmax[col] = m
    
    bad = False
    for row in range(rows):
        for col in range(cols):
            if (rowmax[row] > game[row][col]) and (colmax[col] > game[row][col]):
                bad = True
                break
        if bad:
            break
            
    if bad:
        print "Case #" + str(case) + ": NO"
    else:
        print "Case #" + str(case) + ": YES"
    case += 1
