'''
Created on May 8, 2010

@author: qfel13
'''

if __name__ == '__main__':
	sol = {}
	step = {}
	for i in xrange(1, 31):
		sol[i] = 0
		step[i] = 2**i
		for j in xrange(i):
			sol[i] += 2**j
	
	f = open("A-large.in", "r")
	fout = open("A-large.out", "w")
	caseCount = int(f.readline())
	for case in xrange(caseCount):
		a = f.readline().split(" ", 1)
		n = int (a[0])
		k = int (a[1])
		
		fout.write("Case #" + str(case + 1) + ": ")
		if (k%step[n]) == sol[n]:
			fout.write("ON\n")
		else:
			fout.write("OFF\n")