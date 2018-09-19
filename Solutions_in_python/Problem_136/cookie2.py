#! /usr/bin/env python3.4
	
def solution(i, C, F, X):
	
	prod = 2.0
	if float(X) < float(C):
		secs = float(X)/prod # Just wait it out
	else: 
		# Make a decision at farm time
		secs = float(C)/prod 
		total = float(C) 
		while True:
			eta1 = (float(X) - total) / float(prod)
			eta2 = (float(X)) / (prod+float(F))
			if eta1 > 0 and eta2 > 0 and eta2 < eta1:
				total += prod * (float(C)/prod) # how much extra it produced between farms
				total -= float(C)
				prod += float(F)
				secs += float(C)/prod
			else:
				secs += eta1
				break
		
	line = 'Case #{0}: {1} \n'.format(i+1, secs)

	return line
	
# Start
outfile = open("output.txt", "w")
file = open("B-large.in")
N = file.readline()
line = ""
for i in range(0, int(N)):
	C, F, X = file.readline().strip().split()
	line += solution(i, C, F, X)
outfile.write(line)

				