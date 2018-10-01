'''
Created on 13/04/2013

@author: Carles
'''

import math

def creaListaPalindromos(maximo,lista):
    for i in range(1,maximo):
        if esPalindromo(i):
            if esPalindromo(i*i):
                lista.append(i*i)

def esPalindromo(x):
    pal = str(x)
    l = len(pal)
    if l>1:
        for i in range(math.trunc(l/2)):
            if pal[i] != pal[l-i-1]:
                return False
    return True

def trataCaso(inFile, lista):
    linea = inFile.readline()
    minimo = int(linea.partition(' ')[0])
    maximo = int(linea.partition(' ')[2])
    cont = 0
    
    i = 0
    fin = len(lista)
     
    while(i<=fin-1):
        if lista[i]>=minimo and lista[i]<=maximo:
            cont +=1
        i+=1
                
    return cont

    

def main():
    inFile = open('input.in', 'r')
    outFile = open('output.out', 'w')
    
    lista = []
    creaListaPalindromos(int(math.sqrt(10000000000000)),lista)

    numCasos = int(inFile.readline())

    for i in range(numCasos):
        outFile.write("Case #"+str(i+1)+": "+str(trataCaso(inFile,lista))+"\n")
        #print trataCaso(inFile)
        
        
if __name__ == "__main__":main()