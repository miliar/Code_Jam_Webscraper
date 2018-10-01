f = open('1.ex', 'r')
fo = open('1.out' ,'w')

cases = int(f.readline())

for c in xrange(cases):
    
    board = []
    empty_space = False
    
    for i in xrange(4):
        row = f.readline().strip()
        board.append(row)
        if not empty_space and '.' in row:
            empty_space = True
    f.readline()
        
    winning_symbol = None
    
    # Check horizontal
    for row in board:
        row_symbol = None
        for symbol in row:
            if symbol == '.':
                row_symbol = None
                break
            elif symbol == 'T':
                continue
            if not row_symbol:
                row_symbol = symbol
            elif not row_symbol == symbol and not symbol == 'T':
                row_symbol = None
                break
        if row_symbol:
            # Iemand heeft gewonnen
            winning_symbol = row_symbol
            break
    
    if not winning_symbol:
        # Check vertical
        for column in xrange(4):
            column_symbol = None
            for row in xrange(4):
                symbol = board[row][column]
                if symbol == '.':
                    column_symbol = None
                    break
                elif symbol == 'T':
                    continue
                if not column_symbol:
                    column_symbol = symbol
                elif not column_symbol == symbol and not symbol == 'T':
                    column_symbol = None
                    break
            if column_symbol:
                # Iemand heeft gewonnen
                winning_symbol = column_symbol
                break
    
    if not winning_symbol:
        # Check diagonal
        diag_symbol = None
        for i in xrange(4):
            symbol = board[i][i]
            if symbol == '.':
                diag_symbol = None
                break
            elif symbol == 'T':
                continue
            if not diag_symbol:
                diag_symbol = symbol
            elif not diag_symbol == symbol and not symbol == 'T':
                diag_symbol = None
                break
        if diag_symbol:
            winning_symbol = diag_symbol
    
    if not winning_symbol:
        # Check other diagonal
        diag_symbol = None
        for i in xrange(4):
            symbol = board[i][3-i]
            if symbol == '.':
                diag_symbol = None
                break
            elif symbol == 'T':
                continue
            if not diag_symbol:
                diag_symbol = symbol
            elif not diag_symbol == symbol and not symbol == 'T':
                diag_symbol = None
                break
        if diag_symbol:
            winning_symbol = diag_symbol
    
    if winning_symbol:
        # Somebody won
        result = winning_symbol + ' won'
    elif empty_space:
        result = 'Game has not completed'
    else:
        result = 'Draw'
    
    fo.write('Case #' + str(c+1) + ': ' + str(result) + '\n')