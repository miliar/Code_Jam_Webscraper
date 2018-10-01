# alien

import sys;

arg = sys.stdin.readline()
args = arg.split(" "); # L D N
L = int(args[0])
D = int(args[1])
N = int(args[2])


def findLimited(index, letter, pos):
	#print "index = " + str(index) + ", letter = " + str(letter) +", pos= " + str(pos) 
	result = []
	for i in pos:
		if arrays[index][i] == letter:
			result.append(i)
	
	return result

arrays = []
for i in range(0,L): arrays.append([])

for i in range(0, D ): # loop until D
	txt = sys.stdin.readline() 
	# untuk tiap huruf
	for j in range(0, L): arrays[j].append( txt[j] )

#print arrays


for i in range(0, N):
	txt = sys.stdin.readline() 
	
	index = 0
	counter=0
	rightpos = range(0, D)
	#print rightpos
	
	j = 0
	while j < len(txt) and index < L:
		if txt[j] == '(': 
			j+=1
			newpos = findLimited(index, txt[j], rightpos)
			#print rightpos
			j+=1
			while txt[j] != ')':
				newpos += findLimited(index, txt[j], rightpos)
				j+=1
				#print rightpos
			
			rightpos = newpos
		elif txt[j] == ')': pass
		else:
			rightpos = findLimited(index, txt[j], rightpos)
		
		j += 1
		index += 1
		
		
	
				
	print "Case #%d: %d" % (i+1, len(rightpos))

	

