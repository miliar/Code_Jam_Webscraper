import string
import itertools
import sys

def process_case(L,P,C):
    val = L * C
    cnt = 0
    while (val < P):
        val *= C
        cnt += 1
    return cnt.bit_length()
##    for i in range(1000000):
##        if enough(L,P,C,i):
##            return i

def enough(L,P,C,k):
    if k==0:
        return (L*C >= P)
    return enough(L*pow(C,k), P, C, k-1)

    
def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        L,P,C = line_of_numbers(next(lines))[:3]
        result = process_case(L,P,C)
        yield 'Case #{0}: {1}\n'.format(ci, result)
    
def line_of_numbers(s):
    return [int(sub) for sub in s.split()]

def input_gen(f_in):
    for line in f_in:
        if line.endswith('\n'):
            line = line[:-1]
        yield line

def start(basename):
    infile = basename + '.in'
    outfile = basename + '.out'
    f_in = open(infile, 'r')
    f_out = open(outfile, 'w')
    f_out.writelines(result_gen(input_gen(f_in)))
    f_in.close()
    f_out.close()

#start('B-test')
#start('B-small-attempt1')
start('B-large')

