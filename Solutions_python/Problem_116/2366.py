X_WINNER = 1
O_WINNER = 0

DIM = 4

def handle_config(line):

    winner = None
    if '.' in line:
        full = False
        return (full, winner)
    else:
        full = True

    set_line = set(line)
    set_t = set('T')

    new_set_line = set_line - set_t

    if len(new_set_line) == 1:
        winner = new_set_line.pop()

    return (full, winner)

def handle_board(board):

    global_full = True
    for i in xrange(DIM):
        cur_line = [board[i][j] for j in xrange(DIM)]
        (full, winner) = handle_config(cur_line)
        global_full = global_full and full
        if winner is not None:
            return (global_full, winner)

        cur_col = [board[j][i] for j in xrange(DIM)]
        (full, winner) = handle_config(cur_col)
        global_full = global_full and full
        if winner is not None:
            return (global_full, winner)
        

    left_diag = [board[i][i] for i in xrange(DIM)]
    (full, winner) = handle_config(left_diag)
    global_full = global_full and full
    if winner is not None:
        return (global_full, winner)


    right_diag = [board[i][DIM - i - 1] for i in xrange(DIM)]
    (full, winner) = handle_config(right_diag)
    global_full = global_full and full
    if winner is not None:
        return (global_full, winner)

    return (global_full, winner)


def solve(input_path):
    with open(input_path) as f:
        num_of_boards = int(f.readline())
        for i in xrange(num_of_boards):
            board = [[0 for _ in xrange(DIM)] for _ in xrange(DIM)]
            for j in xrange(DIM):
                line = f.readline()
                line = line[:DIM]
                for k, c in enumerate(line):
                    board[j][k] = c
            
            (full, winner) = handle_board(board)
            base_string = 'Case #%d: ' % (i + 1,)
            if winner is not None:
                print base_string + winner + ' won'
            else:
                if full:
                    print base_string + 'Draw'
                else:
                    print base_string + 'Game has not completed'

            f.readline()


if __name__ == "__main__":
    solve('input')
    pass
