#!/usr/bin/env python

import sys,getopt

# GC2011 Round 1C
# solve Problem A.

def solve(p, verbose=False):
    ans = p
    if verbose: print p
    R = len(p)
    
    for r in xrange(R):
        old_l = p[r]
        new_l = p[r].replace('##', 'lr')
        if verbose: print >>sys.stderr, old_l, '->', new_l, 
        if new_l.find('#') > -1: return []
        new_l = list(new_l)
        for c in xrange(len(new_l)):
            if new_l[c] == '.':
                if (r > 0) and (p[r-1][c] == 'l' or p[r-1][c] == 'r'):
                    return []
            if new_l[c] == 'l':
                if (r > 0) and p[r-1][c] == 'l':
                    new_l[c] = 'L'
                elif (r > 0) and p[r-1][c] == 'r':
                    if verbose: print >>sys.stderr, '@%d / NG?' % c
                    return []
            elif new_l[c] == 'r':
                if (r > 0) and p[r-1][c] == 'r':
                    new_l[c] = 'R'
                elif (r > 0) and p[r-1][c] == 'l':
                    if verbose: print >>sys.stderr, '@%d \\ NG?' % c
                    return []
            p[r] = "".join(new_l)
        if verbose: print >>sys.stderr, '->', p[r]
        if p[R-1].find('lr') > -1: return []
        
        ans = [p[r].replace('lr', '/\\').replace('LR', '\\/') for r in xrange(R)]
    return ans

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'v', ['verbose'])
        
    except getopt.GetoptError, err:
        print str(err)
        print >>sys.stderr, sys.argv[0], '[-h] [-v]'
        sys.exit(2)
    verbose = False
    for o, a in opts:
        if o in ('-v', '--verbose'):
            verbose = True
        else:
            assert False, 'unhandled option'

    line= sys.stdin.readline()
    T = int(line) # number ot test cases
    
#main loop
    if verbose:
        print >>sys.stderr, 'input %d test cases' % T
    for t in xrange(T):
        print 'Case #%d:' % (t+1)
        line = sys.stdin.readline()
        R, C = map(lambda x:int(x), line.split())
        if verbose: print >>sys.stderr, '%d rows, %d columns' % (R, C)

        ans = solve([sys.stdin.readline().rstrip() for i in xrange(R)], verbose)
        if ans == []: print 'Impossible'
        else:
            for i in xrange(R):
                print ans[i]
        
        
if __name__ == '__main__':
    main()

        
    
