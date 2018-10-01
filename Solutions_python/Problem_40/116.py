#!/usr/bin/python

class Arbol:
    def __init__(self, porcentaje, nombre, padre, izda=None, dcha=None):
        self.porcentaje = porcentaje
        self.nombre = nombre
        self.padre = padre
        self.izda  = izda
        self.dcha = dcha

    def __str__(self):
        return str(self.datos) 

    def __str__(nombre):
        return self.nombre


def convertFloat(num):
    value = -1.0
    try:
        value = float(num)
    except ValueError:
        value = -1.0
    return value

def recursiveFound(arbol, i, last_parent):
#    print '0.- %s, %s, %s' % (arbol, i, last_parent)
    if ((i < len(arbol)-1) and (convertFloat(arbol[i+1]) == -1.0)):
#        print 'HI'
        hijoIzda, arbol = recursiveFound(arbol, i+2, arbol[i+1])
#        print 'HD'
        hijoDcha, arbol = recursiveFound(arbol, i+2, arbol[i+1])
        padre = Arbol(float(arbol[i]), arbol[i+1], last_parent, hijoIzda, hijoDcha)
#        print '1- ',
#        print arbol
        arbol_temp = arbol[:i]
        arbol_temp.extend(arbol[i+2:])
#        print arbol_temp
        return padre, arbol_temp
    else:
#        print '2- ',
#        print arbol
        arbol_temp = arbol[:i]
        arbol_temp.extend(arbol[i+1:])
#        print arbol_temp
        return Arbol(float(arbol[i]), '', last_parent), arbol_temp

def calculaProb(nodo, prob, lista):
    if (nodo != None):
        prob *= nodo.porcentaje
        if (nodo.nombre in linea):
            prob = calculaProb(nodo.izda, prob, linea)
        else:
            prob = calculaProb(nodo.dcha, prob, linea)
    return prob

for case in range(input()):
    print 'Case #%s:' % (case + 1)
    L = input()
    arbol_s = []
    for i in range(L):
        linea = raw_input()
        linea = linea.replace('(', '')
        linea = linea.replace(')', '')
        datos = linea.split()
        arbol_s.extend(datos)

    count = 1
    my_arbol, borrar = recursiveFound(arbol_s, 0, '')

    A = input()
    for i in range(A):
        linea = raw_input().split()
        linea = linea[2:]
        sol = calculaProb(my_arbol, 1, linea)
        print '%.7f' % (sol)

