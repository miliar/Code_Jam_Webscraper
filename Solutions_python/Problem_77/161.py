T = int(raw_input())

def countWellPlaced(elements):
	elementsSorted = elements[:]
	elementsSorted.sort()
	wellPlacedCount = 0
	stillWellPlaced = True
	pos = 0
	for i,element in enumerate(elementsSorted):
		if element == elements[i]:
			wellPlacedCount += 1
		
# 	pos = len(elements)-1
# 	stillWellPlaced = True
# 	while stillWellPlaced:
# 		if elementsSorted[pos] == elements[pos]:
# 			wellPlacedCount += 1
# 		else:
# 			stillWellPlaced = False
# 		pos -= 1
	return wellPlacedCount

def solveCase(elements):
	wellPlacedCount = countWellPlaced(elements)
	return len(elements)-wellPlacedCount
	
for t in range(1,T+1):
	N = int(raw_input())
	elements = map(int,raw_input().split())
	sol = solveCase(elements)
	print "Case #%d: %.6f" % (t,float(sol))