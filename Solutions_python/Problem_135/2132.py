#magictrick

import math
import random

fin = open("magictrick.in","r")
fout = open("magictrick.out","w")

N = int(fin.readline())

for i in range(N):
	ans1 = int(fin.readline())
	cards1 = []
	for j in range(4):
		#cards themselves are strings, not ints
		cards1.append(fin.readline().split())
	ans2 = int(fin.readline())
	cards2 = []
	for j in range(4):
		cards2.append(fin.readline().split())
	
	row1 = cards1[ans1 - 1]
	row2 = cards2[ans2 - 1]
	
	possibs = []
	for j in range(4):
		for k in range(4):
			if row1[j] == row2[k] and row1[j] not in possibs:
				possibs.append(row1[j])
	
	#print(row1)
	#print(row2)
	
	output = ""
	if len(possibs) == 0:
		output = "Volunteer cheated!"
	elif len(possibs) == 1:
		output = possibs[0]
	else:
		output = "Bad magician!"
		#fout.write(possibs[0] + " " + possibs[1])
	
	fout.write("Case #" + str(i + 1) + ": " + output + "\n")
	
fin.close()
	
	
