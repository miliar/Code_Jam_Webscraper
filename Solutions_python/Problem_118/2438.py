#!/usr/bin/python
from math import *
def ispalindrome(n):
	cadena = n
	cont = 0
	cadena2="";
	es = 1
	for i in cadena:
		if i.isupper():
			i= i.lower()
		if i != " ":
			cadena2 = cadena2 + i
			cont = cont + 1
	for i in range(cont/2):
		if cadena2[i] != cadena2[cont-i-1]:
			es = 0
			break
	if (es):
		return True
	else:
		return False


def main():
	fichero = open("input.txt","r");
	n_casos = int(fichero.readline())
	for bucle in range(1,n_casos+1):
		tuplaab = fichero.readline().split(" ")
		inicio = int(tuplaab[0])
		final = int(tuplaab[1])
		cont = 0
		for num in range (inicio,final+1):
			raiz = sqrt(num)
			if ispalindrome(str(num)) and (raiz - int(raiz))==0 and ispalindrome(str((int(raiz)))):
				cont+=1
		print "Case #"+str(bucle)+": "+str(cont)
	fichero.close()
	return 0

if __name__ == '__main__':
	main()

