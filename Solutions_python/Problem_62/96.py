#!/usr/bin/env python

def intersect(rope1, rope2):
    (h11, h12) = rope1
    (h21, h22) = rope2
    if ((h11-h21) * (h12-h22) < 0):
        return True
    else:
        return False

def solve(read):
    [N] = read_int_line(read)
    ropes = []
    for x in xrange(N):
        [h1, h2] = read_int_line(read)
        ropes.append( (h1, h2, ) )
    
    return len([(rope1, rope2) for rope1 in ropes
                                    for rope2 in ropes
                                        if intersect(rope1, rope2)]) // 2

def main():
    solve_n_cases(solve)

##### PROBLEM VARIABLES ######

INFILENAME = 'A-large.in'
OUTFILENAME = 'output.out'

##### PROBLEM TEMPLATE ######

def init_io():
    read = open(INFILENAME, 'rt')
    write = open(OUTFILENAME, 'wt')
    return (read, write)

def deinit_io(read, write):
    read.close()
    write.close()
    
def read_token_line(read, tokenparsefunction):
    return [tokenparsefunction(x)
                for x in read.readline().split()]
    
def read_int_line(read):
    return read_token_line(read, int)
    
def output_case_sharp(write, casenum, result):
    write.write( 'Case #{0}: {1}\n'.format(casenum, result) )

def solve_n_cases(case_function, output_function = output_case_sharp):
    read, write = init_io()
    
    cases_num = int(read.readline())
    current_case = 1
    
    while (cases_num>0):
        case_result = case_function(read)
        output_function(write, current_case, case_result)
        
        cases_num -= 1
        current_case += 1
        
    
    deinit_io(read, write)

main()