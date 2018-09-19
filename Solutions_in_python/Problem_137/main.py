from copy import deepcopy
debug = True

MINE = 1
NOT_MINE = 2
IMP_MINE = 3

ZERO_MINE = 4
ADJ_MINE = 5

def draw(t):
    t = zip(*t)
    s = ''
    for i in t:
        s += '\n' + ''.join(map(lambda x: '*' if x == MINE else 'c' if x == ZERO_MINE else '.', i)) 
    return s

def get_neighbors(t, i, j):
    C = len(t)
    R = len(t[0])
    for ci in (1, 0, -1):
        for cj in (1, 0, -1):
            if (ci != 0 or cj != 0) and 0 <= i + ci < C and 0 <= j + cj < R:
                yield (i + ci, j + cj)
                
def propage(t, i, j):
    t[i][j] = ZERO_MINE
    for ni, nj in get_neighbors(t, i, j):
        if t[ni][nj] == MINE:
            t[i][j] = ADJ_MINE
            break
    if t[i][j] == ZERO_MINE:
        for ni, nj in get_neighbors(t, i, j):
            if t[ni][nj] in (NOT_MINE, IMP_MINE):
                propage(t, ni, nj) 
    
def check(t):
    tt = t
    t = deepcopy(t)
    a = -1
    b = -1
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] != MINE:
                a, b = i, j
                break
    for nx, ny in get_neighbors(t, a, b):
        if t[nx][ny]  == ZERO_MINE:
            a, b = nx, ny
            break
    if a >= 0 and b >= 0:
        propage(t, a, b)
        if all([c != NOT_MINE and  c != IMP_MINE for y in t for c in y ]):
            tt[a][b] = ZERO_MINE
            return True
    else:
        count = 0
        for i in range(len(t)):
            for j in range(len(t[0])):
                if t[i][j] != MINE:
                    count += 1
                if count >= 2:
                    return False
        return True
    
def set_mine(t, i, j):
    t[i][j] = MINE
    changed = []
    for ci in (2, 0, -2):
        for cj in (2, 0, -2):
            if ci != 0 or cj != 0:
                if 0 <= i + ci < C and 0 <= j + cj < R:
                    if t[i + ci][j + cj] == NOT_MINE:
                        changed.append((i + ci, j + cj))
                        t[i + ci][j + cj] = IMP_MINE
    for nx, ny in get_neighbors(t, i, j):
        if t[nx][ny] == IMP_MINE:
            changed.append((nx, ny))
            t[nx][ny] = NOT_MINE
    return changed

def unset_mine(t, i, j, changed):
    t[i][j] = NOT_MINE
    for ii, jj in changed:
        t[ii][jj] = NOT_MINE + IMP_MINE - t[ii][jj]
            
        
def step(t, M, i, j, acc):
    #print '-'*10
    #print M, draw(t)
    if M <= 0:
        return check(t)

    C = len(t)
    R = len(t[0])
    count = acc + (R-j) + R * (C-i) + 1
    force = False
    if count == M:
        force = True
    elif count < M:
        return False
    if i >= C or j >= R:
        return  M <= 0 and check(t)

     
    possible = (t[i][j] != IMP_MINE)
  
    next_i = i 
    next_j = j + 1
    if next_j >= R:
        next_j = 0
        next_i = i + 1
        
    if (not force) and step(t, M, next_i, next_j, acc):
        return True
    
    if possible:
        changed = set_mine(t, i, j)
        if step(t, M - 1, next_i, next_j, acc+1):
            return True
        else:
            unset_mine(t, i, j, changed)
    return False
    
def resolve(R, C, M):
    table = [ [NOT_MINE] * R for _ in range(C)]
    i,j = 0, 0
    if M > R and C == 5 and R == 5:
        for x in range(R):
            set_mine(table, 0, x)
        i = 1
        M -= R
#     if R >= 4:
#         for i in (-2, 1):
#             table[0][i] = IMP_MINE
#             table[-1][i] = IMP_MINE
#     if C >= 4:
#         for i in (-2, 1):  
#             table[i][0] = IMP_MINE
#             table[i][-1] = IMP_MINE
    #for y in table: print y
    if step(table, M, i, j, 0):
        return draw(table)
    else:
        return "\nImpossible"
    

input_file = open('A-small-practice.in')
output_file = open('output', 'w')

T = int(input_file.readline())
for i in range(1, T + 1):
    R, C, M = map(int, input_file.readline().split())
    sol = 'Case #%d: %s\n' % (i, resolve(R, C, M))
    output_file.write(sol)
    if debug:
        print R, C, M, sol[:-1]

    
input_file.close()
output_file.close()

