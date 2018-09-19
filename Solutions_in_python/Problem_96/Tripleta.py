'''
Created on 13/04/2012

@author: david
'''

class Tripleta(object):
    '''
    classdocs
    '''
    __c = 0
    __b = 0
    __a = 0
    __suma = 0
    __supera = False


    def __init__(self, numero):
        self.__suma = numero 
        if numero % 3 == 0:
            self.__a = numero / 3
            self.__b = self.__a
            self.__c = self.__a
        elif numero % 3 == 1:
            self.__a = numero / 3
            self.__b = self.__a
            self.__c = self.__a + 1
        else:
            self.__a = numero / 3
            self.__b = self.__a + 1
            self.__c = self.__a + 1
    
    def __cmp__(self, other):
        return cmp(other.getSuma(),self.__suma)
            
    def convierteSorpresa(self):
        if self.__a == self.__b and self.__b == self.__c:
            if self.__suma != 0:
                self.__c += 1
                self.__a -= 1
        elif self.__a == self.__b and self.__b != self.__c:
            if self.__suma != 1:
                self.__a -= 1
                self.__b += 1
        elif self.__a != self.__b and self.__b == self.__c:
            self.__b -= 1
            self.__c += 1

    def superaExpec(self, tope):
        if self.__c >= tope:
            self.__supera = True
            
    def getSuma(self):
        return self.__suma
    
    def menorIgual(self, otro):
        if(self.__suma <= otro.getSuma()):
            return True
        else:
            return False  
    
    def getSupera(self):
        return self.__supera
    
    def getC(self):
        return self.__c
