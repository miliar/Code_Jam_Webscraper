#!/usr/bin/python

def distancia(A, B):
    x = (A[0] - B[0])**2
    y = (A[1] - B[1])**2
    return (x + y)**0.5 + A[2] + B[2]

for case in range(input()):
    lista = []
    N = input()
    for i in range(N):
        X, Y, R = map(int, raw_input().split())
        lista.append([X, Y, R])

    dist = []
    if (N == 3):
        for i in range(N):
            for j in range(i+1, N):
                dist.append(distancia(lista[i], lista[j]))
        sol = float(min(dist))/2
    else:
        for i in range(N):
            dist.append(lista[i][2])
        sol = max(dist)

    print 'Case #%s: %.7f' % (case + 1, sol)

