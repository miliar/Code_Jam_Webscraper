#!/usr/bin/python

f = open('A-small-attempt1.in')
#f = open('freecell-input.in')
inputline = f.readline()
numcase = int(inputline)

fout = open('freecell_small_result.txt', 'w')

poss_pct = []
masterlist = []
def calc_poss_pct(max):
	global poss_pct
	poss_pct = []
	#print "calc max=",max
	for i in range (1,max+1):
		for j in range(1,i+1):
			cand = (j/float(i)) * 100
			#print "  cand=",str(cand)," i=",i," j=",j
			if (cand % 1 == 0):
				if cand not in poss_pct:
					poss_pct.append(int(cand))
	#return poss_pct

masterlist.append([])
for i in range (1,11):
	#global masterlist, poss_pct
	calc_poss_pct(i)
	masterlist.append(poss_pct)

#for i in range (1,11):
#	print "master[",i,"]:"
#	for j in range(0, len(masterlist[i])):
#		print " ",masterlist[i][j],
#	print ""

for i in range (0,numcase):
	line = f.readline()
	linelist = line.split()
	n = int(linelist[0])
	pd = int(linelist[1])
	pg = int(linelist[2])
	#print " size masterlist=",len(masterlist)
	if (pd < 100) and (pg == 100):
		truth = False
	elif (pd > 0) and (pg == 0):
		truth = False
	else:
		if pd == 0:
			truth = True
		elif pd in masterlist[n]:
			truth = True
		else: 
			truth = False

	if truth:
		answer = "Case #"+str(i+1)+": Possible"	
	else:
		answer = "Case #"+str(i+1)+": Broken"
	#print answer
	#print "Case #",i+1,": ",totalmove
	fout.write(answer)
	fout.write('\n')
