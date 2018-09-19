
def buscarLetra(completados, secuencia, letra):
	try:
		a = [x[0] for x in secuencia].index(letra, completados)
		return secuencia[a][1]
	except ValueError:
		return -1

entrada = file('A-large.in')
salida = file('output-fixed-large.ou', 'w')
casos = int(entrada.readline())

for i in range(casos):
	
	temp = entrada.readline().split()
	secuencia = []
	for j in xrange(1, len(temp)-1, 2):
		secuencia.append((temp[j], int(temp[j+1])))
	
	#print secuencia
	
	#print orangePath, bluePath
		
	oActual = 1
	bActual = 1
	
	completados = 0
	movimientos = 0
	
	while (completados < len(secuencia)):
		if (secuencia[completados][0] == 'O'):
			saltos = secuencia[completados][1] - oActual
			oActual += saltos
			saltos = abs(saltos) + 1
			completados += 1
			if completados == len(secuencia):
				movimientos += saltos
				break
			
			#sigBlue = siguienteAzul(bluePath, blueFound+1)
			sigBlue = buscarLetra(completados, secuencia, 'B')
			if sigBlue != -1:
				if bActual < sigBlue:
					if bActual+saltos >= sigBlue:
						bActual = sigBlue
					else:
						bActual += saltos
				elif bActual > sigBlue:
					if bActual-saltos <= sigBlue:
						bActual = sigBlue
					else:
						bActual -= saltos
		else:
			saltos = secuencia[completados][1] - bActual
			bActual += saltos
			saltos = abs(saltos) + 1
			completados += 1
			if completados == len(secuencia):
				movimientos += saltos
				break
			
			sigOrange = buscarLetra(completados, secuencia, 'O')
			if sigOrange != -1:
				if oActual < sigOrange:
					if oActual+saltos >= sigOrange:
						oActual = sigOrange
					else:
						oActual += saltos
				elif oActual > sigOrange:
					if oActual-saltos <= sigOrange:
						oActual = sigOrange
					else:
						oActual -= saltos
		movimientos += saltos
					
	
	salida.write('Case #%d: %d\n' % ((i+1), (movimientos)))
	
entrada.close()
salida.close()
