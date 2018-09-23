__author__ = 'Christian'

#fname = 'test_a.txt'
#fname = 'A-small-attempt0.in'
fname = 'A-large.in'

f = open(fname, 'r')
data = f.read().split('\n')
f.close()

res_file = open(fname + '.res', 'w')

def populate_cake(cake, starting_row, ending_row, starting_col, ending_col):
    # find the first row with at least one letter
    #print "looking at ", starting_row, ending_row, starting_col, ending_col
    #print cake
    for r in range(starting_row, ending_row+1):
        if not all([c == '?' for c in cake[r][starting_col:ending_col+1]]):
            break
    row_with_data = r
    #print 'row_with_data', r
    # add all the following empty rows
    if row_with_data == ending_row:
        separation_row = row_with_data
    else:
        separation_row = ending_row
        for r in range(row_with_data+1, ending_row+1):
            if not all([c == '?' for c in cake[r][starting_col:ending_col+1]]):
                separation_row = r-1
                break
    #print 'separation', separation_row

    # find the second letter in the row with data
    second_letter = ending_col+1
    char_found = 0
    filling_char = None
    for ind in range(starting_col,ending_col+1):
        c = cake[row_with_data][ind]
        if c != '?':
            char_found += 1
            if char_found == 1:
                filling_char = c
            elif char_found == 2:
                second_letter = ind - 1
                break
    # mark the left part with the first letter
    #print 'before fill', starting_row, separation_row, starting_col, second_letter
    #raise ValueError
    for r in range(starting_row, separation_row+1):
        for c in range(starting_col, min(ending_col,second_letter)+1):
            #print r, c
            cake[r][c] = filling_char
    # and loop the process on the other part
    if second_letter != ending_col+1:
        populate_cake(cake, starting_row, separation_row, second_letter+1, ending_col)
    # loop the process on the bottom part pf the cake
    if separation_row != ending_row:
        populate_cake(cake, separation_row+1, ending_row, starting_col, ending_col)
    return '\n'.join([''.join(row) for row in cake])

T = int(data[0])
index = 1
for i in range(T):
    R, C = data[index].split(' ')
    index += 1
    R = int(R)
    C = int(C)
    cake = []
    for j in range(R):
        cake.append(list(data[index]))
        index += 1
    print >> res_file, "Case #%s:\n%s" % (i+1, populate_cake(cake, 0, R-1, 0, C-1))
    
res_file.close()