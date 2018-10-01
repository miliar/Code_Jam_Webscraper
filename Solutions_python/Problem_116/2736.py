def analysis(board):
    any_empty = False

    for i in xrange(len(board)):
        last_in_row = board[i][0]
        if last_in_row == 'T':
            last_in_row = board[i][1]

        last_in_column = board[0][i]
        if last_in_column == 'T':
            last_in_column = board[1][i]

        if last_in_row != '.' and last_in_column != '.':
            row_winner = True
            column_winner = True

            for j in xrange(1, len(board[0])):
                # Rows
                if board[i][j] == '.':
                    row_winner = False
                    any_empty = True
                if row_winner and board[i][j] != last_in_row and \
                        board[i][j] != 'T':
                    row_winner = False

                # Columns
                if column_winner:
                    if board[j][i] == '.':
                        column_winner = False
                    elif board[j][i] != last_in_column and \
                        board[j][i] != 'T':
                        column_winner = False

            if column_winner:
                return last_in_column + ' won'
            elif row_winner:
                return last_in_row + ' won'
        else:
            any_empty = True

    # Diagonal 1
    diagonal_winner = True
    last_in_diagonal = board[0][0]
    if last_in_diagonal == 'T':
            last_in_diagonal = board[1][1]

    for i in xrange(1, 4):
        if diagonal_winner:
            if board[i][i] != '.':
                if board[i][i] != last_in_diagonal and \
                        board[i][i] != 'T':
                    diagonal_winner = False
            else:
                diagonal_winner = False

    if diagonal_winner:
        return last_in_diagonal + ' won'

    # Diagonal 2
    diagonal_winner = True
    last_in_diagonal = board[3][0]
    if last_in_diagonal == 'T':
            last_in_diagonal = board[1][2]

    range_reversed = range(4)
    range_reversed.reverse()

    for j, i in enumerate(range_reversed):
        if diagonal_winner:
            if board[i][j] != '.':
                if board[i][j] != last_in_diagonal and \
                        board[i][j] != 'T':
                    diagonal_winner = False
            else:
                diagonal_winner = False


    if diagonal_winner:
        return last_in_diagonal + ' won'
    elif any_empty:
        return 'Game has not completed'

    return 'Draw'



def main():
    results = ''

    cases = int(raw_input())

    for i in xrange(cases):
        board = []

        for j in xrange(4):
            row = raw_input()
            board.append([row[0], row[1], row[2], row[3]])

        try:
            raw_input()
        except:
            pass

        print 'Case #' + str(i + 1) + ": " + analysis(board)

if __name__ == "__main__":
    main()
