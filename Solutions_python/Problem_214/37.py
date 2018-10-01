import sys

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

slash = [1, 0, 3, 2]
bslash = [3, 2, 1, 0]

def inbounds(M, x, y):
    return 0 <= x < len(M) and 0 <= y < len(M[0])

def _compute(M, i, j, d):
    ret = []
    x,y = i,j
    while True:
        x = x + dx[d]
        y = y + dy[d]
        if not inbounds(M, x, y):
            return ret
        
        ret.append((x,y))
        if M[x][y] == '/':
            d = slash[d]
        elif M[x][y] == '\\':
            d = bslash[d]
        elif M[x][y] == '#':
            return ret
        elif M[x][y] in ('|', '-'):
            return None

def compute(M, i, j, d):
    ret = _compute(M,i, j,d)
    ret2 = _compute(M,i, j,d + 2)
    if ret != None and ret2 != None:
        return ret + ret2
    return None

def sol(pos, M, tocover, choice):
    for i in xrange(pos, len(M) * len(M[0])):
        x = i / len(M[0])
        y = i % len(M[0])
        if M[x][y] == '.':
            covered = False
            for (x1,y1,dr) in tocover[x][y]:
                if choice[x1][y1] == dr:
                    covered = True
            if not covered:
                for (x1,y1,dr) in tocover[x][y]:
                    if choice[x1][y1] == -1:
                        choice[x1][y1] = dr
                        if sol(i+1, M, tocover, choice): return True
                        choice[x1][y1] = -1
                return False
    return True


def solve(P):
    [r, c] = map(int, sys.stdin.readline().split())
    M = [ sys.stdin.readline().strip() for i in xrange(r) ]
    tocover = [ [ [] for i in xrange(c) ] for j in xrange(r) ]
    choice = [ [ -1 for i in xrange(c) ] for j in xrange(r) ]

    for i in xrange(r):
        for j in xrange(c):
            if M[i][j] in ('-', '|'):
                h1 = compute(M, i, j, 0)
                if h1 != None:
                    for (x,y) in h1:
                        tocover[x][y].append((i,j,0))
                h2 = compute(M, i, j, 1)
                if h2 != None:
                    for (x,y) in h2:
                        tocover[x][y].append((i,j,1))
                if h1 == None and h2 == None:
                    print 'IMPOSSIBLE'
                    return
                if h1 == None:
                    M[i] = M[i][:j] + '|' + M[i][j+1:]
                if h2 == None:
                    M[i] = M[i][:j] + '-' + M[i][j+1:]

    if not sol(0, M, tocover, choice):
        print 'IMPOSSIBLE'
        return

    for i in xrange(r):
        for j in xrange(c):
            if choice[i][j] == 0:
                M[i] = M[i][:j] + '-' + M[i][j+1:]
            elif choice[i][j] == 1:
                M[i] = M[i][:j] + '|' + M[i][j+1:]
    print 'POSSIBLE'
    print '\n'.join(M)


if __name__ == '__main__':
	c = int(sys.stdin.readline())
	for i in range(c):
		sys.stdout.write('Case #%d: ' % (i+1,))
		solve(i)
