lines = [line.strip() for line in open('large_input.txt').readlines() if line.strip()]
num_boards = int(lines[0])
phrases = ["X won", "O won", "Draw", "Game has not completed"]

def winner(row):
    if all([r=='X' or r=='T' for r in row]):
        return phrases[0]
    if all([r=='O' or r=='T' for r in row]):
        return phrases[1]

def status(board):
    for i in range(4):
        x = winner([board[i][j] for j in range(4)])
        if x:
            return x
        y = winner([board[j][i] for j in range(4)])
        if y:
            return y
    z = winner([board[j][j] for j in range(4)])
    if z:
        return z
    w = winner([board[j][3-j] for j in range(4)])
    if w:
        return w

    for row in board:
        for cell in row:
            if cell == '.':
                return phrases[3]

    return phrases[2]

for i in range(num_boards):
    board = lines[4*i+1:4*i+5]
    print 'Case #%i: %s' % (i+1, status(board))
