import sys
from operator import mul

def snap(snappers,snaps):
    lista_de_snappers = [0]
    lista_de_energia = [1]
    for i in range(snappers-1):
        lista_de_snappers.append(0)
        lista_de_energia.append(0)
    for i in range(snaps):
        for j in range(snappers):
            if (lista_de_energia[j] == 1):
                if (lista_de_snappers[j] == 0):
                    lista_de_snappers[j] = 1;
                else:
                    lista_de_snappers[j] = 0;
        for j in range(snappers):
            if (lista_de_energia[j-1] == 1) and (lista_de_snappers[j-1] == 1):
                lista_de_energia[j] = 1
            else:
                lista_de_energia[j] = 0
            if j == 0:
                lista_de_energia[j] = 1
    resultado = reduce(mul,lista_de_snappers)
    if resultado == 1:
        return "ON"
    else:
        return "OFF"
            
        
    

def prepare_to_snap(arquivo):
    file = open (arquivo,"r")
    resultado = open ("resultado.out","w")
    sys.stdout = resultado
    numero_de_casos = int(file.readline())
    for i in range(numero_de_casos):
        (snappers,snaps)=file.readline().split()
        snappers = int(snappers)
        snaps = int(snaps)
        string = snap(snappers,snaps)
        print "Case #%i: %s" % (i+1,string) 
            

if __name__ == "__main__":
    prepare_to_snap(sys.argv[1])
