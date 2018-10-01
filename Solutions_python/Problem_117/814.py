
def lawnmower():
    """
        used to solve google code jam 2013 - Problem B
    """
    in_f = open('B-large.in', 'r')
    out_f = open('B-large_output.txt', 'w')
    num_of_case = int(in_f.readline().rstrip('\n'))
    print "num of cases:{}".format(num_of_case)
    for i in range(1, num_of_case+1):
        solve_case(in_f, out_f, i)
        
def solve_case(in_f, out_f, case_index):
    """
    solve each case
    """
    print "start handling case #{}".format(case_index)
    square_info = in_f.readline().rstrip('\n').split(" ")
    row = int(square_info[0])
    column = int(square_info[1])
#    board = [[[0 for x in xrange(3)] for x in xrange(column)] for x in xrange(row)]
    board = [[0 for x in xrange(column)] for x in xrange(row)]
    # do the board initialiaztion and at the same time, 
    # if there is a quick win by line, quit quickly by just finishing reading all the remaining lines. 
    for j in range(0, row):
        line = in_f.readline().rstrip('\n')
        str_list = line.split(" ")
        board[j] = [int(x) for x in str_list]
    print board
    # start calculate the max values for each row
    row_max = [0 for x in xrange(row)]
    for i in range(0, row):
        row_max[i] = max(board[i])
    print row_max
    # start calculate the max values for each column
    column_max = [0 for x in xrange(column)]
    for i in range(0, column):
        column_list = [each_row[i] for each_row in board]
        column_max[i] = max(column_list)
    print column_max
    # start testing:
    for i in range(0, row):
        for j in range(0, column):
            if board[i][j] < min(row_max[i], column_max[j]):
                print "NO"
                out_f.write("Case #{}: NO\n".format(case_index))
                return
    print "YES"
    out_f.write("Case #{}: YES\n".format(case_index))
    
if __name__ == '__main__':
    lawnmower()
