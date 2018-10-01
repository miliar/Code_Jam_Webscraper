# ready to take input file name as second command line argument
# ready to take output file name as third command line argument

import sys
import math

def get_num_black_rings(r, t):
    # will always be one black ring so subtract the following from t
    paint_left, new_rad = t - (2 * r + 1), r + 1
    num_rings = 1
    amt_needed_next = (2 * new_rad + 3)
    while paint_left >= amt_needed_next:
        num_rings += 1
        paint_left -= amt_needed_next
        new_rad += 2
        amt_needed_next = (2 * new_rad + 3)
    return num_rings

def main():
    input = open(sys.argv[1], 'r')
    input.readline()
    # will need input.readlines() (or something similar) later, which will separate lines into
    # list elements, leaving the \n attached to the end of each line
    # the string method .strip('\n') will remove these
    output = open(sys.argv[2] + '.out', 'w')
    # will use output.write(result + '\n') later to write one 'result' line at a time to the output file
    
    case = 1
    for line in input:
        params = line.strip().split()
        num_rings = get_num_black_rings(int(params[0]), int(params[1]))
        result = ('\n' if case > 1 else '') + 'Case #{}: {}'.format(case, num_rings)
        output.write(result)
        case += 1
    
    # close both files at end of program
    output.close()
    input.close()
    print 'Done!'

def main2():
    
    input = open(sys.argv[1], 'r')
    input.readline()
    
    for line in input:
        print line,
    
    input.close()

if __name__ == '__main__':
    
    main()