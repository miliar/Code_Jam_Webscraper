
import sys
import os
import numpy as np
import math
import pandas as pd
import itertools


def nCk(n,k):
    if k == 0: return 1
    if k == n: return 1
    top = 1
    bot = 1
    for i in xrange(k):
        top *= (n-i)
        bot *= (i+1)
    return top / bot

def in_range(x, low, high):
    return x >= low and x <= high

# Thank you stackoverflow
def kbits(n, k):
    result = []
    for bits in itertools.combinations(range(n), k):
        s = ['0'] * n
        for bit in bits:
            s[bit] = '1'
        result.append(''.join(s))
    return result

def str_rev( s ):
    z = map(lambda x: s[-x], range(1,len(s) + 1))
    return ''.join(z)
    

def generate_pall_roots( digits ):
    if digits == 1: return ['1', '2', '3']
    palls = []
    arr = ['0' for x in xrange(digits)]
    # First, the head and tail could be two
    arr[0] = '2'
    arr[-1] = '2'
    palls += [''.join(arr)]
    if digits % 2 == 1:
        mid = (digits - 1) / 2
        arr[mid] = '1'
        palls += [''.join(arr)]
        arr[mid] = '0'
        arr[0] = '1'
        arr[-1] = '1'
        arr[mid] = '2'
        palls += [''.join(arr)]
        varsize = (digits - 3) / 2
        forward = reduce(lambda x,y: x + kbits(varsize, y), range(4), [])
        back    = map(lambda x: str_rev(x), forward)
        with_one = map(lambda x: '1' + forward[x] + '1' + back[x] + '1', range(len(forward)))
        with_zero =map(lambda x: '1' + forward[x] + '0' + back[x] + '1', range(len(forward)))
        palls += with_one
        palls += with_zero
    else:
        varsize = (digits - 2) / 2
        forward = reduce(lambda x,y: x + kbits(varsize, y), range(4), [])
        back    = map(lambda x: str_rev(x), forward)
        mids = map(lambda x: '1' + forward[x] + back[x] + '1', range(len(forward)) )
        palls += mids
    return palls
    

def is_pall( n ):
    string = str(n)
    strlen = len(string)
    if strlen == 1:
        return True
    stop = ( (strlen + 1) / 2 ) + 1
    checks = map(lambda x: string[x] == string[-(x+1)], range(stop))
    return reduce(lambda x,y: x and y, checks, True)

def is_square( x ):
    return x == int(math.sqrt(x))**2


def process(A,B):
    return len(filter(lambda x: in_range(x, A,B), afs))
    

#
# Always run this initialization
#
if not os.path.isfile('AllFairSquaresRoots.txt'):
    the_roots = reduce(lambda x,y: x + generate_pall_roots(y), range(1,51), [])
    fhand = open('AllFairSquaresRoots.txt', 'wb')
    for root in the_roots:
        fhand.write(root + '\n')
    fhand.close()


afsr = map(int, open('AllFairSquaresRoots.txt').readlines())
afs  = map(lambda x: x**2, afsr)

if __name__ == '__main__':
    infile = open(sys.argv[1], 'rb')
    lines = map(lambda x: x.rstrip(), infile.readlines())

    N = int(lines[0])  # Number of cases
    lineIdx = 1
    caseNo = 1

    while (lineIdx < len(lines) and caseNo <= N):
        A,B = map(int,lines[lineIdx].split(' '))
        lineIdx += 1
        caseAnswer = process(A,B)
        print 'Case #%d: %d' % (caseNo, caseAnswer)
        caseNo += 1
        


