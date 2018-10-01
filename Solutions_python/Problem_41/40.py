import sys
import re
from itertools import *

input = None
output = None

def readints():
    for s in islice(input, 1): 
        lst = map(int, s.split())
        return lst[0] if len(lst) == 1 else lst

def readstr():
    for s in islice(input, 1): 
        return s.strip()

def order(s):
    return ''.join(sorted(s))

def revxrange(a, b = None):
    if b is None:
        return xrange(a - 1, -1, -1)
    else:
        return xrange(b - 1, a - 1, -1)
    
def nextperm(lst):
    for i in revxrange(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            for j in revxrange(i + 1, len(lst)):
                if lst[j] > lst[i]:
                    lst[i], lst[j] = lst[j], lst[i]
                    lst[i + 1:] = lst[:i:-1] # reverse
                    return True
    return False  
            
    
def solvecase(case):
    s = readstr()
    lst = list(s)
    if nextperm(lst):
        s = ''.join(lst)
    else:
        s = order(s)
        for i in range(len(s)):
            if s[i] != '0':
                s = s[i] + '0' + s[:i] + s[i + 1:]
                break
        else:
            raise Exception('WTF')
    
    print >>output, "Case #%d: %s" % (case, s)
    return s
    

def solve():
    casecount = readints()
    for case in range(1, casecount + 1):
        solvecase(case)
            
taskname = 'B'
if __name__ == '__main__':
    input = open(taskname + '-small.in', 'r')
    output = open(taskname + '-small.out', 'w')
    solve()
    print 'Small solved'
    input.close()
    output.close()

    input = open(taskname + '-large.in', 'r')
    output = open(taskname + '-large.out', 'w')
    solve()
    print 'Large solved'
    input.close()
    output.close()
      