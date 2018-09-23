import imp, sys

sys.modules["utils"] = __mod = imp.new_module("utils")
exec """#!/usr/bin/python

from itertools import chain, repeat, izip

def line(*args):
	L = raw_input().strip().split()
	L = izip( L, chain( args, repeat(str) ) )
	return [ type(data) for data, type in L ]	
	
def iline(): return map( int, raw_input().strip().split() )
def fline(): return map( float, raw_input().strip().split() )""" in vars(__mod)

#!/usr/bin/python

from utils import line, iline

def test():
    S, k = line(str, int)
    
    yield
    
    
    S = [ c for c in S ]

    ans = 0
    for i, c in enumerate(S):
        if c == '-':
            if i+k > len(S):
                print 'IMPOSSIBLE'
                return

            for j in xrange(i, i+k):
                S[j] = '+' if S[j] == '-' else '-'

            ans += 1

    print ans
        
        
        
if __name__ == '__main__':
    T = input()
    for i in xrange(1, T+1):
        print 'Case #%d:' % i,
        solver = test()
        if hasattr(solver, 'next'):
            list(solver)
        elif callable(solver):
            solver()

