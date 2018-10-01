# -------------------------
# Google Code Jam 2017
# Round 1A
# 2017 April 14
# Brendan Wood
# brendanwood1989@gmail.com
# -------------------------
filename = 'B-large'

import math

def findpossibles(minimum, maximum, n, S):
    possibles = []
    for rng in S[n]:
        if rng[0] > maximum:
            break
        if rng[1] < minimum:
            continue
        possibles.append(rng)
    return possibles

   
def makekit(N, n, S, i, kit, minimum, maximum):
    
    for rng in S[n]:
        if S[0][i][0] and rng[0]:
            if rng[1] > maximum:
                break
            if rng[2] < minimum:
                continue
            
            newkit = kit + [rng]
            newmin = max(minimum, rng[1])
            newmax = min(maximum, rng[2])
            
            if n+1 == N:
                S[0][i][0] = False
                return newkit
            else:
                return makekit(N,n+1,S,i,newkit,newmin,newmax)
     
def solve(N,P,R,Q):
    for ingredient in Q:
        ingredient.sort()
    
    S = []    
    for i in range(N):
        S.append([])
        for quant in Q[i]:
            minimum = math.ceil(quant/R[i]/1.1)
            maximum = math.floor(quant/R[i]/0.9)
            if maximum >= minimum:
                S[i].append([True,minimum,maximum])
    
    if N == 1:
        return len(S[0])
    
    kits = 0
    for i in range(len(S[0])):
        kit = makekit(N,1,S,i,[S[0][i]],S[0][i][1],S[0][i][2])
        if kit:
            for i in range(1,N):
                j = S[i].index(kit[i])
                S[i][j][0] = False
            kits += 1   
    
    return kits
    
with open(filename+'.in') as f:
    data = f.read().splitlines()

f = open(filename+'.out', 'w')

T = int(data.pop(0))

for case in range(T):
    N,P = map(int,data.pop(0).split())
    R = list(map(int,data.pop(0).split()))
    Q = []
    for ingredient in range(N):
        Q.append(list(map(int,data.pop(0).split())))
    f.write('Case #{}: {}\n'.format(case+1,solve(N,P,R,Q)))
        
f.close()