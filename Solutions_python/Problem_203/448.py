entrada = open("A-large.in")
salida = open("a-output.txt", 'w')
cases = int(entrada.readline())
from collections import defaultdict
from pprint import pprint
for case in xrange(1, cases+1):
    r, c = map(int, entrada.readline().split())
    pos = defaultdict(list)
    salida.write("Case #" + str(case) + ":\n")
    matriz = [list(entrada.readline().strip()) for _ in xrange(r)]
    if case == 89:
        pprint(matriz)
    for i in xrange(r):
        for j in xrange(c):
            pos[matriz[i][j]].append((i,j))
    for letra in pos:
        if letra == "?":
            continue
        lista = pos[letra]
        lista.sort()
        p1 = lista[0]
        p2 = lista[-1]
        for i in xrange(p1[0], p2[0]+1):
            for j in xrange(p1[1], p2[1]+1):
                matriz[i][j] = letra
    pos = defaultdict(list)
    for i in xrange(r):
        for j in xrange(c):
            pos[matriz[i][j]].append((i,j))
    cants = [(len(pos[l]),l) for l in pos if l != "?"]
    cants.sort(reverse = True)
    for cant in cants:
        ci, l = cant
        lista = pos[l]
        lista.sort()
        i, j = lista[0], lista[-1]
        k = i[0]
        while k > 0:
            k -= 1
            salir = False
            for x in xrange(i[1],j[1]+1):
                if matriz[k][x] != "?":
                    salir = True
                    break
            if salir:
                k += 1
                break
            for x in xrange(i[1],j[1]+1):
                matriz[k][x] = l
        minr = k
        k = j[0]
        while k < r-1:
            k += 1
            salir = False
            for x in xrange(i[1],j[1]+1):
                if matriz[k][x] != "?":
                    salir = True
                    break
            if salir:
                k -= 1
                break
            for x in xrange(i[1],j[1]+1):
                matriz[k][x] = l
        maxr = k
        k2 = i[1]
        while k2 > 0:
            k2 -= 1
            salir = False
            for x in xrange(minr,maxr+1):
                if matriz[x][k2] != "?":
                    salir = True
                    break
            if salir:
                k += 1
                break
            for x in xrange(minr,maxr+1):
                matriz[x][k2] = l
        k2 = j[1]
        while k2 < c-1:
            k2 += 1
            salir = False
            for x in xrange(minr,maxr+1):
                if matriz[x][k2] != "?":
                    salir = True
                    break
            if salir:
                k -= 1
                break
            for x in xrange(minr,maxr+1):
                matriz[x][k2] = l
    for i in xrange(r):
        salida.write("".join(matriz[i])+"\n")

salida.close()