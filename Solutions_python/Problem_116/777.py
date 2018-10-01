# python 3

WILDCARD = 'T'
EMPTY = '.'
BOARD_SIZE = 4

X_WINS = 'X'
O_WINS = 'O'
INCOMPLETE = 'incomplete'
DRAW = 'draw'

X_WIN_MSG = 'X won'
O_WIN_MSG = 'O won'
INCOMPLETE_MSG = 'Game has not completed'
DRAW_MSG = 'Draw'
MSG_DICT = {X_WINS: X_WIN_MSG,
            O_WINS: O_WIN_MSG,
            INCOMPLETE: INCOMPLETE_MSG,
            DRAW: DRAW_MSG}

def read_input():
    num_cases = int(input())
    games = []
    for j in range(num_cases):
        games.append([list(input()) for i in range(BOARD_SIZE)])
        input()  # ignore blank line after each game
        
    return games

    
def check_row(row):
    # check row
    # returns X, O, draw, or incomplete
    all_x = True
    all_o = True
    
    for c in row:
        if c == EMPTY:
            return INCOMPLETE
        elif c != 'X' and c != WILDCARD:
            all_x = False
        elif c != 'O' and c != WILDCARD:
            all_o = False
        
    if all_x:
        return X_WINS
    if all_o:
        return O_WINS
    
    return DRAW
        
        
def check_rows(rows):
    incomplete = False
    
    for row in rows:
        result = check_row(row)
        if result == X_WINS or result == O_WINS:
            return result
        elif result == INCOMPLETE:
            # draw is no longer possible as there is still at least one empty field
            incomplete = True
    
    if incomplete:
        return INCOMPLETE
    return DRAW
        
        
def check_game(gs):
    # gs = game state, list of BOARD_SIZE lists
    # get rows, columns, and diagonals as a single list of rows to check
    check_list = []
    
    # rows
    for row in gs:
        check_list.append(row)# rows
    # columns
    cols = [[row[i] for row in gs] for i in range(BOARD_SIZE)]
    for row in cols:
        check_list.append(row)
    # diagonals
    check_list.append([gs[i][i] for i in range(BOARD_SIZE)])
    check_list.append([gs[i][j] for i, j in zip(range(BOARD_SIZE), range(BOARD_SIZE-1, -1, -1))])
    
    return check_rows(check_list)
    

if __name__ == '__main__':
    games = read_input()
    for i in range(len(games)):
        result = check_game(games[i])
        msg = MSG_DICT[result]
        print('Case #{0}: {1}'.format(i+1, msg))