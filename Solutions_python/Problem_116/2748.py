#! /usr/bin/env python

import sys;



def DetermineOutcome(GameString):
	for row in GameString:
		if (sum(row) >= 300.5):
			return 100;
		elif(sum(row) <= -299.5):
			return 1;
	for i in range(len(GameString)):
		total = sum([row[i] for row in GameString])
		if (total >= 300.5):
			return 100;
		elif(total <= -299.5):
			return 1
	diagonal_left = 0
	diagonal_right = 0
	for i in range(len(GameString)):
		diagonal_left = diagonal_left + GameString[i][i];
		diagonal_right = diagonal_right + GameString[i][3-i];
	if (diagonal_left >= 300.5):
		return 100
	elif (diagonal_left <= -299.5):
		return 1
	
	if (diagonal_right >= 300.5):
		return 100 
	elif (diagonal_right <= -299.5):
		return 1 

	return 0



def ProcessGameString(GameString):

	for i in range(len(GameString)):
		for j in range(len(GameString[i])):
			if (GameString[i][j] == 'X'):
				GameString[i][j] = 100
			elif(GameString[i][j] == 'O'):
				GameString[i][j] = -100
			elif(GameString[i][j] == '.'):
				GameString[i][j] = 0;
			elif(GameString[i][j] == 'T'):
				GameString[i][j] = 0.5;
			else:
				print "Invalid input: %s" % GameString[i][j]
		




#read file
f = open(sys.argv[1], "r")
k = open("output", "w")
NumOfTest = f.readline()

emptyFlag = 0
GameString = []
caseNum = 1
for line in f:
	
	line = line.strip()
	if line == "":
		continue
	if '.' in line:
		emptyFlag = 1
	row = [x for x in line]
	GameString.append(row)
	if len(GameString) == 4:
		ProcessGameString(GameString)
		outcome = DetermineOutcome(GameString)
		if (outcome == 100):
			k.write("Case #%d: X won\n" % caseNum);
		elif(outcome == 1):
			k.write( "Case #%d: O won\n" % caseNum);
		elif (outcome == 0 and emptyFlag == 1):
			k.write("Case #%d: Game has not completed\n" % caseNum);
		else:
			k.write("Case #%d: Draw\n" % caseNum ); 
		GameString = []
		emptyFlag = 0
		caseNum = caseNum + 1
 


