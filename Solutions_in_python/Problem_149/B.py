import sys
import itertools
import math
import collections
import functools

def read_word(f):
    return next(f).strip()
def read_int(f, b=10):
    return int(read_word(f), b)
def read_letters(f):
    return list(read_word(f))
def read_digits(f, b=10):
    return [int(x, b) for x in read_letters(f)]
def read_words(f, d=' '):
    return read_word(f).split(d)
def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]
def read_floats(f, d=' '):
    return [float(x) for x in read_words(f, d)]
def read_arr(f, R, reader=read_ints, *args, **kwargs):
    res = []
    for i in range(R):
        res.append(reader(f, *args, **kwargs))
    return res
def solve(solver,SMALL=True,PRACTICE=False):
    fn = sys.argv[0]
    fn = fn[ 1+fn.rfind('/'): fn.rfind('.') ]
    fn = fn+['-large','-small'][SMALL]+['','-practice'][PRACTICE]
    in_fn = fn + '.in'
    out_fn = fn + '.out'
    with open(in_fn, 'r') as fi:
        with open(out_fn, 'w') as fo:
            T = read_int(fi)
            for i in range(T):
                case = read_case(fi)
                res = solver(case)
                print i+1, res
                write_case(fo, i+1, res)
def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')

#######################################################

def read_case(f):
    N = read_int(f)
    A = read_ints(f)
    B = A[:]
    B.sort()
    
    return N, map(lambda x: B.index(x),A)

#######################################################
def merge_and_count(a, b):
    assert a == sorted(a) and b == sorted(b)
    c = []
    count = 0
    i, j = 0, 0
    while i < len(a) and j < len(b):
        c.append(min(b[j], a[i]))
        if b[j] < a[i]:
            count += len(a) - i # number of elements remaining in `a`
            j+=1
        else:
            i+=1
    # now we reached the end of one the lists
    c += a[i:] + b[j:] # append the remainder of the list to C
    return count, c

def sort_and_count(L):
    if len(L) == 0: return 0, L
    if len(L) == 1: return 0, L
    n = len(L) // 2 
    a, b = L[:n], L[n:]
    ra, a = sort_and_count(a)
    rb, b = sort_and_count(b)
    r, L = merge_and_count(a, b)
    return ra+rb+r, L

def solver(case):
    #0 must be leftmost or rightmost, just try all
    N,A = case
    #print N,A
    ct = 0
    l = 0
    r = N-1
    sw = 0
    while ct < N:
        ix = A.index(ct)
        lefty = ix
        righty = len(A) - ix - 1
        A.pop(ix)
        #print A
        sw += max(0, min(lefty,righty))
        ct += 1
        #print 's',sw,ct
    return sw
"""
def solver(case):
    N,A = case
    ix = A.index(N-1)
    YY = sort_and_count(A[:ix])
    B = A[ix:]
    B.reverse()
    ZZ = sort_and_count(B)
    
def solver2(case):
    N,A = case
    maxi = 999999999999999
    print '!',A
    for i in xrange(N):
        #try x[:i] and x[i:], ignoring N-1
        B = A[i:]
        C = A[:i]
        B.reverse()
        
        tri = sort_and_count(B)[0] + sort_and_count(C)[0]
        print B,C,sort_and_count(B)[0],sort_and_count(C)[0]
        if tri < maxi: maxi = tri
    return maxi"""


    
#False for large
solve(solver,True)
#solve(solver,False)

print 'Done'
