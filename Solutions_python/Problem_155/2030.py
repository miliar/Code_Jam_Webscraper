import sys
import math

filename = 'A-large'
f = open(filename+'.in.txt', 'r')
fo = open(filename+'.out.txt', 'w')

N = int(f.readline().strip())

for n in range(N):
    Smax, S = f.readline().strip().split()
    S = [int(i) for i in list(S)]

    stand_p = 0
    invited = 0
    for Si, nb in enumerate(S):
        if Si > stand_p:
           invited += Si - stand_p
           stand_p += Si - stand_p
        stand_p += nb

    fo.write("Case #{}: {}\n".format(n+1, invited))

