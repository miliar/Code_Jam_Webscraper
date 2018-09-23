def is_tidy(N):
	
	for i in range(1,len(N)):
		if N[i-1] > N[i]:
			#print "N at i: "+str(N[i])
			#print "N at i-1: "+str(N[i-1])
			return i
		
		
	return -1	

def make_tidy(N):
	
	start = is_tidy(N) 

	#print "N "+str(N)+" start "+str(start)
	# N is already tidy
	if start == -1:
		Nstr =""
		for i in range(len(N)):
			Nstr = Nstr+str(N[i])
		return int(Nstr)
		
	
	# integer is not tidy, at pos N
	
	for i in range(start, 0, -1):
		#print N[i]
		if N[i-1] <= N[i]:
			break
		N[i] = 9
		N[i-1]=N[i-1] - 1		

	
	for i in range(start+1, len(N)):
		N[i] = 9
	Nstr =""
	for i in range(len(N)):
		Nstr = Nstr+str(N[i])
	return int(Nstr)
	

numcase = int(raw_input())
#for i in [1]:
for j in range(numcase):
	N = raw_input()
	
	#N = "1110"#
	#N = "122000"#"111111111111111110"#"654321"#"321234" #int(case)
	ans = 0
	if len(N) == 1:
		ans = N	
		
	else:
		N_L = []
		for i in range(len(N)):
			N_L .append(int(N[i]))
		#print "N_L"+str(N_L)
		#print "N is "+str(N)
		ans = make_tidy(N_L)

	print "Case #"+str(j+1)+": "+str(ans)
