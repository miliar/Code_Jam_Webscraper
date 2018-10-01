"""Solution : 


"""
import numpy as np

def solve(naomi, ken):
	size = len(naomi)
	
	# Normal war
	copyken = ken[:]
	copynaomi = naomi[:]
	sortnaomi = reversed(sorted(naomi))

	for n in sortnaomi: # Ken play optimally according to his game
		if max(ken) > n:
			naomi.pop(naomi.index(n))
			ken.pop(ken.index(max(ken)))
	# print "result", len(naomi),
	pointwar = len(naomi)


	# Deceitful War
	naomi = copynaomi
	ken = copyken
	sortken = reversed(sorted(ken))

	for k in sortken:
		if max(naomi) > k:
			naomi.pop(naomi.index(max(naomi)))
			ken.pop(ken.index(k))
	# print "result", size - len(naomi)
	pointdeceitfulwar = size - len(naomi)

	points = str(pointdeceitfulwar) +" "+ str(pointwar)
	return points


fr = open('D-large.in', 'r')
fw = open('output.txt', 'w+')
numcases = int(fr.readline())
idline = 0

for x in xrange(1,numcases+1):
	idline += 1
	inputsize = int(fr.readline())
	inputnaomi = fr.readline().replace('\n', '').split(' ')
	inputken = fr.readline().replace('\n', '').split(' ')
	floatnaomi = [float(i) for i in inputnaomi]
	floatken = [float(i) for i in inputken]

	time = solve(floatnaomi, floatken)
	fw.write("Case #"+str(idline)+": "+str(time)+'\n')


def test():
	solve([0.5],[0.6])
	solve([0.7, 0.2],[0.8, 0.3])
	solve([0.5, 0.1, 0.9],[0.6, 0.4, 0.3])
	solve([0.186, 0.389, 0.907, 0.832, 0.959, 0.557, 0.300, 0.992, 0.899], [0.916, 0.728, 0.271, 0.520, 0.700, 0.521, 0.215, 0.341, 0.458])
# test()