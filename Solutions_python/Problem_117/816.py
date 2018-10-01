def check_column(inp, col_num, N, element):
    column_items = []
    for i in range(N):
        column_items.append(inp[i][col_num])
    return all([item <= element for item in column_items])

def check_row(inp, row_num, element):
    return all([item <= element for item in inp[row_num]])

def is_cuttable(inp, i, j, N, M):
    """
    Checks if this particular square can be cut using lawnmover. This can be
    done by checking if ith row or jth column has an element higher than this
    number.
    """
    return any([check_row(inp, i, inp[i][j]), check_column(inp, j, N, inp[i][j])])

def can_be_mowed(inp, N, M):
    for i in range(N):
        for j in range(M):
            if not is_cuttable(inp, i, j, N, M):
                return "NO"
    return "YES"

def read_input():
    no_of_cases = input()
    for i in range(no_of_cases):
        inp = []
        N, M  = map(int, raw_input().split(' '))
        for j in range(N):
            inp.append(map(int, raw_input().split(' ')))
        print "Case #%d: %s" % (i+1, can_be_mowed(inp, N, M))


if __name__ == '__main__':
    read_input()
