import sys
from itertools import *

def second_dig(number):
    i=groupby(number)
    i.next()
    try:
        return i.next()[0]
    except:
        return None
def solve(input, case_no):
    print "solving ", case_no
    number = list(input.next().strip())
   
    zero_dig=second_dig(number)
    digs={zero_dig:0}
    next=1
    for dig in number:
        if dig not in digs:
            digs[dig] = next
            next += 1
    base = next
    print "Base is", base
    m = 1
    rval = 0
    for dig in reversed(number):
        rval += digs[dig] * m
        m *= base
    print rval
    return rval
    
input = iter(open(sys.argv[1], 'r'))
output = open(sys.argv[1].replace('.in', '.out'), 'w')

T = int(input.next().strip())

for case_no in range(T):
    solution = solve(input,case_no)
    print >>output, "Case #%d: %s"  % (case_no+1, solution) 