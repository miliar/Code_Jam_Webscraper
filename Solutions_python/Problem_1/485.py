#!/usr/bin/python

def encontrar_primero (engines, queries):
	cont = 0
	for x in queries:
		if len(engines)  == 1:
			if engines[0] == x:
				#print "el buenas",engines,cont
				return engines[0],cont
		#print engines, x, cont
		try:
			if len(engines) != 1:
				engines.remove(x)
		except:
			pass
		cont = cont + 1
	#print "recorrio todo", engines[0], cont
	return engines[0],cont

def total_camino(engines,queries):
	index = 0
	index_swp = 0
	cont = 0
	while True:
		#print "con queries",index,queries[index:],engines
		engines_copy = engines[:]	
		engine,index_swp = encontrar_primero (engines_copy, queries[index:])
		index = index + index_swp
		if len(queries[index:]) < 1:
			#print  "el total es uno:", cont
			break
		cont = cont + 1
	return cont



f = open('A-large.out', 'w+')
in_f = open('A-large.in', 'r+')
cont = 0
engines = []
queries = []
voy = 0
cont_line = 0
case = 1
for line in in_f.readlines()[1:]:
	casi_final = 0
	cont_line = cont_line + 1
	try:
		cont_max = int(line)
		voy = voy + 1
		cont = 0
	except ValueError:
		if voy == 1:
			engines.append(line[:-1])
		if voy == 2:
			queries.append(line[:-1])
			cont = cont + 1
	if cont == cont_max:
		voy = 0
		#print engines,queries
		casi_final = total_camino(engines,queries)
		#print "casi_final:", casi_final
		print "Case #%d: %d" %(case, casi_final)
		case = case + 1
		#print "linea que sigue", cont_line
		engines = []
		queries = []	
	
