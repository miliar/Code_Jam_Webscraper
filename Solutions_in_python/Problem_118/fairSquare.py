'''
Created on 13/04/2013

@author: Rafael
'''
def cuadradoPalindromos(listaPalindromo):
    listResult=[]
    for i in listaPalindromo:
        listResult.append(i*i)
    return listResult



def hallaPalindromo(minNum, maxNum):
    list = range(minNum, maxNum + 1)
    listPalindromo = []
    listaPalindromoCuadrado = []
    for i in list:
        cad = str(i)
        bandera = False
        if len(cad) == 1:
            listPalindromo.append(i);
        else:
            if len(cad) % 2 == 0:
                pivote = int(len(cad) / 2)
                bandera = validaPalindromo(pivote, cad)
            else:
                pivote = int(len(cad) / 2)
                bandera = validaPalindromo(pivote, cad[:pivote] + cad[pivote + 1:])
        
        if(bandera == True):
            listPalindromo.append(i)
    listaPalindromoCuadrado = cuadradoPalindromos(listPalindromo)
    
    listaPalindromoAux = []
    for i in listaPalindromoCuadrado:
        cad = str(i)
        bandera = False
        if len(cad) == 1:
            listaPalindromoAux.append(i);
        else:
            if len(cad) % 2 == 0:
                pivote = int(len(cad) / 2)
                bandera = validaPalindromo(pivote, cad)
            else:
                pivote = int(len(cad) / 2)
                bandera = validaPalindromo(pivote, cad[:pivote] + cad[pivote + 1:])
        
        if(bandera == True):
            listaPalindromoAux.append(i)
    
    return len(listaPalindromoAux)


        
def validaPalindromo(pivote, cadena):
    j = 0
    for i in range(1, pivote + 1):
        if(cadena[pivote - i] != cadena[pivote + j]):
            return False
        j += 1
    return True

if __name__ == '__main__':
    fileIn = open("C-small-attempt0.in")
    iter = int (fileIn.readline())
    l = range(iter)
    listaEntrada = []
    listaPalindromos = []
    for i in l:
        cad = fileIn.readline()
        cad = cad[:-1]
        auxList = cad.split(" ")
        listaEntrada.append(auxList)
    fileIn.close()
    for i in listaEntrada:
        list = []
        min =  pow(int(i[0]), 0.5)
        if(min%1!=0):
            min=min+1
        min = "%.2f" % min
        max = "%.2f" % pow(int(i[1]), 0.5)
        listaPalindromos.append( hallaPalindromo(int(min[:-3]), int(max[:-3])))
    fileOut = open("output.txt",'w')
    for i in range(len(listaPalindromos)):
        fileOut.writelines("Case #%d: %s" % (i + 1, listaPalindromos[i])+'\n')
    fileOut.close()
    
