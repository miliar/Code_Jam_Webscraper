
import itertools
WINNING_X = set(["XXXX", "XXXT", "XXTX", "XTXX", "TXXX"])
WINNING_O = set(["OOOO", "OOOT", "OOTO", "OTOO", "TOOO"])
WINNING = WINNING_X.union(WINNING_O)

def row_at(board, i):
    return board[i]

def col_at(board, i):
    return board[0][i] + board[1][i] + board[2][i] + board[3][i]

def main_diag(board):
    return board[0][0] + board[1][1] + board[2][2] + board[3][3]

def rev_diag(board):
    return board[0][3] + board[1][2] + board[2][1] + board[3][0]

def analyze_board(board):
    rows = [row_at(board, i) for i in range(4)]
    cols = [col_at(board, i) for i in range(4)]
    diag = [main_diag(board), rev_diag(board)]

    opts = rows + cols + diag
    for sol in opts:
        if sol in WINNING_X:
            return "X"
        elif sol in WINNING_O:
            return "O"
    return "D" # no-one

def has_empty_space(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == ".":
                return True
    return False



def solve(input_filename, output_filename):
    input_lines = [x.strip() for x in open(input_filename).readlines()]
    output_lines = []
    cases = []

    num_cases = int(input_lines[0])
    for i in xrange(num_cases):
        cases.append(input_lines[i*5+1:(i+1)*5])

    for idx, board in enumerate(cases):
        status = analyze_board(board)
        msg = None
        if status == "X":
            msg = "X won"
        elif status == "O":
            msg = "O won"
        else:
            if has_empty_space(board):
                msg = "Game has not completed"
            else:
                msg = "Draw"

        output_lines.append("Case #%s: %s\n" % (idx+1, msg))

    open(output_filename, "w").writelines(output_lines)
        
        
