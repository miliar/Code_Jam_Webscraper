"""
Ejercicio 3
"""

import sys

def log(cadena):
    """ Muestra cadena por sys error """
    print >> sys.stderr, cadena
    pass

def caso(linea):
    """ Segunda forma """
    (N, K) = map(int, linea.split(" "))

    # la suma tiene que dar...
    sitios_libres = N-K


    entraron_previamente = 0
    fac = 1
    while entraron_previamente < K:
        entraron_previamente = entraron_previamente + fac
        fac = fac*2
    fac = fac/2
    entraron_previamente = entraron_previamente - fac

    sitios_libres = N - K
    media = sitios_libres / (fac*2)

    log("Para N=%d K=%d. Sitios libres=%d. Entraron previamente %d. fac = %d, media = %d" % (N, K, sitios_libres, entraron_previamente, fac, media))

    subtotal = media*2*fac
    reparto = sitios_libres - subtotal
    quedan = subtotal - reparto
    log("subtotal %d, reparto %d, quedan = %d" % (subtotal, reparto, quedan))

    if reparto > entraron_previamente:
        return "%d %d" % (media + 1, media)
    else:
        return "%d %d" % (media, media)

    if K == 1:
        return "%d %d" % (N/2, (N-1)/2)
    else:
        return "NOSE"



def caso2(linea):
    """ Resuelve un caso concreto """
    # P = map(int,P.split(" "))
    # (pancakes, sK) = linea.split(" ")
    (N, K) = map(int, linea.split(" "))
    #(N, K) = (54323454645432,453523454523)
    log("Entrada: %s.  N = %d . K = %d" % (linea, N, K))

    grupo = N
    i = 1
    fac = 1
    a = grupo / 2
    b = (grupo-1)/2 
    personas = 0
    while K >= i:
        personas = personas + i
        a = grupo/2
        b = (grupo-1)/2 
        log("Inter %d - a=%d b=%d. Llevan %d personas" % (i, a, b, personas))
        # i = i + 1
        if i == fac:
            fac = fac*2
            i = fac
            grupo = grupo / 2
        else:
            i = i + 1

    log("Acaba el bucle")
    if personas > K:
        return caso("%d %d" % (a*2, K-(personas/2)))
    else:
        return "%d %d" % (a,b)
    



        

def problema():
    """ Funcion principal """
    namefile = "C-large"
    # fichero = open("/home/michi/code/codejam/eje3/" + namefile + ".in", "r")
    fichero = open("/home/michi/code/codejam/eje3/" + namefile + ".in", "r")

    casos = int(fichero.readline())
    log("---------- Casos: %d" % (casos))

    for i in xrange(1, casos+1):

        log("---------- Caso %d de %d" % (i, casos))

        linea = fichero.readline().rstrip('\n')
        print "Case #%d: %s" % (i, caso(linea))


if __name__ == "__main__":
    # print donde_rompe("54")
    problema()
    """
    print "#################################################3"
    """
    """
    print "-caso 1001 1:", caso("1001 1")
    print "-caso 1001 2:", caso("1001 2")
    print "-caso 1001 3:", caso("1001 3")
    print "-caso 1001 4:", caso("1001 4")
    print "-caso 1001 5:", caso("1001 5")
    print "-caso 1001 6:", caso("1001 6")
    print "-caso 1001 7:", caso("1001 7")
    """
    """
    print "-caso 12 1:", caso("12 1")
    print "-caso 12 2:", caso("12 2")
    print "-caso 12 3:", caso("12 3")
    print "-caso 12 4:", caso("12 4")
    print "-caso 12 5:", caso("12 5")
    print "-caso 12 6:", caso("12 6")
    print "-caso 12 7:", caso("12 7")
    print "-caso 12 8:", caso("12 8")
    print "-caso 12 9:", caso("12 9")
    print "-caso 12 12:", caso("12 12")
    """
