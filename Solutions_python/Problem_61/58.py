import sys
import os

def f(n, k=None, cache={}):
    # a pure set of size k containing n from {2..n}
    if k is None: return sum(f(n,k) for k in range(n))
    
    if k == 0 and n != 1: return 0
    if k < 0 or k >= n: return 0
    if k == 1 or k == n-1: return 1 # all or just n
    if (n,k) not in cache:
        cache[n,k] = sum(binomial(n-k-1, t) * f(k, k-1-t) for t in range(k-1))
    return cache[n,k]
    
#NAME = 'C-example'
NAME = 'C-small-attempt1'
#NAME = 'C-large'

BASEDIR = os.path.expanduser('~/Projects/Challenge/Google CodeJam/GCJ 2010 Round 1B/%s')
inname  = BASEDIR % (NAME + '.in')
outname = BASEDIR % (NAME + '.out')

with open(inname) as fin:
    with open(outname,'w') as fout:
        num_cases = int(fin.readline())
        for case_idx in range(1,1+num_cases):
            n = int(fin.readline())
            assert 2 <= n <= 500

            answer = f(n) % 100003
            print >> fout, "Case #%d: %d" % (case_idx, answer)
