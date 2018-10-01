# https://code.google.com/codejam/contest/5304486/dashboard

import sys

def alphabet_cake(R, C, cake):
    alphabets = find_alphabets(R, C, cake)
    for arow, acol in alphabets:
        c = cake[arow][acol]
        row_backward, row_forward = acol-1, acol+1
        col_upward, col_downward = arow-1, arow+1
        # print 'Considering',c,'at',(arow,acol), 'col window:', row_backward, row_forward, 'row window:', col_upward, col_downward
        while 0 <= row_backward and cake[arow][row_backward] == '?':
            # print '--backward before', cake[arow],
            cake[arow][row_backward] = c
            # print '-->', cake[arow]
            row_backward -= 1
        while row_forward < C and cake[arow][row_forward] == '?':
            # print '--forward before', cake[arow],
            cake[arow][row_forward] = c
            # print '-->', cake[arow]
            row_forward += 1
        # print '  row_backward', row_backward, 'row_forward', row_forward, 'width', (row_forward-row_backward-1)
        while 0 <= col_upward:
            if any_alphabet(col_upward, row_backward, row_forward, cake):
                break
            # print '--upward before', cake[col_upward],
            for i in range(row_backward+1, row_forward):
                cake[col_upward][i] = c
            # print '-->', cake[col_upward]
            col_upward -= 1
        while col_downward < R:
            if any_alphabet(col_downward, row_backward, row_forward, cake):
                break
            # print '--downward before', cake[col_downward],
            for i in range(row_backward+1, row_forward):
                cake[col_downward][i] = c
            # print '-->', cake[col_downward]
            col_downward += 1
        # print '  col_upward', col_upward, 'col_downward', col_downward
    return '\n'.join([''.join(row) for row in cake])

# exclusive
def any_alphabet(row, left, right, cake):
    # print 'any_alphabet', cake[row][left+1:right]
    for c in cake[row][left+1:right]:
        if c != '?':
            return True
    return False

def find_alphabets(R, C, cake):
    alphabets = []
    for row in range(R):
        for col in range(C):
            c = cake[row][col]
            if c != '?':
                alphabets.append(((row, col)))
    return alphabets

if __name__ == '__main__':
    f = sys.stdin
    T = int(f.readline())
    for i in range(T):
        R, C = map(int, f.readline().split())
        cake = [list(f.readline().strip()) for j in range(R)]
        print "Case #"+str(i+1)+":"
        print alphabet_cake(R, C, cake)
