def copyT(T):
    return [x[:] for x in T]

def isGrid(R,C,T,c):
    posi = set()
    posj = set()
    pos  = set()
    for i in range(R):
        for j in range(C):
            if T[i][j] == c:
                posi.add(i)
                posj.add(j)
                pos.add((i,j))
    posi = sorted(list(posi))
    posj = sorted(list(posj))
    mi, ni = max(posi), min(posi)
    mj, nj = max(posj), min(posj)
    posi = list(range(ni, mi+1))
    posj = list(range(nj, mj+1))
    for i in posi:
        for j in posj:
            if T[i][j] != c and T[i][j] != '?':
                return False
    return True

def f2(R,C,T,chars):
    i, j = -1, -1
    for x in range(R):
        for y in range(C):
            if T[x][y] == '?':
                i, j = x, y
                break
        if (i,j) != (-1, -1):
            break
    if (i, j) == (-1, -1):
        return T

    CT = copyT(T)
    for c in chars:
        #CT = copyT(T)
        CT[i][j] = c
        #print(c, isGrid(R,C,CT,c), CT)
        if isGrid(R,C,CT,c):
            res = f2(R,C,CT,chars)
            if res != False:
                return res

    return False


def f(R,C,T):
    chars = []
    for row in T:
        for t in row:
            if t != '?':
                chars.append(t)

    CT = copyT(T)
    return f2(R,C,CT,chars)

fin = open('al.in')
fout = open('al.out','w')

T = int(fin.readline())

for t in range(1, T+1):
    print(t)
    R, C = [int(x) for x in fin.readline().split()]
    T = []
    for _ in range(R):
        T.append(list(fin.readline())[:-1])
    fout.write('Case #%s:\n' % t)
    res = f(R,C,T)
    for row in res:
        fout.write(''.join(row) + '\n')
fout.close()