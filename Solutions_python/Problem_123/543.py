import math
import sys

def parse_block(it):
    a, num_n = [int(i) for i in it.next().split()]
    ni = tuple([int(i) for i in it.next().split()])
    return (a, ni,)
    

def run(it):
    input = parse_block(it)
    return process(input)
    
def process(input):
    a, ni = input
    ni = [ i for i in ni]
    ni.sort()
    
    op = 0
    op_min = [99999999999999999999]
    mote(op_min, a, 0, ni)
    return op_min[0]
    
def mote(op_min, ca, op_so_far, ni):
    if len(ni) == 0:
        if op_so_far < op_min[0]:
            op_min[0] = op_so_far
        return
        
    n = ni[0]
    if ca > n:
        mote(op_min, ca + n, op_so_far, ni[1:])
    else:
        mote(op_min, ca, op_so_far + 1, ni[1:]) # remove
        if ca > 1:
            mote(op_min, ca * 2 - 1, op_so_far + 1, ni[:]) # add