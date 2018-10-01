z = 1
Z = raw_input("")
Z = int(Z);

def nwd(a,b):
	if b == 0:
		return a
	else:
		return nwd(b,a%b)

while z <= Z:
	tab = raw_input("").split()
	a = 0
	for i in tab:
		tab[a] = int(i)
		a += 1
	n = tab[0]
	tab[0] = int(0)
	m = int(0)
	for i in tab:
		for j in tab:
			if i != j and i != 0 and j != 0:
				m = nwd(m, abs(i-j))
	print "Case #"+str(z)+": "+str((m-(tab[1]%m))%m)
	z += 1

