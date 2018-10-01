#!/bin/python

iterations = raw_input() 

for iteration in range(int(iterations)) :
	answer = raw_input()
	cards = []
	for line in xrange(0, 4 ) :
		line_text = raw_input()
		cards.append(line_text.split(" "))
	possible_1 = cards[int(answer)-1]
	#print possible_1
	answer = raw_input()
	cards = []
	for line in xrange(0, 4 ) :
		line_text = raw_input()
		cards.append(line_text.split(" "))
	possible_2 = cards[int(answer)-1]
	#print possible_2

	choices = []
	for value in possible_1 :
		if value in possible_2 :
			choices.append(value)

			

	
	
	
	print "Case #%s:" % str(int(iteration+1)),
	if len(choices) == 1 : print choices[-1]
	elif len(choices) == 0 : print r'Volunteer cheated!'
	else : print r'Bad magician!'
	#print filesystem
	#print mkdirs
