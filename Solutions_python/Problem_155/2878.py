def getInput() :
	t = int(input())
	tab = []
	for i in range(t) :
		myLigne = input().split()
		myLigne[0] = int(myLigne[0])
		tab.append(myLigne)

	return t, tab

def solve(k, tab) :
	somme = 0
	ajouter = 0

	for j in range(int(tab[0])+1) :
		if somme < j :
			ajouter += j-somme
			somme += j-somme
		somme += int(tab[1][j])

	print("Case #" + str(k+1) + ": " + str(ajouter))

(t, tab) = getInput()
for a in range(t) :
	solve(a, tab[a])