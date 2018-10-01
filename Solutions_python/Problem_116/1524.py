file = open("ticTacToeTomek")
T = int(file.readline())

count = 1
for num in range(T):
    
    board = []
    for num in range(4):
        board.append(file.readline().replace('\n',''))
    file.readline()
    
    Oboard = board
    newOboard = []
    for line in Oboard:
        line = line.replace('T', 'O')
        newOboard.append(line)
    
    Xboard = board
    newXboard = []
    for line in Xboard:
        line = line.replace('T', 'X')
        newXboard.append(line)
    
    p = 0
    
    for line in newOboard:
        if line == 'OOOO':
            print  "Case #" + str(count) + ": O won"
            p=1
    
    for line in newXboard:
        if line == 'XXXX':
            print  "Case #" + str(count) + ": X won"
            p=1
    
    if newXboard[0][0] == 'X' and newXboard[1][1] == 'X' and newXboard[2][2] == 'X' and newXboard[3][3] == 'X' and p == 0:
        print  "Case #" + str(count) + ": X won"
        p=1
    
    if newOboard[0][0] == 'O' and newOboard[1][1] == 'O' and newOboard[2][2] == 'O' and newOboard[3][3] == 'O' and p == 0:
        print  "Case #" + str(count) + ": O won"
        p=1
        
    if newXboard[3][0] == 'X' and newXboard[2][1] == 'X' and newXboard[1][2] == 'X' and newXboard[0][3] == 'X' and p == 0:
        print  "Case #" + str(count) + ": X won"
        p=1
    
    if newOboard[3][0] == 'O' and newOboard[2][1] == 'O' and newOboard[1][2] == 'O' and newOboard[0][3] == 'O' and p == 0:
        print  "Case #" + str(count) + ": O won"
        p=1
    
    for v in range(4):    
        if newOboard[0][v] == 'O' and newOboard[1][v] == 'O' and newOboard[2][v] == 'O' and newOboard[3][v] == 'O' and p == 0:
            print  "Case #" + str(count) + ": O won"
            p=1
    
    for v in range(4):    
        if newXboard[0][v] == 'X' and newXboard[1][v] == 'X' and newXboard[2][v] == 'X' and newXboard[3][v] == 'X' and p == 0:
            print  "Case #" + str(count) + ": X won"
            p=1
    
    if not '.' in line in newXboard and p ==0:
        print  "Case #" + str(count) + ": Draw"
        p=1
    
    if p == 0:
        print "Case #" + str(count) + ": Game has not completed"
                
    count += 1
    

