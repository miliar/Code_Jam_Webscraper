def line_winner(board,line):
    x_in = False
    o_in = False
    space_in = False
    
    for spot in line:
        c = board[spot[0]][spot[1]]
        x_in = (c == "X") or x_in
        o_in = (c == "O") or o_in
        space_in = (c == ".") or space_in
    
    if space_in:
        return "."
    if (x_in and o_in):
        return "D"
    if x_in:
        return "X"
    if o_in:
        return "O"

z_thru_4 = range(4)
lines = [zip(z_thru_4,[0]*4),
         zip(z_thru_4,[1]*4),
         zip(z_thru_4,[2]*4),
         zip(z_thru_4,[3]*4),
         zip([0]*4,z_thru_4),
         zip([1]*4,z_thru_4),
         zip([2]*4,z_thru_4),
         zip([3]*4,z_thru_4),
         zip(z_thru_4,z_thru_4),
         zip(z_thru_4,reversed(z_thru_4))]

def board_winner(board):
    boardFull = True
    for line in lines:
        w = line_winner(board, line)
        if w == "X":
            return "X won"
        if w == "O":
            return "O won"
        if w == ".":
            boardFull = False
    if not boardFull:
        return "Game has not completed"
    return "Draw"

inputFile = "A-large.in"
outputFile = "goog_code_jam_1.out"

f = open(inputFile)
T = int(f.readline())
boards = f.readlines(100000000)

with open(outputFile, 'w') as o:
    for i in range(T):
        b = boards[:4]
        boards = boards[5:]
        o.write("Case #{0}: {1}\n".format(i+1, board_winner(b)))


