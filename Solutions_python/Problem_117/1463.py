import sys

def verify_pattern(matrix):
    for idx_row,row in enumerate(matrix):
        max_value_required = get_max_value(row,0)
        matrix = update_h_in_row(matrix,idx_row,max_value_required)
    idx_column = 0
    numbers_column = len(matrix[0])
    while idx_column < numbers_column:
        column = get_collumn(matrix,idx_column)
        if verify(column):
            idx_column += 1
        else:
            max_value_required = get_max_value(column,0)
            matrix = update_h_in_column(matrix, idx_column, max_value_required)
            if verify(column):
                idx_column += 1
            else:
                return 'NO'
    return 'YES'

def get_max_value(vector,type_of_value):
    values_required = [i[type_of_value] for i in vector]
    return max(values_required)

def update_h_in_row(matrix, idx_row, new_value):
    for i in xrange(0,len(matrix[idx_row])):
        matrix[idx_row][i][1] = new_value
    return matrix

def get_collumn(matrix, n):
    collumn = []
    for i in xrange(0,len(matrix)):
        collumn.append(matrix[i][n])
    return collumn

def update_h_in_column(matrix, idx_column, new_value):
    for i in xrange(0,len(matrix)):
        matrix[i][idx_column][1] = new_value
    return matrix

def verify(vector):
    result = True
    for i in vector:
        if i[0] != i[1]:
            return False
    return result
    
if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        quantity = int(f.readline())
        for execution in xrange(quantity):
            line = f.readline()
            line = line.split()
            n = int(line[0])
            m = int(line[1])
            matrix = []
            for idx_row in xrange(0,n):
                row = []
                line = f.readline()
                line = line.split()
                for idx_col in xrange(0,m):
                    row.append([int(line[idx_col]),100])
                matrix.append(row)
            print 'Case #%i: %s' %(execution+1,verify_pattern(matrix))