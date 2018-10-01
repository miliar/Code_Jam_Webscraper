import os
import sys
import math

def check(N,M,q,i,j):
    xmin = q[i][j]

    vert = 0
    for w in xrange(0,N):
        vert += q[w][j]
    
    hor = 0
    for w in xrange(0,M):
        hor += q[i][w]

    if hor  == xmin * M: return True
    if vert == xmin * N: return True

    return False

def main(f):
    inFile = open(f)
    
    T = int(inFile.readline())

    r = []
    for i in xrange(0, T):
        v = inFile.readline()
        [N,M] = map(lambda x: int(x), v.split(' '))

        q = []
        xmin = 100
        for n in xrange(0,N):
            v = inFile.readline().replace('\n','')
            q += [map(lambda x: int(x), v.split(' '))]

            xmin = min(xmin, min(q[-1]))

        z = True
        for i in xrange(0,N):
            for j in xrange(0,M):
                if z and q[i][j]==xmin:
                    z = check(N,M,q,i,j)

        if z: res = 'YES'
        else: res = 'NO'
        r.append(res)

    outFile = open(f.replace('.in', '.out'), 'w')
    for i in xrange(0, T):
        outFile.write('Case #%d: %s\n' % ((i+1), r[i]))
    outFile.close

if __name__ == '__main__':
    main('%s/%s' %(os.path.dirname(sys.argv[0]), 'B-small-attempt0.in'))

