import copy
def process_input(inpf):
	number_of_tests = int(inpf.readline())
	result = []
	for i in range(number_of_tests):
		inpf.readline()
		devices = inpf.readline().split()
		sockets = inpf.readline().split()
		result += ["Case #"+str(i+1)+": "+str(process(devices, sockets))]
	return result
	
def process(devs,socs):
	diffs = buildDiffs(devs,socs)
	mindiff = analyseDiff(diffs)
	if mindiff == -1:
		return "NOT POSSIBLE"
	else: 
		return mindiff
def buildDiffs(devlist, soclist):
	diffs = []
	for dev in devlist:
		diffs += [ [] ]
		for soc in soclist:
			diffs[-1] += [buildDiff(dev,soc)]			
	return diffs
def buildDiff(dev, soc):
	result = []
	for i in range(len(dev)):
		if dev[i] != soc[i]:
			result += [i]
	return result
def analyseDiff(diffs):
	if(len(diffs) == 1):
		return len(diffs[0][0])
	idlist = intersectListsDiffIds(diffs[0], diffs[1])
	for diffList in diffs[2:]:
		idlist = intersectListsPreviousIds(idlist, diffList)
	if not idlist :
		return -1
	min = 1000
	for idx in idlist:
		if min > len(idx[1]):
			min = len(idx[1])
	return min
def intersectListsDiffIds( listx, listy):
	result = []
	for idx, x in enumerate( listx):
		for idy, y in enumerate(listy):
			if idx != idy and y == x:
				result += [([idx]+[idy], y)]
	return result
def intersectListsPreviousIds( idList, list):
	result = []
	for idx in idList:
		for idy, y in enumerate(list):
			if idy not in idx[0] and y == idx[1]:
				result += [(idx[0]+[idy], y)]
	return result
def execute()	:
		#args = parse_arguments()
		input_file = open("in", 'r')
		out = process_input(input_file)
		output_file = open( "out", 'w')
		output_file.write("\n".join(out))

execute()