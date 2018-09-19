import bisect

def chooseFromRemaining(sortedKen, naomisblock) :
	a = bisect.bisect(sortedKen, naomisblock)
	if a < len(sortedKen):
		return sortedKen.pop(a)
	else :
		return sortedKen.pop(0)
	# print a
	# return a

def playWar(naomi, ken) :
	sortedKen = sorted(ken)
	naomiscore = 0
	for naomisblock in naomi :
		kensblock = chooseFromRemaining(sortedKen, naomisblock)
		if kensblock < naomisblock :
			naomiscore = naomiscore + 1
	return naomiscore

def playDeceitful(naomi, ken) :
	sortedNaomi = sorted(naomi, reverse=True)
	sortedKen = sorted(ken, reverse=True)
	naomisScore = 0
	while(len(sortedKen) != 0) :
		sizeOfArray = len(sortedKen)
		if sortedKen[0] > sortedNaomi[0]:
			#naomi abandons her smallest asset
			sortedNaomi.pop(sizeOfArray - 1)
			sortedKen.pop(0)
		else :
			# Naomi wins
			sortedKen.pop(0)
			sortedNaomi.pop(0)
			naomisScore = naomisScore + 1
	return naomisScore

	
outputfile = open("output.txt", "w")


f = open("D-large.in")
lines =  [x.strip("\n") for x in f.readlines()]
testCases = int(lines[0])
for i in xrange(testCases) :
	test = lines[i*3+1:i*3+4]
	blocksnumber = int(test[0])
	naomis = [float(x) for x in test[1].split(" ")]
	kens = [float(x) for x in test[2].split(" ")]
	# print naomis
	# print kens
	# print playWar(naomis, kens)

	outputline = "Case #{0}: {1} {2}".format(i+1, playDeceitful(naomis, kens), playWar(naomis, kens))
	outputfile.write(outputline + "\n")

print playDeceitful([0.1,0.2,0.5], [0.15,0.4,0.6])

	
