def solve(board):
    # print board
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            vert = True
            hor = True
            for jj in xrange(len(board[0])):
                if board[i][jj]>board[i][j]:
                    hor = False
                    break

            for ii in xrange(len(board)):
                if board[ii][j]>board[i][j]:
                    vert = False
                    break
            if not vert and not hor:
                return False
    return True


if __name__ == '__main__':
    import sys
    l = [x.strip() for x in open(sys.argv[1]).readlines()]
    count = int(l[0])
    next = 1
    for i in xrange(count):
        n,m = map(int,l[next].split())
        next+=1
        # import pdb; pdb.set_trace()
        board = [[int(cell) for cell in row.split()] for row in l[next:next+n]]
        ret = solve(board)
        next += n
        print "Case #%s: %s" % (i + 1, "YES" if ret else "NO")
