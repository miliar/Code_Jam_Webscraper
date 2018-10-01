import sys

def makebox(fd, i):
    box = []
    for i in range(i):
        row = fd.readline().strip().split(' ')
        box.append(row)
    return box

# R - total rows
# C - total cols
# r,c idx of each
def val(b, r, c, R, C):
    good = 1
    for i in range(C):
        if b[r][i] == '2':
            good = 0
            break

    if good == 1:
        return True

    good = 1
    for i in range(R):
        if b[i][c] == '2':
            good = 0
            break

    if good == 1:
        return True
    else:
        return False

def case(fd):
    numrows, numcols = fd.readline().split(' ')
    numrows = int(numrows)
    numcols = int(numcols)
    b = makebox(fd, numrows)

    # for each 1, validate it
    for i in range(numrows):
        for j in range(numcols):
            if b[i][j] == '1':
                if val(b, i, j, numrows, numcols) is not True:
                    return 'NO'
    return 'YES'

def main():
    fd = sys.stdin
    n = int(fd.readline())
    for i in range(n):
        print 'Case #%d: %s' % (i+1, case(fd))

main()

