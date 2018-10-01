O = ['O']*4
X = ['X']*4
  
def row(board):
    for row in range(4):
        if board[row] == O or (board[row].count('O') == 3 and 'T' in board[row]):
            return 'O won'
        elif board[row] == X or (board[row].count('X') == 3 and 'T' in board[row]):
            return 'X won'
                     
def column(board):
    new = []
    for column in range(4):
        new.append([board[0][column],board[1][column],board[2][column],board[3][column]])
    return row(new)
            
def diagonal(board):
    left = []
    right = []
    special = []
    for i in range(4):
        left.append(board[i][i])
        right.append(board[i][3-i])
    if left == O or (left.count('O') == 3 and 'T' in left):
        return 'O won'
    elif left == X or (left.count('X') == 3 and 'T' in left):
        return 'X won'
    if right == O or (right.count('O') == 3 and 'T' in right):
        return 'O won'
    elif right == 'X' or (right.count('X') == 3 and 'T' in right):
        return 'X won'
        
def tic_tac_toe(board):
    r = row(board)
    if r:
        return r
    c = column(board)
    if c:
        return c
    d = diagonal(board)
    if d:
        return d
    if '.' in str(board):
        return 'Game has not completed'
    return 'Draw'  
            
    
f = open('A-small-attempt2.in','r')
output = open('tictactoeresultsmall.txt','w')
lines = f.readline()
for i in range(int(lines)):
    board = []
    for j in range(4):
        board.append([x for x in f.readline() if x != '\n'])
    print(board)
    result = tic_tac_toe(board)
    f.readline()
    output.write('Case #{0}: {1}\n'.format(i+1, result))
f.close()
output.close()
    