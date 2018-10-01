from sys import stdin, stdout
cin=open("in")
cout=open("out","w")
n_cases=int(cin.readline().rstrip())
n=0
m=0
comb=["X"]
liked_by={}
#sol_found=False

min_malted=1000
best_sol=None

def recur(next):
	global comb, i, sol_found, liked_by, min_malted, best_sol
	comb.append(next)
	if len(comb)==n+1:
		#complete combination
		satisfied=set()	
		for i in xrange(1,n+1):
			key=(i,comb[i])
			if key in liked_by:
				satisfied=satisfied.union(liked_by[key])
		#print comb, "***", satisfied
		if satisfied==set(range(1,m+1)):
			n_malted=sum(comb[1:])
			if n_malted<min_malted:
				min_malted=n_malted
				best_sol=list(comb)
	else:
		recur(1)
		recur(0)
	del comb[-1]


for case_i in xrange(1,n_cases+1):
	n=int(cin.readline().rstrip())
	m=int(cin.readline().rstrip())
	liked_by={}
	#input
	for i in xrange(1,m+1):
		likes_raw=map(int, cin.readline().split(" "))[1:]
		for j in xrange(len(likes_raw)/2):
			tmp=(likes_raw[2*j], likes_raw[2*j+1])
			if tmp in liked_by:
				liked_by[tmp].add(i)
			else:
				liked_by[tmp]=set([i])
	#all combinations
	#print liked_by, "+++"
	comb=["X"]
	sol_found=False
	min_malted=1000
	best_sol=None
	recur(1)
	recur(0)

	cout.write("Case #"+str(case_i)+": ")
	if best_sol!=None:
		cout.write(" ".join(map(str, best_sol[1:])))
	else:
		cout.write("IMPOSSIBLE")	
	cout.write("\n")


		
		
		

