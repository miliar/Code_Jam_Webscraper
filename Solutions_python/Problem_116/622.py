ncases = int(raw_input())
for caseno in xrange(1, ncases+1):
    board = ''.join(raw_input().strip() for i in xrange(4))
    raw_input() # for empty line

    allquads = [
        board[0:4], board[4:8], board[8:12], board[12:16], # row
        board[0::4], board[1::4], board[2::4], board[3::4], # col
        board[0::5], board[3:15:3] # diag
    ]

    if 'XXXX' in allquads or 'XXXT' in allquads or 'TXXX' in allquads:
        result = 'X won'
    elif 'OOOO' in allquads or 'OOOT' in allquads or 'TOOO' in allquads:
        result = 'O won'
    elif '.' in board:
        result = 'Game has not completed'
    else:
        result = 'Draw'
    print 'Case #%d: %s' % (caseno, result)
