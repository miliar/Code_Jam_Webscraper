#!/usr/bin/python

#def giveCombinations(lista):
rr = lambda n,k: (n > 0) and [k%n] + rr(n-1,k/n) or []
dfr = lambda rs: len(rs) and rs[:1] + [r + (rs[0]<=r) for r in dfr(rs[1:])] or []
perm = lambda xs,k: [xs[i] for i in dfr(rr(len(xs),k))]

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

#for k in range(24):
#    print "".join(perm("perm",k))
def calculaFact():
    lista = []
    for i in range(10):
        lista.append(factorial(i))
    return lista

def getSolution(number, div_len):
    resto_s = str(number)
    resto_s += '0'*(div_len - len(resto_s))
#        print 'Resto ' + resto_s 
    lista = [int("".join(perm(resto_s, k))) for k in range(factoriales_l[len(resto_s)])]
    lista = list(set(lista))
    lista.sort()
    i = 0
    while (i < len(lista)) and (lista[i] <= number):
        i += 1
    if (i < len(lista)):
#            print resto
#            print lista
#            print 'I = %s' % i
        return lista[i]
    else:
        return -1

factoriales_l = calculaFact()
for case in range(input()):
    num = input()
#    print 'Num = %s' % (num)
    div = 100
    div_len = 2
    found = 0
    sol = -1
    while ((num / div) != 0) and (not found):
        resto = num % div
        pos_sol = getSolution(resto, div_len)
        if (pos_sol != -1):
            sol = (num / div) * div + pos_sol
            found = 1
        else:
            div = div*10
            div_len += 1

    if (sol == -1):
        resto_s = str(num)
        resto_s += '0'*(div_len - len(resto_s))
        lista = [int("".join(perm(resto_s, k))) for k in range(factoriales_l[len(resto_s)])]
        lista = list(set(lista))
        lista.sort()
        i = 0
        while (i < len(lista)) and (lista[i] <= num):
            i += 1
        if (i < len(lista)):
#            print 'I = %s' % i
            sol = lista[i]
            #sol = (num / div) * div + lista[i]
            found = 1
    
    while (sol == -1):
        div_len += 1
        sol = getSolution(num, div_len)

    print 'Case #%s: %s' % (case + 1, sol)
