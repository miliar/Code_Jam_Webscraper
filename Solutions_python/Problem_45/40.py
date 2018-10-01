import re

#f = open('C-test.in')
f = open('C-small.in')
#f = open('C-large.in')
lines = [line.strip('\n') for line in f.readlines()]
N = int(lines.pop(0))

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

def compute_bribe(P,Q,p):
    cells = [1]*P
    sum = 0
    for q in range(Q):
        i = p[q]-1
        cells[i] = 0 
        for j in range(i+1,P):
            if cells[j] == 0:
                break
            else:
                sum += 1
        for k in range(i-1,-1,-1):
            if cells[k] == 0:
                break
            else:
                sum += 1
    return sum

for j in range(N):
    P,Q = [int(i) for i in lines.pop(0).split(' ')]
    C = 10000
    for p in all_perms([int(i) for i in lines.pop(0).split(' ')]):
        _C = compute_bribe(P,Q,p)
        if _C < C:
            C = _C
    print "Case #%d: %d"%(j+1,C)
