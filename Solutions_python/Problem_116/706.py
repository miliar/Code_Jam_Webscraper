def compute(board):
    def f(seq):
        nx = sum(1 for x in seq if x == 'X')
        no = sum(1 for x in seq if x == 'O')
        t = 'T' in seq
        if nx == 4 or nx == 3 and t:
            print 'X won'
            return 1
        if no == 4 or no == 3 and t:
            print 'O won'
            return 1
        return 0

    for line in board:
        if f(line):
            return
    for j in xrange(4):
        col = [board[i][j] for i in xrange(4)]
        if f(col):
            return

    diag = [board[i][i] for i in xrange(4)]
    if f(diag):
        return

    diag = [board[i][3-i] for i in xrange(4)]
    if f(diag):
        return

    if any('.' in line for line in board):
        print 'Game has not completed'
        return

    print 'Draw'


def run():
    T = int(raw_input())
    for i in xrange(T):
        board = []
        for _ in xrange(4):
            board.append(raw_input())
        print 'Case #%d:' % (i + 1),
        compute(board)
        raw_input()

if __name__ == '__main__':
    run()
