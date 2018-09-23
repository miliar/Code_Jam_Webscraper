# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def answer(n, k):
	N = n+2
	occupied_list = [0, N-1]
	for i in range(0,k):
		minLR = []
		maxLR = []
		posList = []
		#~ print occupied_list
		for j in range(1,len(occupied_list)):
			L = occupied_list[j-1]
			R = occupied_list[j]
			if (R-L) > 1:
				minVals = 0
				maxVals = 0
				pos = int((L+R)/2)
				posList.append(pos)
				minVals = min([abs(pos-L-1), abs(R-pos-1)])
				minLR.append(minVals)
				maxVals = max([abs(pos-L-1), abs(R-pos-1)])
				maxLR.append(maxVals)
				
		minLR_max = max(minLR)
		maxLR_min = max(maxLR)
		indices_min = [a for a,v in enumerate(minLR) if v == minLR_max]
		if len(indices_min) > 1:
			indices_max = [a for a,v in enumerate(maxLR) if v == maxLR_min]
			if len(indices_max) > 1:
				indices = list(set(indices_min).intersection(indices_max))
				retVal = indices[0]
			else:
				retVal = indices_max[0]
		else:
			retVal = indices_min[0]
		
		pos = posList[retVal]
		occupied_list.append(pos)
		occupied_list = sorted(occupied_list)
	return [maxLR_min, minLR_max]


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
	ans = answer(n, m)
	print "Case #{}: {} {}".format(i, ans[0], ans[1])

  
