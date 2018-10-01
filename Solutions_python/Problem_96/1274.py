input = open("input.txt")
numProbs = int(input.readline())
probNum=0
for line in input:
	probNum=probNum+1
	output=0
	line = line.split()
	dancers = int(line[0])
	suprises = int(line[1])
	targetScore = int(line[2])
	dancerTotals=[]
	for i in range(3,len(line)):
		dancerTotals.append(int(line[i]))
	#print dancerTotals

	scores=[]
		
	#consider best result without suprises.
	for total in dancerTotals:
		normal = (total/3,total/3,total/3)
		if total % 3 == 1:
			normal = (normal[0]+1,normal[1],normal[2])
		if total % 3 == 2:
			normal = (normal[0]+1,normal[1]+1,normal[2])
		scores.append(normal)
		
	#print scores
	lowScores = []
	#For those who don't make it consider using suprises.
	for score in scores:
		if score[0] >= targetScore:
			output = output+1
		else:
			lowScores.append(score)
			
	#print output
	#print lowScores

	#use suprises carefully on those that can be increased to the critical level
	for score in lowScores:
		if score[0] == targetScore-1 and score[1] == targetScore-1 and score[1] > 0 and suprises > 0:
			output=output+1
			suprises=suprises-1
		
	print "Case #"+str(probNum)+": "+str(output)