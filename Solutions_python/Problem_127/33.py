from math import *;
INPUT_NAME = 'B-small-attempt0.in'
OUTPUT_NAME = 'B-small_0.out'
#INPUT_NAME = 'B-large.in'
#OUTPUT_NAME = 'B-large.out'
#INPUT_NAME = 'B.in'
#OUTPUT_NAME = 'B.out'
	
def solve(X,Y):
	# first do EW steps to get to X
	if(X<0):
		s = 'EW'*(-X)
	else:
		s = 'WE'*X
		
	# now do NS steps to get to Y
	if(Y<0):
		s += 'NS'*(-Y)
	else:
		s += 'SN'*Y
	return s
	
# THIS IS THE "MAIN" FUNCTION
def fullsol(slst):
	T = int(slst[0]) # number of test cases
	cur = 1
	answers = [];
	for i in xrange(T):
		(X,Y) = map(int, slst[cur].split())
		cur += 1
		answers.append(solve(X,Y))
		
	return answers
#############################
	
	
def makestring(row):
	# make a list into a string separated by spaces
	return ''.join([' '+str(i) for i in row])[1:]

def olwrite(fname, answers):
	# write outputs to file line by line [one-line outputs]
	f = open(fname, 'w')
	lines = ['Case #'+str(i+1)+': '+answers[i]+'\n' for i in xrange(len(answers))]
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


	