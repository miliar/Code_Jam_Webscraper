#!/usr/bin/python

SIZE = 'small'
PROBLEM = 'B'
DATASET = PROBLEM + '-' + SIZE
IFILE = DATASET + '.in'
OFILE = DATASET + '.out'

def game(team, level):
    return team / (2**(level+1))

def solve(P, M):
    rounds = [([False]*(2**(P-i-1))) for i in xrange(P)]
    for i in xrange(len(M)):
        for level in xrange(M[i], P):
            #print i, level, game(i, level), rounds
            rounds[level][game(i, level)] = True
    return sum(sum(a) for a in rounds)

ifile = open(IFILE, 'r')
ofile = open(OFILE, 'w')
T = int(ifile.readline())
for i in xrange(T):
    P = int(ifile.readline())
    line = ifile.readline().strip().split(' ')
    M = [int(a) for a in line]
    assert(len(M) == 2**P)
    for j in xrange(P):
        line = ifile.readline().strip().split(' ')
        assert(line == ['1']*(2**(P-j-1)))
    solution = solve(P, M)
    ofile.write('Case #%s: %s\n' % (i+1,str(solution)))
ifile.close()
ofile.close()
