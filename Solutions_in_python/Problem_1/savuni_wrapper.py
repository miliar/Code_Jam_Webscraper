#!/usr/bin/python
# intento de resolver el problema A de la ronda de clasificacion
#**********************
# SECTOR DE FUNCIONES
#**********************


 
#
#funcion que remueve el elemento 'element' de la lista 'listum' si esta en ella
#

def remove_if_in_list(element,listum):
	try:
		listum.remove(element)
	except ValueError, name:
		#print "No se pudo eliminar el elemento pues no estaba en la lista!! Pero no pasa nada xD"
		a=0


#
# funcion que devuelve la cantidad de switchs que hay q hacer
#
#IDEA:
#
#
#backupeo lista de buscadores
#recorro la lista de queries tachando de la lista de buscadores los que aparecen
#cuando se acaba la lista de buscadores, sumo 1 y restituyo la lista de buscadores
#eso hasta que llego al final de la lista de queries
#
def count_switches(lista_de_buscadores,lista_de_queries):
	cuenta=0
	bkp_buscadores=lista_de_buscadores[:]
	#print bkp_buscadores
	#print lista_de_queries
	for i in lista_de_queries:
		
		if (len(lista_de_buscadores)==1):
			if(lista_de_buscadores[0]==i):
				lista_de_buscadores=bkp_buscadores[:]
				#print bkp_buscadores
				cuenta+=1
				#print "cuenta actualizada a ", cuenta
		#print i
		remove_if_in_list(i,lista_de_buscadores)
		#print bkp_buscadores
			
	return cuenta


#******************************
# SECTOR DE CODIGO DE PROGRAMA
#******************************


file=open('./A-large.in','r')
#you can change the name to get the input from other file
# I'm sorry for my bad programming, I'm new to python :D
#and comments are in english and spanish because I'm from argentina




N=file.readline().strip('\n')
#print N

acumulador_rta=''
for i in xrange(0,int(N)):
	S=file.readline().strip('\n')
	#print S
	lista_de_buscadores=[]
	for j in xrange(0,int(S)):
		lista_de_buscadores.append(file.readline().strip('\n'))
	
	#print "He aqui la lista de buscadores del caso", i, " : ", lista_de_buscadores
	Q=file.readline().strip('\n')
	#print Q
	lista_de_queries=[]
	for j in xrange(0,int(Q)):
		lista_de_queries.append(file.readline().strip('\n'))
	#print "He aqui la lista de queries del caso", i, " : ", lista_de_queries
	rta=count_switches(lista_de_buscadores,lista_de_queries)
	acumulador_rta=acumulador_rta +'Case #'+str(i+1)+': '+ str(rta) +'\n'
	

file.close()

file_dest=open('./A-large.out','w')
file_dest.write(acumulador_rta)

file_dest.close()