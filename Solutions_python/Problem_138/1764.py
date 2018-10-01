def qsort(list):
    if list == []: 
        return []
    else:
        pivot = list[0]
        lesser = qsort([x for x in list[1:] if x < pivot])
        greater = qsort([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater
        
        
testCases = input()

warPoints = []
deceitfulWarPoints = []

for i in range(testCases):
	n = input()
	naomi = []
	ken = []
	aux = raw_input()
	aux = aux.split(" ")
	for j in aux:
		naomi.append(float(j))
	
	aux = raw_input()
	aux = aux.split(" ")
	for j in aux:
		ken.append(float(j))
	
	naomi = qsort(naomi)
	ken = qsort(ken)
	
	aux = 0
	for i in naomi:
		if i > ken[aux]:
			aux = aux + 1
			
	deceitfulWarPoints.append(aux)
	
	aux = 0
	for i in ken:
		if i > naomi[aux]:
			aux = aux + 1
	aux = n - aux
	warPoints.append(aux)

counter = 0
for i in deceitfulWarPoints:
	counter = counter +1
	print "Case #" + str(counter) + ": " + str(i) + " " + str(warPoints[counter-1])
	
	
			
		
	
	
