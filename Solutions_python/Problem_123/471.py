from math import *;
#INPUT_NAME = 'A-large.in'
#OUTPUT_NAME = 'A-large.out'
#INPUT_NAME = 'A-small-attempt1.in'
#OUTPUT_NAME = 'A-small.out'

INPUT_NAME = 'A-large.in'
OUTPUT_NAME = 'A-large.out'
	
def cumsumd(L):
	Lnew = [0]
	diff = [L[0]]
	s = 0
	i = 0
	for elem in L[:-1]:
		i += 1
		s += elem
		Lnew.append(s)
		diff.append(L[i]-s)
		
	return (Lnew,diff)

def solve(A, L):	
	(cs, d) = cumsumd(L)
	moves_to_remove = range(len(L),0,-1)
	moves_to_add = []	
	cur = A	
	for i in xrange(len(L)):
		if(d[i]<cur):
			moves_to_add.append(0)			
		elif 2*cur+cs[i] <= 2:						
			moves_to_add.append(2*moves_to_remove[i])
		else:
			v = (((d[i]-1))//(2*(cur-1)+cs[i]))
			if(v==0):
				n = 1
			else:
				n = 1+v.bit_length()
			
			cur = (2**(n-1))*(2*(cur-1)+cs[i])+1			
			moves_to_add.append(n)			
	
	# compute final cost
	cost = 0	
	for i in xrange(len(moves_to_remove)-1, -1, -1):
		if(cost+moves_to_add[i]<moves_to_remove[i]):
			cost += moves_to_add[i]
		else:
			cost = moves_to_remove[i]			
	
	return cost
	

def fullsol(slst):
	T = int(slst[0]) # number of test cases
	sol = [];
	cur = 1;
	for i in xrange(T):	
		A = int(slst[cur].split()[0])		
		cur += 1
		L = sorted(map(int, slst[cur].split()))
		cur += 1
		sol.append(solve(A, L))
	return sol
	
	
def makestring(row):
	# make a list into a string separated by spaces
	return ''.join([' '+str(i) for i in row])[1:]

def olwrite(fname, answers):
	# write outputs to file line by line [one-line outputs]
	f = open(fname, 'w')
	lines = ['Case #'+str(i+1)+': '+str(answers[i])+'\n' for i in xrange(len(answers))]
	f.writelines(lines)
	f.close()
	return
	
def sread(fname):
	f = open(fname, 'r')
	res = [x.strip() for x in f.readlines()]
	f.close()
	return res
	
stuff = sread(INPUT_NAME)
answers = fullsol(stuff)
olwrite(OUTPUT_NAME, answers)


	