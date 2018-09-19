#!/usr/bin/env python

import sys,getopt

# GCJ2011 Qualification Round
# solve Problem A.

def solve(line, verbose=False):
    ans = -1
    O_p = 1
    O_m = []
    B_p = 1
    B_m = []
    N = int(line.split()[0])
    RP = line.split()[1:]
    if verbose:
        print >>sys.stderr, N, 'terms'
    for i in xrange(N):
        if verbose:
            print >>sys.stderr, RP[2*i], RP[2*i+1]
        pos = int(RP[2*i+1])
        d = 0
        if RP[2*i] == 'O':
            if pos-O_p>0: d=1
            else: d=-1
            for j in xrange(abs(pos-O_p)):
                if len(O_m) > j and O_m[-1-j] == 'S':
                    O_m.pop(-1-j)
                    O_m.append(d)
                else:
                    O_m.append(d)
                    B_m.append('S')

            O_m.append('P')
            B_m.append('S')
            O_p = pos
        else:
            if pos-B_p>0: d=1
            else: d=-1
            for j in xrange(abs(pos-B_p)):
                if len(B_m) > j and B_m[-1-j] == 'S':
                    B_m.pop(-1-j)
                    B_m.append(d)
                else:
                    B_m.append(d)
                    O_m.append('S')

            B_m.append('P')
            O_m.append('S')
            B_p = pos


    if verbose:
        print >>sys.stderr, O_m
        print >>sys.stderr, B_m
        print >>sys.stderr, 'Time | Orange           | Blue'
        print >>sys.stderr, '-----+------------------+-----------------'
        for t in xrange(min(len(O_m), len(B_m))):
            print >>sys.stderr, '%5d|%18.18s|%17.17s' % (t+1, str(O_m[t]), str(B_m[t]))

    ans = min(len(O_m), len(B_m))
    return ans

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hv', ['help', 'verbose'])
    except getopt.GetoptError, err:
        print str(err)
        print >>sys.stderr, 'solve-A.py [-h] [-v]'
        sys.exit(2)
    verbose = False
    for o, a in opts:
        if o in ('-v', '--verbose'):
            verbose = True
        elif o in ('-h', '--help'):
            print >>sys.stderr, 'solve-A.py [-h] [-v]'
            sys.exit()
        else:
            assert False, 'unhandled option'
    
    line = sys.stdin.readline()
    T = int(line)
#main loop
#input handling
    if verbose:
        print >>sys.stderr, 'input %d test cases' % T
    for i in xrange(T):
        line = sys.stdin.readline()
        ans = solve(line, verbose)
        print 'Case #%d: %d' % (i+1, ans)

if __name__ == '__main__':
    main()

