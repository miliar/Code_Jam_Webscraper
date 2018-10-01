cases = int(raw_input())

for case in xrange(cases):
    board = []
    winner = ''
    complete = True

    for r in xrange(4):
        row_in = raw_input()
        if '.' in row_in:
            complete = False
        board.append(list(row_in))
    raw_input()  # Take empty line following case

    # Check horizontal
    for row in board:
        start = row[0]
        if start == 'T':
            start = row[1]
        for col in row:
            if col == '.' or (col != start and col != 'T'):
                break
        else:
            winner = start
    
    if winner:
        print 'Case #%d: %s won' % (case+1, winner)
        continue

    # Check vertical:
    for c in xrange(4):
        start = board[0][c]
        if start == 'T':
            start = board[1][c]
        for r in xrange(4):
            spot = board[r][c]
            if spot == '.' or (spot != start and spot != 'T'):
                break
        else:
            winner = start

    if winner:
        print 'Case #%d: %s won' % (case+1, winner)
        continue

    # Check diagonals:
    start_l = board[0][0]
    if start_l == 'T':
        start_l = board[1][1]

    for s in xrange(4):
        spot = board[s][s]
        if spot == '.' or (spot != start_l and spot != 'T'):
            break
    else:
        winner = start_l

    if winner:
        print 'Case #%d: %s won' % (case+1, winner)
        continue

    start_r = board[0][-1]
    if start_r == 'T':
        start_r = board[1][-2]

    for s in xrange(4):
        spot = board[s][-s-1]
        if spot == '.' or (spot != start_r and spot != 'T'):
            break
    else:
        winner = start_r

    if winner:
        print 'Case #%d: %s won' % (case+1, winner)
        continue

    if complete:
        print 'Case #%d: Draw' % (case+1)
    else:
        print 'Case #%d: Game has not completed' % (case+1)

