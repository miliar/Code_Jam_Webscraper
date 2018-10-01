import os
import numpy as np
import argparse

def run(filename, out_filename):


    f = open(filename, 'r')
    f_out = open(out_filename, 'w')    
    
    
    no_of_cases = int(f.readline())
    print 'Number of cases: ', no_of_cases
    

    lines = f.readlines()
    case = 1

    rows = []

    for line in lines:

        if line == '\n':
            selection = makeSelection(rows)
            status = evaluate(selection)
            message = 'Case #%i: %s\n'% (case,status)
            print message
            f_out.write(message)

            case +=1
            rows=[]
        
        else:
            rows.append(line.replace('\n', ''))

def evaluate(selection):
    '''
    Evaluate selection strings.
    ''' 
    for sel in selection:
        x = sel.count('X') + sel.count('T')
        if x == 4:
            return 'X won'

        o = sel.count('O') + sel.count('T')
        if o == 4:
            return 'O won'
  
    all_fields = ''
    for sel in selection[0:4]:
        all_fields = all_fields + sel
    if all_fields.count('.') > 0:
        return 'Game has not completed'
    else:
        return 'Draw'



def makeSelection(rows):
    '''
    Create strings containing all possible combination of all directions inside
    the board.
    '''
  
    cols = ['', '', '', '']
    digs = ['', '']

    for j, row in zip(xrange(len(rows)), rows):
        for i, r in zip(xrange(len(row)), row):          
            cols[i]=cols[i]+r     
            if i == 3-j:
                digs[0]=digs[0]+ r
            if i == j:
                digs[1]=digs[1]+ r
    
    selection = rows + cols + digs

    return selection

if __name__ == '__main__': 

    parser = argparse.ArgumentParser(description='Tic Tac Toe')

    parser.add_argument('-i','--input-file',                                        
                             action="store", help='Input filename')
    parser.add_argument('-o', '--output-file',
                             action ='store', help='Output file')
    args = parser.parse_args()
    
    if args.input_file == None:
        args.input_file = 'input.txt'    
    if args.output_file == None:
        args.output_file = 'output.txt'
    run(args.input_file, args.output_file)    
