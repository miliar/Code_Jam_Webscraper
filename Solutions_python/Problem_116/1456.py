'''
Created on Apr 13, 2013

@author: steve
'''
T = int(input())
for Ti in range(1, T+1):
    
    Board = [input() for i in range(4)]
    input() # Clear empty line
    BoardO = [l.replace('T','O') for l in Board]
    BoardX = [l.replace('T','X') for l in Board]
    
    print('Case #%d:' % Ti, end=' ')
    
    # Check for O Victory
    if ('O' == BoardO[0][0] == BoardO[1][1] == BoardO[2][2] == BoardO[3][3]):
        print('O won')
        continue
    if ('O' == BoardO[0][3] == BoardO[1][2] == BoardO[2][1] == BoardO[3][0]):
        print('O won')
        continue
    victory = False
    for i in range(4):
        if ('O' == BoardO[i][0] == BoardO[i][1] == BoardO[i][2] == BoardO[i][3]):
            print('O won')
            victory = True
            break
        if ('O' == BoardO[0][i] == BoardO[1][i] == BoardO[2][i] == BoardO[3][i]):
            print('O won')
            victory = True
            break
    if victory: continue
    
    # Check for X Victory
    victory = False
    if ('X' == BoardX[0][0] == BoardX[1][1] == BoardX[2][2] == BoardX[3][3]):
        print('X won')
        continue
    if ('X' == BoardX[0][3] == BoardX[1][2] == BoardX[2][1] == BoardX[3][0]):
        print('X won')
        continue
    for i in range(4):
        if ('X' == BoardX[i][0] == BoardX[i][1] == BoardX[i][2] == BoardX[i][3]):
            print('X won')
            victory = True
            break
        if ('X' == BoardX[0][i] == BoardX[1][i] == BoardX[2][i] == BoardX[3][i]):
            print('X won')
            victory = True
            break
    if victory: continue
    
    # Check for draw
    draw = True
    for i in range(4):
        for j in range(4):
            if draw and Board[i][j] == '.':
                draw = False
    if draw:
        print('Draw')
    else:
        print('Game has not completed')
                
    