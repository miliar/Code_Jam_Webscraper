'''
Created on 14/04/2012

@author: david
'''

class Reverso(object):
    '''
    classdocs
    '''
    numero = 0
    min = 0
    max = 0
    listaReversos = []
    

    def __init__(self, numero, min, max):
        self.numero = numero
        self.max = max
        self.min = min
    
    def construyeListaReversos(self):
        cad = str(self.numero)
        aux = []
        for i in range(1, len(cad)):
            auxCad = cad[i:]+cad[:i]
            if auxCad[0]!= 0:
                intAux = int(auxCad)
                if cad != auxCad and intAux >= self.min and intAux <= self.max and aux.count(intAux) == 0:
                    aux.append(intAux)
        self.listaReversos = aux    
    
    def getListaReversos(self):
        return self.listaReversos

        