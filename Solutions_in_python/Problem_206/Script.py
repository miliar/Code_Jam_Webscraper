
def executer_calcul(entrees):
	D=entrees[0]
	N=entrees[1]
	K=entrees[2]
	S=entrees[3]
	Case=entrees[4]
	H=0.0
	for i in range(N):
		H=max(H,(D-K[i])/S[i])
	return str(D/H)


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
		D,N=map(int,input[current_line].split(' '))
		current_line+=1
		K=[0]*N
		S=[0]*N
		for i in range(N):
			k,s=map(int,input[current_line].split(' '))
			K[i]=k
			S[i]=s
			current_line+=1
		entrees.append([D,N,K,S,Case])
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



