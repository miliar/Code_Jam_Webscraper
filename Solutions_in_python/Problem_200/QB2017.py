archivo=open('B-large.in')

archivo.readline()

lista=[]

for linea in archivo.readlines():
	lista.append (int(linea))
	

	
def numOrdenado (entero):
	num=entero
	while num >= 10:
		if num%10 < (num/10)%10:
			return False
		num/=10
	return True
	
def funcion (caso):
	if numOrdenado (caso) == True:
		return caso
	else:
		numFinal='9'
		nuevoNum=(caso+9-(caso)%10-10)/10
		while nuevoNum >= 10:
			if numOrdenado (nuevoNum)== True:
				return str(nuevoNum)+numFinal
			else:
				numFinal+='9'
				nuevoNum=(nuevoNum+9-(nuevoNum)%10-10)/10
		if nuevoNum==0:
			return numFinal
		else:
			return str(nuevoNum)+numFinal
		
		
		

	
for i, item in enumerate(lista):
	print "Case #{}: {}".format(i+1, funcion (item))




