#!/usr/bin/python

from decimal import *
getcontext().prec = 100
import sys

def reshape(mine_mat):
    for r in range(R):
        for c in range(C):
            sys.stdout.write(mine_mat[r][c])
        sys.stdout.write('\n')

def reshapestr(mine_mat):
    res = ""
    for r in range(R):
        for c in range(C):
            res += str(mine_mat[r][c])
        res += '\n'
    return res.strip()

def add_click(mine_mat):
    mine_mat[-1][-1] = 'c'

def fill_row(mine_mat, num_row, start, end):
    for c in range(start, end + 1):
        mine_mat[num_row][c] = '*'
    # reshape(mine_mat)
    # print ""

def fill_col(mine_mat, num_col, start, end):
    for r in range(start, end + 1):
        mine_mat[r][num_col] = '*'
    # reshape(mine_mat)
    # print ""

def count_star(mine_mat):
    star_cnt = 0
    for r in range(R):
        for c in range(C):
            if mine_mat[r][c] == '*':
                star_cnt += 1
    return star_cnt

def process(R, C, M):
    print R, C, M
    # init
    mine_mat = [['.' for x in range(C)] for x in range(R)]
    # reshape(mine_mat)
    # print ""

    R_cur = R
    C_cur = C
    M_cur = M
    keep_going = 1
    last_mine = 0

    if (R * C) - 1 == M:
        mine_mat = [['*' for x in range(C)] for x in range(R)]
        add_click(mine_mat)
        assert(M == count_star(mine_mat))
        return reshapestr(mine_mat)


    while M_cur > 0 and keep_going == 1:
        if C_cur < 3 and R_cur < 3 and M_cur >= 1:
            keep_going = 0
            continue

        #try to fill the smallest cur dimension
        if R_cur < C_cur:
            if M_cur >= R_cur:
                # fill a line with mines
                fill_col(mine_mat, C - C_cur, R - R_cur, R-1)
                M_cur -= R_cur
                C_cur -= 1
            else:
                # fill the line with remaining mines
                # be carefull: to keep at least 2 space
                if (R_cur - M_cur) == 1:
                    #assert 0==1, "not implemented"
                    fill_col(mine_mat, C - C_cur, R - R_cur, R-3)
                    if last_mine == 1:
                        keep_going = 0
                        continue
                    last_mine = 1
                    M_cur = 1
                    C_cur -= 1

                else:
                    fill_col(mine_mat, C - C_cur, R - R_cur, R - R_cur + M_cur - 1)
                    M_cur = 0
        else:
            if M_cur >= C_cur:
                fill_row(mine_mat, R - R_cur, C - C_cur, C - 1)
                M_cur -= C_cur
                R_cur -= 1
            else:
                if (C_cur - M_cur) == 1:
                    fill_row(mine_mat, R - R_cur, C - C_cur, C - 3)
                    #assert 0==1, "not implemented"
                    # only one mine remaining
                    if last_mine == 1:
                        keep_going = 0
                        continue
                    last_mine = 1
                    M_cur = 1
                    R_cur -= 1

                else:
                    fill_row(mine_mat, R - R_cur, C - C_cur, C - C_cur + M_cur -1)
                    M_cur = 0

    if keep_going == 0:
        return "Impossible"
    else:
        add_click(mine_mat)
        assert(M == count_star(mine_mat))
        return reshapestr(mine_mat)


fin = open(sys.argv[1], 'r')

fout = open(sys.argv[1].split(".")[0] + ".out", "w")

nb_cases = int(fin.readline())

for i in range(1, nb_cases + 1):
    line = fin.readline().strip().split(" ")
    R = int(line[0])
    C = int(line[1])
    M = int(line[2])
    print "Case #%d" % (i)
    fout.write("Case #%d:\n%s\n" % (i, process(R, C, M)))

fout.flush()
fout.close()
fin.close()
