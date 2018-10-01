
def executer_calcul(entrees):
	K=entrees[1]
	Case=entrees[2]
	nb_pancakes=len(entrees[0])
	S=['+']*nb_pancakes
	for i in range(nb_pancakes):
		if (entrees[0][i]=='-'): S[i]='-'
	accu=0
	i=0
	while(i<=nb_pancakes-K):
		if(S[i]=='-'):
			accu+=1
			for j in range(K):
				if(S[i+j]=='+'): S[i+j]='-'
				elif(S[i+j]=='-'): S[i+j]='+'
		i+=1
	while(i<nb_pancakes):
		if(S[i]=='-'): return 'IMPOSSIBLE'
		i+=1
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
		S,K=input[current_line].split(' ')
		K=int(K)
		current_line+=1
		entrees.append([S,K,Case])
		Case=Case+1
	# Exécution des calculs
	results=['']*len(entrees)
	if (not multiprocessed):
		for case in range(len(entrees)):
			results[case]=executer_calcul(entrees[case])
	else:
		pool=Pool(3) # Décide du nombre de processus à faire tourner en parallèle
		results=pool.map(executer_calcul,entrees)
	# Impression des résultats dans un fichier de sortie
	with open('Output.txt','w') as output:
		for case in range(len(entrees)):
			output.write('Case #'+str(case+1)+': '+results[case]+'\n')



