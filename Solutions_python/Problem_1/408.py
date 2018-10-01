INFINITY = 999999
#..........function find the number of switch()..........................
def findSwitchNumber (E,Q):
	NE = len(E)
	NQ = len(Q)
	N = 0
	while NQ != 0:
		List = {}
		for i in range(0,NE):
			if E[i] in Q:
				List[E[i]] = Q.index(E[i])
			else:
				List[E[i]] = INFINITY
		if INFINITY in List.values():
			break
		NQ -= max(List.values())
		N = N + 1
		Q = Q[max(List.values()):]
	return N		

#................................. __main()__ ...............
Input = open("A-large.in")
Output = open ("A-large.out","w")

NoOfCases = int(Input.readline())
print NoOfCases
for i in range(0,NoOfCases):
	
	Engines = []
	x=Input.readline()
	NoOfEngines = int(x)
	for j in range(0,NoOfEngines):
		Engines.append(Input.readline()[:-1])
	
	Queries = []
	x=Input.readline()
	NoOfQueries = int(x)
	for j in range(0,NoOfQueries):
		Queries.append(Input.readline()[:-1])

	NoOfSwitch = findSwitchNumber(Engines,Queries)
	Write = "Case #"+ str(i+1) + ": " + str(NoOfSwitch) + "\n"
	Output.writelines(Write)
	print NoOfSwitch
	
Input.close()
Output.close()
