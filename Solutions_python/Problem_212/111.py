# -------------------------
# Google Code Jam 2017
# Round 2
# 2017 May 13
# Brendan Wood
# brendanwood1989@gmail.com
# -------------------------
filename = 'A-large'

def p2(M):
    new = M
    return new

def p3(M):
    new = []

    M0 = M.count(0)
    M1 = M.count(1)
    M2 = M.count(2)

    while M0:
        new.append(0)
        M0 -= 1
    
    while M1 and M2:
        new.append(1)
        new.append(2)
        M1 -= 1
        M2 -= 1
    
    while M1:
        new.append(1)
        M1 -= 1
    
    while M2:
        new.append(2)
        M2 -= 1
    
    return new

def p4(M):
    new = []
    
    M0 = M.count(0)
    M1 = M.count(1)
    M2 = M.count(2)
    M3 = M.count(3)

    while M0:
        new.append(0)
        M0 -= 1
    
    while M1 and M3:
        new.append(1)
        new.append(3)
        M1 -= 1
        M3 -= 1

    while M2:
        new.append(2)
        M2 -= 1
        
    while M1:
        new.append(1)
        M1 -= 1
    
    while M3:
        new.append(3)
        M3 -= 1
    
    return new    

def solve(N,P,G):

    M = []
    for g in G:
        M.append(g%P)
    M.sort()
    
    if   P == 2:
        M = p2(M)
    elif P == 3:
        M = p3(M)
    elif P == 4:
        M = p4(M)

    fresh = 0
    total = 0
    for m in M:
        if total % P == 0:
            fresh += 1
        total += m

    return fresh
    
with open(filename+'.in') as f:
    data = f.read().splitlines()

f = open(filename+'.out', 'w')

T = int(data.pop(0))

for case in range(T):
    N,P = map(int,data.pop(0).split())
    G = list(map(int,data.pop(0).split()))
    f.write('Case #{}: {}\n'.format(case+1,solve(N,P,G)))
        
f.close()