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

from utils import iline
from sys import stderr

HALF = 12*60
FULL = 24*60

def test():
    C, J = iline()
    cjobs = [iline() for i in xrange(C)]
    jjobs = [iline() for i in xrange(J)]
    
    yield
    
    jobs = [(c, d, 'c') for c, d in cjobs] + [(c, d, 'j') for c, d in jjobs]
    jobs.sort()

    def solve(who, need, answer):
        gains = []

        for prev, next in zip(jobs, jobs[1:] + jobs[:1]):
            if prev[2] == next[2]:
                gains.append((next[0]-prev[1]+FULL)%FULL)

        gains.sort()
        #print >>stderr, need, gains

        while need > 0:
            answer += 2
            gain = gains[-1]
            gains.pop()
            need -= gain

        print answer

    if C == 0:
        solve('c', HALF, 0)
        return
    elif J == 0:
        solve('j', HALF, 0)
        return

    i = 0
    while jobs[i][2] == jobs[-1][2]:
        jobs[i] = (jobs[i][0] + FULL, jobs[i][1] + FULL, jobs[i][2])
        i += 1

    jobs = jobs[i:]+jobs[:i]

    def merge():
        left = 0
        while left < len(jobs):
            right = left
            while right < len(jobs) and jobs[right][2] == jobs[left][2]:
                right += 1
            yield jobs[left][0], jobs[right-1][1], jobs[left][2]
            left = right

    def maximize(jobs, who):

        other = {'c': 'j', 'j': 'c'}
        change_min = jobs[-1][1]-FULL

        for job in jobs:
            change_max = job[0]

            if job[2] == who:
                yield change_max, other[job[2]]
            else:
                yield change_min, other[job[2]]

            change_min = job[1]


    mjobs = list(merge())
    cchanges = list(maximize(mjobs, 'c')) 
    cchanges.append((cchanges[0][0]+FULL, cchanges[0][1]))
    jchanges = list(maximize(mjobs, 'j'))
    jchanges.append((jchanges[0][0]+FULL, jchanges[0][1]))

    ctotal = sum((d-c) for (c, who), (d, _) in zip(cchanges[:-1], cchanges[1:]) if who == 'c')
    jtotal = sum((d-c) for (c, who), (d, _) in zip(jchanges[:-1], jchanges[1:]) if who == 'j')

    #print >>stderr, jobs
    #print >>stderr, mjobs
    #print >>stderr, cchanges
    #print >>stderr, jchanges
    #print >>stderr, ctotal, jtotal

    if ctotal < HALF:
        solve('c', HALF-ctotal, len(cchanges)-1)
    elif jtotal < HALF:
        solve('j', HALF-jtotal, len(cchanges)-1)
    else:
        print len(cchanges)-1
        
        
        
if __name__ == '__main__':
    def main():
        T = input()
        for i in xrange(1, T+1):
            print 'Case #%d:' % i,
            solver = test()
            if hasattr(solver, 'next'):
                list(solver)
            elif callable(solver):
                solver()
    main()

