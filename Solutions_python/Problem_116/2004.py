import sys
import pdb

T = int(sys.stdin.readline().strip())

def check(m, C):
    
    for r in range(4):
        if m[r].count(C) + m[r].count('T') == 4:
            return True

    if sum(1 for c in range(4) if m[c][c] == C or m[c][c] == 'T') == 4:
        return True

    if sum(1 for c in range(4) if m[c][4-c-1] == C or m[c][4-c-1] == 'T') == 4:
        return True

    n = zip(*m)
    for r in range(4):
        if list(n[r]).count(C) + list(n[r]).count('T') == 4:
            return True
    
    return False 

for i in range(T):
    m = []
    for r in range(4):
        m.append(list(sys.stdin.readline().strip()))
    sys.stdin.readline()
    print "Case #" + str(i+1) + ":",
    if check(m, 'X'):
        print "X won"
    elif check(m, 'O'):
        print "O won"
    elif sum( sum(1 for c in row if c == '.') for row in m) > 0: 
        print "Game has not completed"
    else:
        print "Draw"
    
