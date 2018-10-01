def check4(spots):
    if all(s in 'XT' for s in spots):
        return 'X won'
    if all(s in 'OT' for s in spots):
        return 'O won'
    return None

def row(board, i):
    return board[i]

def column(board, i):
    return [b[i] for b in board]

def diag1(board):
    return [board[i][i] for i in [0, 1, 2, 3]]

def diag2(board):
    return [board[i][3-i] for i in [0, 1, 2, 3]]


def solve(board):
    print 'solving'
    print '\n'.join(board),
    for i in range(4):
        c = check4(row(board, i))
        if c:
            return c
        c = check4(column(board, i))
        if c:
            return c

    c = check4(diag1(board))
    if c:
        return c

    c = check4(diag2(board))
    if c:
        return c

    done = all(s != '.' for row in board for s in row)
    if done:
        return 'Draw'

    return 'Game has not completed'


def main(fname):
    data = open(fname + '.in').readlines()
    data = [d.strip() for d in data]

    T = int(data[0])
    data = data[1:]

    with open(fname + '.out', 'w') as outfile:
        for i in range(T):
            board = data[5 * i: 5 * i + 4]
            result =  solve(board)

            outfile.write("Case #%i: %s\n" % (i+1, result))
            print result


if __name__ == "__main__":
    import sys
    main(sys.argv[1])
