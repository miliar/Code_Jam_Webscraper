import math, collections, copy, sys
f = open('input.in','r')
g = open('output.txt','w')
"""
sort and greedy
"""
for index in xrange(1, int(f.readline()[:-1]) + 1):
    N, P = [int(x) for x in f.readline()[:-1].split(' ')]
    R = [int(x) for x in f.readline()[:-1].split(' ')]
    Q = [0]*N
    for i in xrange(N):
        Q[i] = sorted(int(x) for x in f.readline()[:-1].split(' '))
    for i in xrange(N):
        Q[i] = [ (math.ceil(x/(1.1*R[i])), math.floor(x/(0.9*R[i]))) for x in Q[i]]
    I = [0]*N
    result = 0
    M = max(xrange(N), key = lambda i:Q[i][I[i]])
    max_val0 = Q[M][I[M]][0]
    max_val1 = Q[M][I[M]][1]
    while all(I[i] < P for i in xrange(N)):
        sign = True
        for i in xrange(N):
            while I[i] < P and Q[i][I[i]][1] < max_val0:
                sign = False
                I[i] += 1
            if I[i] == P:
                sign = False
                break
        if sign:
            result += 1
            I = [i+1 for i in I]
        if all(I[i] < P for i in xrange(N)):
            M = max(xrange(N), key = lambda i:Q[i][I[i]])
            max_val0 = Q[M][I[M]][0]
            max_val1 = Q[M][I[M]][1]
    g.write("Case #{}: {}\n".format(index, result))
    print "Case #{}: {}\n".format(index, result)
f.close()
g.close()