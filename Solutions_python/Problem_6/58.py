#
# numbers.py





#**********************
# SECTOR DE FUNCIONES
#**********************

from real import *

def mod1000(floater):
    n=floor(floater)
    return int(n % 1000)


def magicn(n):
    return (3+sqrt(5))**n
    #return newton(3,sqrt(5),n)

def factorial(n):
    prod=1
    for i in xrange(1,n+1):
        prod=prod*i
    return prod

def binom(n,k):
    if(n<k):
        print 'error de definicion de binomio'
        return None
    return (factorial(n)/(factorial(k)*factorial(n-k)))

def newton(x,y,n):
    suma=0
    for k in xrange(0,n+1):
        suma+= binom(n,k)*(x**(n-k))*(y**k)
    return suma

def mariostring(integer):
    u= integer % 10
    d= int(floor(integer/10)) % 10
    c= int(floor(integer/100)) % 10
    return str(c)+str(d)+str(u)





#******************************
# SECTOR DE CODIGO DE PROGRAMA
#******************************


file=open('./C-small-attempt2.in','r')
#you can change the name to get the input from other file
# I'm sorry for my bad programming, I'm new to python :D
#and comments are in english and spanish because I'm from argentina




N=file.readline().strip('\n')
#print N

acumulador_rta=''
for i in xrange(0,int(N)):
	n=file.readline().strip('\n')
	rta=mariostring(mod1000(magicn(int(n))))
	acumulador_rta=acumulador_rta +'Case #'+str(i+1)+': '+ str(rta) +'\n'
	

file.close()

file_dest=open('./C-small-attempt2.out','w')
file_dest.write(acumulador_rta)

file_dest.close()
