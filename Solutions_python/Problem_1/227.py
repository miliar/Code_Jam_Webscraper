#!/usr/bin/env python
"simple"
import sys

INF = 11000

global GLB
GLB = {
        #'engines' : 'YNDBG',
        #'queries' : '',
        #'engines' : 'YNDBG',
        #'queries' : 'GDNNYYG',

        #'engines' : 'YNDBG',
        #'queries' : 'YYGBGNBNDGYNB',
        'engines' : 'ABC',
        'queries' : 'ABCABCABC',
        }
GLB['nqueries'] = len(GLB['queries'])
GLB['mem'] = {}

def index(ls, x, i):
    if x in ls[i:]:
        return ls.index(x, i)
    return -1

def save_mem(i, e, sol):
    if i not in GLB['mem']:
        GLB['mem'][i] = {}
    GLB['mem'][i][e] = sol
def remember(i, e):
    if i in GLB['mem']:
        if e in GLB['mem'][i]:
            return GLB['mem'][i][e]
    return None

def saving_univ_r(i, cur_e, bcut):
    if not (0 <= i < GLB['nqueries']):
        return 0
    if bcut <= 0:
        return INF
    memsol = remember(i, cur_e)
    if memsol is not None:
        return memsol
    # candidates
    qs = GLB['queries']
    c = [[index(qs, e, i), e] for e in GLB['engines'] if e != cur_e and e != qs[i] ]
    c.sort(key=lambda t: t[0], reverse=True)
    for t in c:
        j = t[0]
        e = t[1]
        #print j, e
        subsol = saving_univ_r(j, e, bcut - 1)
        bcut = min(bcut, subsol)
        t.append(subsol)
    c.sort(key=lambda t: t[2])
    if i == 0:
        sys.stderr.write(str(c) + '\n')
    sol = c[0][2] + 1
    save_mem(i, cur_e, sol)
    return sol

def saving_univ():
    sol = saving_univ_r(0, '', INF) - 1
    sol = max(0, sol)
    return sol

def main():
    read_input(sys.stdin)
    #sol = saving_univ()
    #print "solution:", sol


def get_id(line):
    if line not in GLB['naming']:
        gid = GLB['naming_counter']
        #gid = chr(gid)
        GLB['naming'][line] = gid
        GLB['naming_counter'] += 1
    return GLB['naming'][line]

def read_input(finp):
    sys.setrecursionlimit(10000)
    N = int(finp.readline())
    for n in xrange(N):
        GLB['queries'] = []
        GLB['engines'] = []
        GLB['naming'] = {}
        GLB['naming_counter'] = 5001
        GLB['mem'] = {}
        S = int(finp.readline())
        for s in xrange(S):
            line = finp.readline().strip('\n\r')
            line = get_id(line)
            GLB['engines'].append(line)
        Q = int(finp.readline())
        for q in xrange(Q):
            line = finp.readline().strip('\n\r')
            line = get_id(line)
            GLB['queries'].append(line)
        GLB['nqueries'] = len(GLB['queries'])
        sol = saving_univ()
        print 'Case #%d: %d' % (n+1, sol)
        #from com.moveki import progbase
        #progbase.yaml_dump('-', GLB)
    if False: print n, s, q

if __name__ == "__main__":
    main()
