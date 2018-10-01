from __future__ import print_function
import sys


NR_ROWS = 4

# Status codes
YES = 1
NO = 2

# Textual desctiption
status_text = {}
status_text[YES] = 'YES'
status_text[NO] = 'NO'

def read_file(filename):
    f = open(filename)
    content = f.read()
    f.close()
    return content
    
def parse_input(f):
    line_idx = 0
    
    cases = []
    nr_cases = int(f.readline())
    
    for case_idx in xrange(nr_cases):
    
        line = f.readline()
        nr_rows, nr_cols = line.split(' ')
        nr_rows = int(nr_rows)
        nr_cols = int(nr_cols)
        
        case = []
        
        for row_idx in xrange(nr_rows):
        
            row = []

            line = f.readline()
            line = line.split(' ')

            for col_idx in xrange(nr_cols):
                row.append(int(line[col_idx]))
                
            case.append(row)
                
        cases.append(case[:])
        
        # Line break after every case
        # line = f.readline()
        
    return cases
    
def printcase(case, dbg):
    for row in case:
        s = ''
        for item in row:
            s += '%d ' % (item,)
            
        print (s, file=dbg)

    
def check_status(case, dbg):
    printcase(case, dbg)

    nr_rows = (len(case))
    if (0 == nr_rows):
        print ('YES', file=dbg)
        return YES
        
        
    nr_cols = len(case[0])
    if (0 == nr_cols):
        print ('YES', file=dbg)
        return YES    
        
    
    for row_idx in xrange(nr_rows):
        for col_idx in xrange(nr_cols):
        
            cur_item = case[row_idx][col_idx]
        
            
            for j in xrange(0, nr_cols):
                if cur_item < case[row_idx][j]:
                    # Validate that the column is smaller/equal
                    for i in xrange(nr_rows):
                        if case[i][col_idx] > cur_item:

                            print ('NO 1', file=dbg)
                            return NO
                            
            
            for j in xrange(0, nr_rows):
                if cur_item < case[j][col_idx]:
                    # Validate that the row is smaller/equal
                    for i in xrange(nr_cols):
                        if case[row_idx][i] > cur_item:
                            
                            print ('NO 3', file=dbg)
                            return NO
                            
    print ('YES', file=dbg)
    return YES
    
def main():
    
    f = open(sys.argv[1], 'r')
    cases = parse_input(f)
    f.close()
    
    dbg = open(r'dbg.txt', 'w')
    
    output_file = open('output_2.txt', 'w')
    for case_idx, case in enumerate(cases):
        dbg.write("case %d\n" % (case_idx + 1,))
        status_code = check_status(case, dbg)
        output_file.write('Case #%d: %s\n' % (case_idx + 1, status_text[status_code]))
        
    output_file.close()
    
    
if __name__ == '__main__':
    main()