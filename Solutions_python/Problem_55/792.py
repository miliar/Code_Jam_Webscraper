import re

f = open("C-small-attempt0.in","r")
T = int(f.readline())
w = open("C-small-attempt0.out","w+")
for i in range(T):
	fila = []
	R,k,N = map(int,f.readline().split())
	fila = map(int,f.readline().split())
	cash = 0
	for j in range(R):
		car = 0
		fila_aux = []	
		while(car<=k and len(fila) > 0):
			if(fila[0]+car<=k):
				car = car + fila[0]
				cash = cash + fila[0]
				fila_aux.append(fila[0])
				fila.remove(fila[0])
			else:
				break
		fila = fila + fila_aux
	if (i==T-1):
		w.write('Case #%d: %d' % ((i+1),cash))
	else:
		w.write('Case #%d: %d\n' % ((i+1),cash))


f.close()
w.close()