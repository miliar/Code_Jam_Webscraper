# -*-coding:Utf-8 -*

import sys

# Parse args
with open("B-large.in") as f:
	arg = f.readlines()

T = int(arg[0])
C = [0 for x in range(T)]
F = [0 for x in range(T)]
X = [0 for x in range(T)]
for ct in range(0, T):
	string = arg[1+ct].split()
	C[ct] = float(string[0])
	F[ct] = float(string[1])
	X[ct] = float(string[2])
	
f = open('B-large.out','w')

# Compute each case
for ct in range(T):
	# Print data in memory
	#print "C : " + str(C[ct]) + ", F : " + str(F[ct]) + ", X : "  + str(X[ct])
	
	elapsedTime = 0
	bestTime = X[ct] / 2
	farm = 0
	while(bestTime > elapsedTime):
		elapsedTime += C[ct] / (2 + farm*F[ct])
		farm += 1
		timeToEndWithConstantFarm = (X[ct] / (2 + farm * F[ct]))
		if(elapsedTime + timeToEndWithConstantFarm < bestTime):
			bestTime = elapsedTime + timeToEndWithConstantFarm

	f.write ("Case #" + str(ct+1) + ": " + str(round(bestTime, 7)) + "\n")
