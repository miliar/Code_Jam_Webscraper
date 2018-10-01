import math


def C(a,b,palin):
	inicio = math.floor(math.sqrt(a))
	fin = math.ceil(math.sqrt(b))
	c = 0
	for j in range(inicio,fin+1):
		sj = str(j)
		if sj == sj[::-1]:
			cuad = j*j
			sc = str(cuad)
			if sc == sc[::-1] and cuad >= a and cuad <= b:
				palin.append(cuad)
	return

palindromos = []
C(1,10**14,palindromos)
#for x in palindromos:
#        print(x)
        
T = int(input())
for i in range(1,T+1):
    linea = str(input()).split()
    A = int(linea[0])
    B = int(linea[1])
    c = 0
    for x in palindromos:
        if x >= A:
                if x > B:
                        break
                else:
                        c += 1
    print('Case #',i,': ',c,sep='')







	
