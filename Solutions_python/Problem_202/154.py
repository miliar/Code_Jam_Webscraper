import math, sys
from copy import deepcopy

def nope_rc(board, r, c):
    for n in range(N):
        board[r][n] = True

    for n in range(N):
        board[n][c] = True

    return board

def nope_diag(board, r, c):
    for n in range(-N,N):
        tr = r+n
        tc = c+n

        if tr >= 0 and tr < N and tc >= 0 and tc < N:
            board[tr][tc] = True

    for n in range(-N,N):
        tr = r-n
        tc = c+n

        if tr >= 0 and tr < N and tc >= 0 and tc < N:
            board[tr][tc] = True

    return board

def solve_x(board_x, N):
    nopes = [[False]*N for n in range(N)]

    # nope out existing
    for r in range(N):
        for c in range(N):
            if board_x[r][c]:
                nopes = nope_rc(nopes, r, c)

    for r in range(N):
        for c in range(N):
            if not nopes[r][c]:
                board_x[r][c] = True
                nopes = nope_rc(nopes, r, c)
    return board_x

def solve_p(board_p, N):
    nopes = [[False]*N for n in range(N)]

    # nope out existing
    for r in range(N):
        for c in range(N):
            if board_p[r][c]:
                nopes = nope_diag(nopes, r, c)

    for r in [0, N-1]:
        for c in range(N):
            if not nopes[r][c]:
                board_p[r][c] = True
                nopes = nope_diag(nopes, r, c)
    return board_p

def gen_board(board_x, board_p, N):
    board = [['.'] * N for n in range(N)]

    for r in range(N):
        for c in range(N):
            if board_p[r][c] and board_x[r][c]:
                board[r][c] = 'o'
            elif board_p[r][c]:
                board[r][c] = '+'
            elif board_x[r][c]:
                board[r][c] = 'x'

    return board

def get_score(board_x, board_p, N):
    score = 0

    for r in range(N):
        for c in range(N):
            if board_p[r][c]:
                score += 1

    for r in range(N):
        for c in range(N):
            if board_x[r][c]:
                score += 1

    return score

def get_num_moves(board_init, board_fin, N):
    num_moves = 0
    for r in range(N):
        for c in range(N):
            if board_fin[r][c] != board_init[r][c]:
                num_moves += 1

    return num_moves

def get_moves(board_init, board_fin, N):
    for r in range(N):
        for c in range(N):
            if board_fin[r][c] != board_init[r][c]:
                print board_fin[r][c], r+1, c+1


if __name__ == "__main__":
    sys.stdin = open('D-small-attempt2.in')
    sys.stdout = open('out.txt', 'w')

    T = int(raw_input())

    for t in range(T):
        N, M = [int(x) for x in raw_input().split(" ")]
        board_x = [[False]*N for n in range(N)]
        board_p = [[False]*N for n in range(N)]

        for m in range(M):
            v, r, c = raw_input().split(" ")
            r = int(r)-1
            c = int(c)-1
            if v == 'o':
                board_x[r][c] = True
                board_p[r][c] = True
            elif v == 'x':
                board_x[r][c] = True
            else: 
                board_p[r][c] = True

        board_init = gen_board(board_x, board_p, N)

        board_x = solve_x(deepcopy(board_x), N) 
        board_p = solve_p(deepcopy(board_p), N) 

        board_fin = gen_board(board_x, board_p, N)

        print "Case #%d: %d %d" % (t+1, get_score(board_x, board_p, N), get_num_moves(board_init, board_fin, N))
        get_moves(board_init, board_fin, N)

#        print N, get_score(board_init, board_fin, N)

#        b = gen_board(board_x, board_p, N)

#        for n in range(N):
#            print ' '.join(b[n])
