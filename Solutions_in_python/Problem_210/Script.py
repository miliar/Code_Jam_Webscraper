
def executer_calcul(entrees):
	Ac=entrees[0]
	Aj=entrees[1]
	C=entrees[2]
	D=entrees[3]
	J=entrees[4]
	K=entrees[5]
	Case=entrees[6]
	C.sort()
	D.sort()
	J.sort()
	K.sort()
	A=[] # Durée des temps libres communs à C et J entre deux activités d'un des parents
	B=[] # Durée des temps libres communs à C et J entre deux activités de deux parents différents
	Tc=0 # Durée d'occupation de C
	Tj=0 # Durée d'occupation de J
	if(Ac==0 and Aj==0): return str(2)
	if(Aj==0 or (Ac>0 and D[Ac-1]>=K[Aj-1])):
		last_care='C'
		last_end=D[Ac-1]-1440
	elif(Ac==0 or (Aj>0 and D[Ac-1]<=K[Aj-1])):
		last_care='J'
		last_end=K[Aj-1]-1440
	accu=0 # Nombre de changements déjà réalisés
	i=0 # Boucle activités C
	j=0 # Boucle activités J
	while(i<Ac or j<Aj):
		if(j==Aj or (i<Ac and C[i]<J[j])):
			if(last_care=='C'):
				A.append(C[i]-last_end)
				Tc+=D[i]-last_end
				last_end=D[i]
			elif(last_care=='J'):
				accu+=1
				B.append(C[i]-last_end)
				last_end=D[i]
				last_care='C'
				Tc+=D[i]-C[i]
			i+=1
		elif(i==Ac or (j<Aj and C[i]>J[j])):
			if(last_care=='J'):
				A.append(J[j]-last_end)
				Tj+=K[j]-last_end
				last_end=K[j]
			elif(last_care=='C'):
				accu+=1
				B.append(J[j]-last_end)
				last_end=K[j]
				last_care='J'
				Tj+=K[j]-J[j]
			j+=1
		else: print('Erreur3')
	A.sort()
	B.sort()
	A.reverse()
	B.reverse()
	sum_B=0
	for k in range(len(B)):
		sum_B+=B[k]
	if(Tc+Tj+sum_B!=1440): print('Erreur'+' '+str(Case)+' '+str(Tc)+' '+str(Tj)+' '+str(sum_B))
	if(Tc<=720 and Tj<=720): return str(accu)
	T=max(Tc,Tj)
	k=0
	while(k<len(A)):
		T=T-A[k]
		accu+=2
		if(T<=720): return str(accu)
		k+=1
	print('Erreur2'+' '+str(Case))
	return str(accu)


# Main : lecture du fichier input, appel à la fonction executer_calcul et impression des résultats dans un fichier output
multiprocessed=False # Décide si l'on parallélise les calculs pour gagner du temps
if (multiprocessed): from multiprocessing import Pool
if ((not multiprocessed) or __name__ == '__main__'):
	# Lecture du fichier input
	with open("Input.txt", "r") as input_file:
		input=input_file.readlines()
	# Exploitation du fichier ainsi enregistré
	T=int(input[0])
	current_line=1
	entrees=[]
	Case=1
	while(current_line<len(input)):
		Ac,Aj=map(int,input[current_line].split(' '))
		current_line+=1
		C=[0]*Ac
		D=[0]*Ac
		J=[0]*Aj
		K=[0]*Aj
		for i in range(Ac):
			C[i],D[i]=map(int,input[current_line].split(' '))
			current_line+=1
		for i in range(Aj):
			J[i],K[i]=map(int,input[current_line].split(' '))
			current_line+=1
		entrees.append([Ac,Aj,C,D,J,K,Case])
		Case=Case+1
	# Exécution des calculs
	results=['']*len(entrees)
	if (not multiprocessed):
		for case in range(len(entrees)):
			results[case]=executer_calcul(entrees[case])
	else:
		pool=Pool() # Décide du nombre de processus à faire tourner en parallèle
		results=pool.map(executer_calcul,entrees)
	# Impression des résultats dans un fichier de sortie
	with open('Output.txt','w') as output:
		for case in range(len(entrees)):
			output.write('Case #'+str(case+1)+': '+results[case]+'\n')



