testCases = input()

aux = []
selected = []

for i in range(testCases):
	answer1 = input()
	arrange1 = []
	for j in range(4):
		card = raw_input() 
		arrange1.append(card)
	
	answer2 = input()
	arrange2 = []
	for j in range(4):
		card = raw_input() 
		arrange2.append(card)
		
	counter = 0
	
	split1 = arrange1[answer1-1].split(" ")
	split2 = arrange2[answer2-1].split(" ")
	
	selected.append('0')
	for j in range(4):
		if split2.count(split1[j]) > 0:
			selected[i] = split1[j]
			counter = counter + 1
			
	aux.append(counter)
			
counter = 1
for i in aux:					
	if i == 0:
		print "Case #" + str(counter) + ": Volunteer cheated!"
	elif i == 1:
		print "Case #" + str(counter) + ": " + selected[counter-1]
	elif i > 1:
		print "Case #" + str(counter) + ": Bad magician!"
	counter = counter + 1
		
						
	
