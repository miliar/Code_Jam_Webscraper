import sys
import string

# Arguments: [in] [out]
# Defaults: in='input.txt', out=stdout

lines = [[0,4,8,12],
        [1,5,9,13],
        [2,6,10,14],
        [3,7,11,15],
        
        [ 0, 1, 2, 3],
        [ 4, 5, 6, 7],
        [ 8, 9,10,11],
        [12,13,14,15],
        
        # diagonal
        [0,5,10,15],
        [3,6,9,12]
        ]
def has_win(s,ch):
    for line in lines:
        win = True
        for i in line:
            win = win and (s[i] == ch or s[i] == 'T') 
        if win:
            return win
    return win


if len(sys.argv) > 1:
    input_file = len(sys.argv)>1 and sys.argv[1] or 'input.txt'
    outf = len(sys.argv)>2 and open(sys.argv[2],'w') or sys.stdout
    with open(input_file) as f:
        T = int(f.readline())
        for x in range(T):
            b = []
            b.append(f.readline().strip())
            b.append(f.readline().strip())
            b.append(f.readline().strip())
            b.append(f.readline().strip())
            f.readline() # skip blank line
            board = ''.join(b)
            assert(len(board) == 16)
            assert (board.count('X') == board.count('O') or
                    board.count('X') == board.count('O')+1)
            moves = board.count('X') + board.count('O')
            turn = moves % 2
            result = 'Game has not completed'
            if board.count('.') == 0:
                result = 'Draw'
            if turn == 0: # 'O' just moved, it is 'X' to move now
                if has_win(board, 'O'):
                    result = 'O won'
            if turn == 1:
                if has_win(board, 'X'):
                    result = 'X won'
            
            outf.write('Case #{0}: '.format(x+1))
            outf.write(result)
            outf.write('\n')
