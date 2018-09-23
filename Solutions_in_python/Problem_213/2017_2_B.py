# -------------------------
# Google Code Jam 2017
# Round 2
# 2017 May 13
# Brendan Wood
# brendanwood1989@gmail.com
# -------------------------
filename = 'B-small-attempt2'

def solve(N,C,M,tickets):
    
    C1 = []
    C2 = []
    
    for ticket in tickets:
        if   ticket[1] == 1:
            C1.append(ticket[0])
        elif ticket[1] == 2:
            C2.append(ticket[0])
        
    rides = 0
    C1.sort()
    C2.sort()

    used = []    
    for t1 in C1:
        pair = False
        for t2 in C2:
            if t2 > t1:
                used.append(t1)
                C2.remove(t2)
                pair = True
                break
        if not pair:
            break
    
    for t1 in used:
        C1.remove(t1)
        rides += 1
        
    used = []
    for t2 in C2:
        pair = False
        for t1 in C1:
            if t1 > t2:
                used.append(t2)
                C1.remove(t1)
                pair = True
                break
        if not pair:
            break
    
    for t2 in used:
        C2.remove(t2)
        rides += 1

    if not C1:
        rides += len(C2)
        return str(rides) + ' 0'
        
    if not C2:
        rides += len(C1)
        return str(rides) + ' 0'
            
    if C1[0] == 1 or C2[0] == 1:
        rides += len(C1)
        rides += len(C2)
        return str(rides) + ' 0'
    
    rides += max(len(C1),len(C2))
    proms = min(len(C1),len(C2))
    
    return str(rides) + ' ' + str(proms)

    
with open(filename+'.in') as f:
    data = f.read().splitlines()

f = open(filename+'.out', 'w')

T = int(data.pop(0))

for case in range(T):
    N,C,M = map(int,data.pop(0).split())
    tickets = []
    for m in range(M):
        tickets.append(list(map(int,data.pop(0).split())))
    f.write('Case #{}: {}\n'.format(case+1,solve(N,C,M,tickets)))
        
f.close()