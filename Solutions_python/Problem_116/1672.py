#!/usr/bin/python -tt
"""
"""

import sys
import math
import time


def prob(problem, input_type):
   
    # boilerplate to handle code jam specific input files

    problem = problem
    input_type = input_type

    if input_type == '':
        filestring = problem + '_'
    else:
        filestring = problem + '_' + input_type + '_'

    finput = open(filestring + 'input.txt', 'r')
    foutput = open(filestring + 'output.txt', 'w')

    # store input file lines in list
    inputs = finput.readlines()
    print(inputs)

    # input file parser
    index = 0
    num_testcases = int(inputs[index]) 
    lines_per_testcase = 5
    print('number testcases:', num_testcases)
    index += 1


    for testcase in range(1,num_testcases+1):
        print('testcase:', testcase)
        
        # grab input data
        # read data into a list
        # convert entries to int for easier outcome recognition
        board = ''
        for i in range(4):
            board = (board + inputs[index+i]).replace('\n','') 
        print(board)
        b = list(board)
        for ind, item in enumerate(b):
            if item == 'X':
                b[ind] = 1
            elif item == 'O':
                b[ind] = 5
            elif item == 'T':
                b[ind] = 21
            else:
                b[ind] = 0
        print(b)
        
        # implement solution algorithm
        # if sum=4 or sum=24, 'X won' 
        # if sum=20 or sum=36, 'O won'
        # else if '0' exists 'Game has not completed'
        # else 'Draw' 

        boardsums = [b[0]+b[1]+b[2]+b[3],
                     b[4]+b[5]+b[6]+b[7],
                     b[8]+b[9]+b[10]+b[11],
                     b[12]+b[13]+b[14]+b[15],
                     b[0]+b[4]+b[8]+b[12],
                     b[1]+b[5]+b[9]+b[13],
                     b[2]+b[6]+b[10]+b[14],
                     b[3]+b[7]+b[11]+b[15],
                     b[0]+b[5]+b[10]+b[15],
                     b[3]+b[6]+b[9]+b[12]]

        print(boardsums)

        if boardsums.count(4) or boardsums.count(24):
            outcome = 'X won'
        elif boardsums.count(20) or boardsums.count(36):
            outcome = 'O won'
        elif b.count(0):
            outcome = 'Game has not completed'
        else:
            outcome = 'Draw'

        print(outcome)
        foutput.write('Case #%d: %s\n' % (testcase, outcome))
       
        # end of solution algorithm

        index = index + lines_per_testcase 
    
    finput.close()
    foutput.close()

# main() handles cmdline parsing and runtime check 
def main():

  # Omit the [0] element which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--problem] <problem> [--input] (sample|small|large)')
    sys.exit(1)

  if not args[3]:
      args[3] = ''

  s = time.time()
  
  answer = prob(args[1], args[3]) 

  print('Runtime: %0.2f seconds' % (time.time() - s))

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
