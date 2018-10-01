def answer(lawn, n, m):
    # Check every cell that isn't on the edges
    if n == 1 or m == 1:
        return 'YES'
    if n == 2 or m == 2:
        return 'YES'
    for row in range(1,n-1):
        for col in range(1,m-1):
            # Does a horizontal or vertical check pass
            cell = lawn[row][col]
            if cell >= lawn[row][col - 1] and cell >= lawn[row][col + 1]:
                # horizontal check passed
                continue
            elif cell >= lawn[row - 1][col] and cell >= lawn[row + 1][col]:
                # vertical check passed
                continue
            else:
                return 'NO'
            print(lawn[row][col], row, col)
    return 'YES'
    # print(lawn)
    # 


def passes_horiz(lawn, n, m, row, col, cell):
    # need to check this entire row
    # if any of the cells in this row are not 1 then it fails
    for i in range(m):
        checkCell = int(lawn[row][i])
        if checkCell == 2:
            return False
    return True

def passes_vert(lawn, n, m, row, col, cell):
    for i in range(n):
        checkCell = int(lawn[i][col])
        if checkCell == 2:
            return False
    return True

def answer(lawn, n, m):
    # Check every cell that isn't on the edges
    good_cols = []
    good_rows = []
    if n == 1 or m == 1:
        return 'YES'
    for row in range(n):
        for col in range(m):
            cell = int(lawn[row][col])
            if row in good_rows or col in good_cols or cell == 2:
                continue
            else:
                if passes_horiz(lawn,n,m,row,col, cell):
                    good_rows.append(row)
                elif passes_vert(lawn,n,m,row,col, cell):
                    good_cols.append(col)
                else:
                    return 'NO'
    return 'YES'
    



def codejam_read(filen):
    f = open(filen,'r')
    fout = open(filen[:-2] + "out", 'w')
    case_num = 0
    test_size = f.readline()

    line = f.readline()
    while line:
        case_num += 1
        line = line.rstrip()
        line = line.split(" ")
        n = int(line[0])
        m = int(line[1])
        lawn = []
        # print(n, m)
        for lines in range(n):
            line = f.readline()
            lawn.append(line.rstrip().split(" "))
        outcome = answer(lawn, n, m)
        print("Case #{0}: {1}\n".format(case_num,outcome))
        line = f.readline()


        fout.write("Case #{0}: {1}\n".format(case_num, outcome))

    fout.close()
    f.close()


codejam_read('B-small-attempt1.in')
# codejam_read('b-sample.in')