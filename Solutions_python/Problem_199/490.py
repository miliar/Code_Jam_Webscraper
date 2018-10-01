"""
Ejercicio 1
"""

import sys

def log(cadena):
    """ Muestra cadena por sys error """
    # print >> sys.stderr, cadena
    pass

def caso(linea):
    """ Resuelve un caso concreto """
    # P = map(int,P.split(" "))
    (pancakes, sK) = linea.split(" ")
    K = int(sK)

    log("Pancakes: %s | K = %d " % (pancakes, K))

    vueltas = 0
    # Mientras haya pancakes en el lado malo... (negativo)
    pc = pancakes.find("-")
    while (pc >= 0):
        if (pc + K) > len(pancakes):
            return "IMPOSSIBLE"
        vueltas = vueltas + 1
        for i in xrange(pc, pc+K):
            if pancakes[i] == '+':
                pancakes = pancakes[:i] + '-' + pancakes[i+1:]
            else:
                pancakes = pancakes[:i] + '+' + pancakes[i+1:]
        log("En el flip %d la cosa esta: %s" % (vueltas, pancakes))
        pc = pancakes.find("-")

    return vueltas

def problema():
    """ Funcion principal """
    namefile = "A-large"
    fichero = open(namefile + ".in", "r")

    casos = int(fichero.readline())

    for i in xrange(1, casos+1):

        log("---------- Caso %d de %d" % (i, casos))

        linea = fichero.readline()
        print "Case #%d: %s" % (i, caso(linea))


if __name__ == "__main__":
   problema()
