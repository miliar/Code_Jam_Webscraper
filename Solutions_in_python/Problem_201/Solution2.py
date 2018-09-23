def compBase2(N):
    i = 0
    suma = 0
    while suma < N:
        suma = suma + 2 ** i
        i = i + 1
    if (suma == N):
        return i - 1, 2 ** (i - 1)
    return i - 1, N - (suma - 2 ** (i - 1))

from math import floor, ceil

def divMultiple(N, cantDiv):
    while cantDiv > 0:
        N = (N - 1) / 2
        cantDiv = cantDiv - 1
    return N

def resEcuation(result, cantDiv):
    if floor(result) != ceil(result):
        x = (2 ** cantDiv) * (result - floor(result)) / (ceil(result) - floor(result))
        y = (2 ** cantDiv) - x
        return (ceil(result), x), (floor(result), y)
    else:
        return (result, 2 ** cantDiv), (0, 0)

def procesar(N):
    if N % 2 == 0:
        h = (N - 1) / 2
        return ceil(h), floor(h)
    else:
        h = (N - 1) / 2
        return h, h

T = int(input())
for i in range(1, T + 1):
    N, K = [int(s) for s in input().split(" ")]
    cantDiv, Resto = compBase2(K)    
    resDivMult = divMultiple(N, cantDiv)
    (fX, X), (fY, Y) = resEcuation(resDivMult, cantDiv)
    if Resto > X:
        maximo, minimo = procesar(fY)
    else:
        maximo, minimo = procesar(fX)
    print("Case #{}: {} {}".format(i, int(maximo), int(minimo)))

