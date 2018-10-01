#! 
import itertools
import sys
import string
import array

t = int(sys.stdin.readline())
i = 0
while (i < t):
	n = int(sys.stdin.readline())
	dulces = sys.stdin.readline()
	
	dulces = string.split(dulces)
	
	cand = array.array('i')
	mark = array.array('i')
	
	
	for x in dulces:
		cand.append(int(x))
		mark.append(int(x))
	
	temp = tuple(mark)
	
	sean = 0
	pat = 0
	patThinkSean = 0
	max = 0
	k = 1
	while(k < n):
		for comb in itertools.combinations(cand,k):
			for candy in comb:
				sean += candy
				patThinkSean = patThinkSean ^ candy
				mark.remove(candy)
			
			for candy in mark:
				pat = pat^candy
			
			if pat == patThinkSean :
				if sean > max:
					max = sean
			
			sean = 0
			pat = 0
			patThinkSean = 0
			mark = array.array('i')
			for x in temp:
				mark.append(x)
		k +=1
	if max > 0:
		print 'Case #{0}: {1}'.format((i + 1), max)
	else:
		print 'Case #{0}: {1}'.format((i + 1), 'NO')
	
	i += 1
