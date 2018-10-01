def f(platelist,c):
	if(c == 0):
		return 1
	max_value = max(platelist)
	max_index = platelist.index(max_value)
	if(max_value <=3):
		return max_value
	optimal = max_value
	for k in xrange(2,int(max_value/2)+1):
		optimal = min(optimal,1+f(trafo(platelist,max_value,max_index,k),c-1))
	return optimal

def trafo(liste,v,i,k):
	lis = liste[:]
	lis[i] = v-k
	lis.append(k)
	return lis
	
for cases in xrange(input()):
	D = input()
	nput = raw_input()
	plates = nput.split()
	plates = [int(x) for x in plates]
	globmax = max(plates)
	optmin = f(plates,globmax)
	print "Case #"+str(cases+1)+": "+str(optmin)

