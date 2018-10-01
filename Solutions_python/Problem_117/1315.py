def is_pattern_possible(rowcnt, colcnt, rows):
    print('%i X %i, %s' % (rowcnt, colcnt, repr(rows)))
    rowmaxes = []
    colmaxes = []
    columns = [[] for i in range(colcnt)]
    for row in rows:
        rowmaxes.append(max(row))
        for colidx in range(colcnt):
            columns[colidx].append(row[colidx])
    for col in columns:
        colmaxes.append(max(col))
    for rowidx in range(rowcnt):
        for colidx in range(colcnt):
            height = rows[rowidx][colidx]
            if height < rowmaxes[rowidx] and height < colmaxes[colidx]:
                return 'NO'
    return 'YES'


import sys
#import pdb

if __name__ == '__main__':
    filename_prefix = sys.argv[1]
    filename_in = filename_prefix + ".in"
    filename_out = filename_prefix + ".out"

    file_in = open(filename_in, 'r')
    lines = file_in.readlines()

    testcnt = int(lines[0])
    idx = 1

    file_out = open(filename_out, 'w')

    #pdb.set_trace()
    for test in range(testcnt):
        line = lines[idx].split(' ')
        idx += 1

        rowcnt = int(line[0])
        colcnt = int(line[1])
        rows = list()
        for rowidx in range(rowcnt):
            line = lines[idx].split(' ')
            idx += 1
            rows.append([int(i) for i in line])

        res = is_pattern_possible(rowcnt, colcnt, rows)
        file_out.write("Case #{0}: {1}\n".format(test + 1, res))
