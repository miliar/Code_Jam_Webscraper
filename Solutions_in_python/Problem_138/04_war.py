# filename = "04-input-test-0"
# filename = "04-D-small-attempt0"
filename = "04-D-large"
fi = open(filename+'.in', 'r')
lData = list()
debug = True
collect = ""
index = 0
strVal = 0

naomi_blocks = []
ken_blocks = []
cases = []

for line in fi:
	if (index > 0):
		if (index % 3 == 2):
			naomi_blocks = map(float, line.strip().split(' '))
		elif (index % 3 == 0):
			ken_blocks = map(float, line.strip().split(' '))
			cases.append([naomi_blocks, ken_blocks])
		elif (index % 3 == 1):
			naomi_blocks = []
			ken_blocks = []

	index = index + 1

fi.close()
# print cases

# Task
def playDeceitfulWar(case): 
	naomi_blocks = list(case[0])
	ken_blocks = list(case[1])
	naomi_blocks.sort()
	ken_blocks.sort()
	naomi_blocks.reverse()
	ken_blocks.reverse()
	# print "Sorted", naomi_blocks, ken_blocks
	naomi_win = 0
	for iNaomi in range(len(naomi_blocks)):
		ken_found = 0
		# print naomi_blocks[iNaomi], ken_blocks[iNaomi], naomi_blocks[iNaomi] - ken_blocks[iNaomi]
		for iKen in range(len(ken_blocks)):
		# 	# print len(ken_blocks)
			if (naomi_blocks[iNaomi] > ken_blocks[iKen]): #Ken wins
				ken_found = ken_blocks[iKen]
				break
		if (ken_found > 0):
			ken_blocks.remove(ken_found)
			naomi_win = naomi_win + 1
		# else: # Naomi wins
		
			# ken_blocks.remove(ken_blocks[0])

	return naomi_win

def playWar(case): 	
	naomi_blocks = list(case[0])
	ken_blocks = list(case[1])
	naomi_blocks.sort()
	ken_blocks.sort()
	# print "Sorted", naomi_blocks, ken_blocks
	naomi_win = 0
	for iNaomi in range(len(naomi_blocks)):
		ken_found = 0
		for iKen in range(len(ken_blocks)):
			# print len(ken_blocks)
			if (naomi_blocks[iNaomi] < ken_blocks[iKen]): #Ken wins
				ken_found = ken_blocks[iKen]
				break
		if (ken_found > 0):
			ken_blocks.remove(ken_found)
		else: # Naomi wins
			naomi_win = naomi_win + 1
			ken_blocks.remove(ken_blocks[0])

	return naomi_win


index = 1
solution = ""
for case in cases:
	# print "Case", index, case
	# sol_object = processCookies(case)
	# print index, ":::", sol_object
	# if index == 1:
		# print index, ":::", sol_object
	solution = solution + "Case #" + str(index) + ": " + str(playDeceitfulWar(case)) + " " + str(playWar(case)) +'\n'
	index = index + 1

print solution

fo = open(filename+'.out', 'w')
solution = solution.strip()
fo.write(solution)
fo.close()