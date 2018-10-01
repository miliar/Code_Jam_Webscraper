
import numpy as np

for T in range(1, int(input()) + 1):
    ans = 0
    line = raw_input().split(' ')
    N = int(line[1])
    D = float(line[0])
    K = []
    S = []
    for i in range(N):
        line = raw_input().split(' ')
        K.append(float(line[0]))
        S.append(float(line[1]))
    t = []
    for i in range(N):
        t.append((D-K[i])/S[i])
    maxt = max(t)               
    ans = D/maxt
    print('Case #%d: %.6f'%(T,ans))