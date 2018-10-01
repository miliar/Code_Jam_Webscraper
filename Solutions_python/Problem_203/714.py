import sys

def fill_row(row, name):
    for i, col in enumerate(row):
        if col == '?':
            row[i]  = name
        else:
            break

def copy_row(ra, rb):
    for i, col in enumerate(rb):
        ra[i] = rb[i]

def slice_cake(cake, ln):

    empty_row = -1

    for i, row in enumerate(cake):
        name = '?'
        last_empty = -1
        for j, col in enumerate(row):

            if col != '?':
                name = col
            else:
                if name == '?':
                    last_empty = j
                else:
                    cake[i][j] = name

            if last_empty != -1 and name != '?':
                fill_row(row, name)

            if j == ln-1 and name == '?' and empty_row == -1:
                empty_row = i

            if empty_row > -1 and name != '?':
                while empty_row < i:
                    copy_row(cake[empty_row], row)
                    empty_row = empty_row+1

                empty_row = -1


    if empty_row > -1:
        while empty_row < len(cake):
            copy_row(cake[empty_row], cake[empty_row-1])
            empty_row = empty_row+1

    return cake

total = None
cases = 0
cake_rows = 0
cake_cals = 0
grid = []

for line in sys.stdin:
    if total:

        if cake_rows:
            row = list(line[0:cake_cals])
            grid.append(row)
            cake_rows = cake_rows-1
            if cake_rows == 0:
                res = slice_cake(grid, cake_cals)
                res = slice_cake(res, cake_cals)

                sys.stdout.write('Case #' + str(cases) + ':' + '\n')
                for i, row in enumerate(res):
                    sys.stdout.write(''.join(res[i]) + '\n')

        else:
            cake = line.split()
            cake_rows = int(cake[0])
            cake_cals = int(cake[1])
            grid = []

            cases = cases+1


        #print line

        #res = str(test(int(line)))
        #sys.stdout.write('Case #' + str(cases) + ': ' + res + '\n')
    else:
        total = line
