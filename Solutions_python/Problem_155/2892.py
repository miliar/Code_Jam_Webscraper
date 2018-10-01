import sys


def main():

        #numero de casos
        casos = raw_input()
        resultado={}

        i = 0
        while(i < int(casos)):
                caso = raw_input()
                max = ''
                k = 0
                for x in caso:
                        max = max + x
                        k = k+1
                        if(x==' '):
                                break
                max = int(max)
                ajudas = 0
                totalp = 0

                j = 0
                while(j <= max):
                        pessoas = int(caso[k])

                        if(k==2 and pessoas==0):
                                ajudas = 1

                        elif(pessoas != 0 ):
                                if((totalp+ajudas) < j):
                                        ajudas = ajudas + (j-(totalp+ajudas))

                        totalp = totalp + pessoas
                        k = k+1
                        j = j+1

                resultado[i] = ajudas

                i=i+1


        for i in range(0,int(casos)):
                print "Case #"+str(i+1)+": " + str(resultado[i])



main()
