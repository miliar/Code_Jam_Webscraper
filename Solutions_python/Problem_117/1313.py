import sys

def getmaxes(lawn):
    rowmax = []
    columnmax = []
    for y in xrange(rows):
        rowmax.append(0)
        for z in xrange(columns):
            if lawn[y][z] > rowmax[-1]:
                rowmax[-1] = lawn[y][z]

    for y in xrange(columns):
        columnmax.append(0)
        for z in xrange(rows):
            if lawn[z][y] > columnmax[-1]:
                columnmax[-1] = lawn[z][y]
    return rowmax, columnmax

def checklawn(rowmax, columnmax, lawn):
    for row, rmax in zip(lawn, rowmax):
        for square, cmax in zip(row, columnmax):
                if square < rmax and square < cmax:
                    return 'NO'
    return 'YES'


if __name__ == '__main__':
    file = open('B-large.in', 'r')
    solution = open('large-result.txt', 'w')
    testcases = int(file.readline().rstrip())
    for lawns in xrange(testcases):
        line = file.readline().rstrip().split()
        rows = int(line[0])
        columns = int(line[1])
        lawn = []
        for x in xrange(rows):
            lawn.append([int(i) for i in file.readline().rstrip().split()])

        rowmax, columnmax = getmaxes(lawn)
        solution.write('Case #' + str(lawns+1) + ': ' + checklawn(rowmax, columnmax, lawn) + '\n')    
    solution.close()