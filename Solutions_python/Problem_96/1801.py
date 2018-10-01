#!/usr/bin/env python
import sys
import fileinput

out = open('Q2Output.o', 'w')

start = 1
T = 0



x=0
listOutputString = []
for line in fileinput.input():
	
	if start == 1:
		T = int(line.replace("\n",""))
		start = 0
	
	elif (not start and line != "\n"):
		usedS = 0
		NumOfBestResults = 0
		N = 0
		S = 0
		P = 0
		Ti = []
		tokens = line.split(" ")
		listOutputString.append("Case #" + str(x+1) + ": ")
		N = tokens[0]
		S = int(tokens[1])
		P = int(tokens[2])
		# in total scores of each player
		for token in tokens[3:]:
			tNum = int(token)
			threshold = tNum/3
			variation = tNum % 3
			# ignore values lower than P
			if threshold < P and (variation + threshold) < P and variation != 0:
			  	pass
			elif P == 0:
				NumOfBestResults = int(N)
				break
			elif P < threshold:
				NumOfBestResults += 1
			elif threshold < P and variation == 0 and (threshold + 1) == P and threshold != 0 and S>usedS:
				NumOfBestResults += 1
				usedS += 1
			elif threshold >= P and S >= usedS and (variation + threshold) > P:
				NumOfBestResults += 1
				if not(threshold+variation>10):
					usedS += 1
			# when remainder is 1 from threshold
			elif threshold + variation >= P and variation == 1:
				NumOfBestResults += 1
			
			elif threshold + variation >= P and variation == 0:
				NumOfBestResults += 1
			elif threshold + variation >= P and S>= usedS:
				if P - threshold == 1 and variation == 1:
					NumOfBestResults += 1
				elif P - threshold == 1 and variation == 2 and S>usedS:
					NumOfBestResults += 1
				elif P - threshold == 1 and variation == 2 and S == 0 and usedS == 0:
					NumOfBestResults += 1
				elif P - threshold == 2 and variation == 2 and S>usedS:
					NumOfBestResults += 1
					usedS += 1
				
				elif P - threshold == 0:
					NumOfBestResults +=1
				# 	NumOfBestResults += 1
				
				# 	if variation != 0:
				# 		usedS += 1
				# 	# pass

		listOutputString[x] += str(NumOfBestResults)
		out.write(listOutputString[x].strip() + "\n")
		x+=1

	
		

# print listOutputString