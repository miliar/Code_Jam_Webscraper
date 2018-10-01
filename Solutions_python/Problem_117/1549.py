def sepuede(N,M,cuadro,it):	
	i=0	
	while i<N:
		j=0
		while j<M:
			puedefila=True
			puedecolumna=True
			valor=int(cuadro[i][j])
			#if it==7 and i==3 and j==8: 
			#	print i,j
			#	print cuadro			
			k=0			
			while k<M:		
				if int(cuadro[i][k])>valor:
					puedefila=False				
				k=k+1
			if not puedefila:			
				k=0			
				while k<N:
					if int(cuadro[k][j])>valor:
						puedecolumna=False				
					k=k+1
			if not(puedefila or puedecolumna):
				return False
			j=j+1	
		i=i+1
	return True



def sepuede2(N,M,cuadro):	
	i=0	
	while i<N:
		j=0
		while j<M:
			puedefila=True
			puedecolumna=True
			valor=int(cuadro[i][j])
			if valor==1:
				k=0			
				while k<M:		
					if int(cuadro[i][k])!=valor:
						puedefila=False				
					k=k+1
				if not puedefila:			
					k=0			
					while k<N:
						if int(cuadro[k][j])!=valor:
							puedecolumna=False				
						k=k+1
			if not(puedefila or puedecolumna):
				return False
			j=j+1	
		i=i+1
	return True



import sys
import math

if(len(sys.argv) > 1):
	fichero = sys.argv[1]
else: 
	print "Debes indicar el nombre del archivo"

f = open(fichero, "r")
casos=int(f.readline())
i=1
while i<=casos:

	fila1=f.readline()
	datos=fila1.split(' ')
	N=int(datos[0])
	M=int(datos[-1])		
	
	v=[]
	j=1
	while j<=N:
		fila2=f.readline()
		if fila2[-1]=='\n': 
			fila2=fila2[0:-1]
		datosfila=fila2.split(' ')
		v.append(datosfila)		
		j=j+1
	if sepuede2(N,M,v):	
		print "Case #%s: YES" % i
	else:
		print "Case #%s: NO" % i
	i=i+1
