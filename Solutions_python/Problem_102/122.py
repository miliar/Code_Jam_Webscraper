def eval(L,i,T):	
	return sum([max(T-L[k],0) if k!= i else 0 for k in xrange(len(L))])

def find_answer(L, i, M,X):
	A = 0.0
	B = float(M)
	x = (B+A)/2.0
	fli = float(L[i])
	while(B-A > 1e-9):		
		fx = eval(L, i, fli+X*x)		
		if(fx>=X*(1-x)): 	# will definitely not be eliminated with this many votes
			B = x   		# so try things out with fewer votes
		else:				# can be eliminated with this many votes
			A = x   		# so try things out with more votes
		x = (B+A)/2.0
	
	x = float(round(x*1e8))/1e8
	return 100*x

def solve(L):	
	N = len(L)
	Lout = [0 for i in xrange(N)]
	X = sum(L)
		
	#first sort L
	Ls = sorted(L)
	ind = sorted(range(N), key = lambda x: L[x])
	
	#now step through Ls and place the answer at ind[i] in Lout
	Lout[ind[0]] = find_answer(Ls, 0, 1,X)
	for i in xrange(1,N):
		Lout[ind[i]] = find_answer(Ls, i, Lout[ind[i-1]],X)
		
	return Lout
	

def slst(lst):
	s = str(lst[0])
	for i in lst[1:]:
		s += ' ' + str(i)
	s += '\n'
	return s
	
def init():
	#Get inputs and apply algorithms
	fin = open('A-large.in', 'r')
	L = [map(int, x.strip().split()) for x in fin.readlines()]
	fin.close()
	
	T = L[0][0]
	
	OL = []			
	for i in xrange(1,T+1):
		OL.append('Case #' + str(i) + ': ' + slst(solve(L[i][1:])))
		
	fout = open('A-large.out', 'w')
	fout.writelines(OL)
	fout.close()
	
init()	
