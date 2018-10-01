import sys

def solve(board):
    m = len(board)
    n = len(board[0])
    for i, row in enumerate(board):
        maxrow = max(row)
        for j, number in enumerate(row):
            maxcol = max([board[x][j] for x in xrange(m)])
            try:
                assert number >= maxrow or number >= maxcol
            except AssertionError:
                return False
    return True

def single_case():
    alln = raw_input().strip().split(" ")
    m, n = alln
    m = int(m)
    n = int(n)
    board = []
    for row in xrange(m):
        line = [int(i) for i in raw_input().strip().split(" ")]
        board.append(line)
    if m == n == 1:
        return True
    return solve(board)

messages = {
    True: 'YES',
    False: 'NO',
}

t = int(raw_input())
for i in xrange(t):
    outcome = single_case()
    print "Case #{0}: {1}".format(i+1, messages[outcome])
