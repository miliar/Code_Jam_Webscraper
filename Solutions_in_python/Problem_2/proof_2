import string
import re
import sys
import pdb


input = open(sys.argv[1])
input_data = input.readline()
input_data=re.sub("\n","",input_data)

def compare(x,y):
	if x[0][0]>y[0][0]:
		return 1
	elif x[0][0]==y[0][0]:
		return 0
	else:
		return -1


def rutas_a(s, a, b, t):
	for i in range(len(b)):
		if (s+t) <= b[i][0][0]:
			return b[i]
	return -1
def rutas_b(s,a,b,t):
	for i in range(len(a)):
		if (s+t) <= a[i][0][0]:
			return a[i]
	return -1



for i in range(0,int(input_data)):
	numero_re = input.readline()
	numero_re = re.sub("\n","",numero_re)
	t_re = int(numero_re)
	numero_are = input.readline()
	numero_abre = numero_are.split()
	a_tx = int(numero_abre[0])
	b_tx = int(numero_abre[1])
	if (a_tx == 0) | (b_tx == 0):
		print('Case #'+str(i+1)+': '+str(a_tx)+' '+str(b_tx))
	else:
		a_dep = range(0,a_tx) 
		b_dep = range(0,b_tx)
		todos = []
		for j in range(0,a_tx):
			temp = input.readline()
			temp = temp.split()
			temp1 = temp[0].split(':')
			temp2 = temp[1].split(':')
			temp3 = 60*int(temp1[0])+int(temp1[1])
			temp4 = 60*int(temp2[0])+int(temp2[1])
			a_dep[j] = [temp3,temp4],0
			todos.append(a_dep[j])
		for j in range(0,b_tx):
			temp = input.readline()
			temp = temp.split()
			temp1 = temp[0].split(':')
			temp2 = temp[1].split(':')
			temp3 = 60*int(temp1[0])+int(temp1[1])
			temp4 = 60*int(temp2[0])+int(temp2[1])
			b_dep[j] = [temp3,temp4],1
			todos.append(b_dep[j])
		a_dep=sorted(a_dep,compare)
		b_dep=sorted(b_dep,compare)
		todos=sorted(todos,compare)
		trenes_a = 0
		trenes_b = 0
		for j in range(len(todos)):
			veri = todos[j]
			if veri[1] == 0:
				try:
					a_dep.remove(veri)
					listo = 0
					trenes_a += 1
					while listo != 1:
						result = rutas_a(veri[0][1],a_dep,b_dep,t_re)
						if result != -1:
							b_dep.remove(result)
							veri = rutas_b(result[0][1],a_dep,b_dep,t_re)
							if veri == -1:
								listo = 1
							else:
								a_dep.remove(veri)
						else:
							listo = 1

				except:
					trenes_a = trenes_a
			else:
				try:
					b_dep.remove(veri)
					listo = 0
					trenes_b += 1
					while listo != 1:
						result = rutas_b(veri[0][1],a_dep,b_dep,t_re)
						if result != -1:
							a_dep.remove(result)
							veri = rutas_a(result[0][1], a_dep, b_dep, t_re)
							if veri == -1:
								listo = 1
							else:
								b_dep.remove(veri)
						else:
							listo = 1
				except:
					trenes_b = trenes_b
		print('Case #'+str(i+1)+': '+str(trenes_a)+' '+str(trenes_b))

