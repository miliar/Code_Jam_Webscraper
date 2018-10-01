#!/usr/bin/env python
import sys
infile = sys.argv[1]
#outfile = sys.argv[2]

indata = open(infile, 'r').readlines()
#print indata

numcases = int(indata[0].strip())
lines = [x.strip() for x in indata[1:]]

for j in range(0, numcases):
	numteams = int(lines[0])
	windata = lines[1:numteams+1]
	assert(numteams == len(windata))
	lines = lines[numteams+1:]

	gameswon = dict()
	gamesplayed = dict()
	WP = dict()
	OWP = list()
	OOWP = dict()

	for i in range(0, numteams):
		gameswon[i] = len(filter(lambda x: x=='1', windata[i]))
		gamesplayed[i] = len(filter(lambda x: x!='.', windata[i]))
		WP[i] = float(gameswon[i]) / gamesplayed[i]
	for i in range(0, numteams):
		x = float(0)
		for k in range(0, numteams):
			if k != i and windata[i][k] != '.':
				tmp = x
				if windata[k][i] == '.':
					assert False
				elif windata[k][i] == '1':
					x += float(gameswon[k] - 1) / (gamesplayed[k] - 1)
				elif windata[k][i] == '0':
					x += float(gameswon[k]) / (gamesplayed[k] - 1)
				else:
					assert False
				#print k, x-tmp
		#print x
		OWP.append(x/(gamesplayed[i]))
	for i in range(0, numteams):
		x = float(0)
		for k in range(0, numteams):
			if k != i and windata[i][k] != '.':
				x += OWP[k]
		OOWP[i] = x/(gamesplayed[i])

	#print WP
	#print OWP
	#print OOWP

	print "Case #" + str(j+1) + ":"
	for i in range(0, numteams):
		 print str(0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i])
