#! /usr/bin/python
# Ugliest code ever. Dumb dumb mistakes.

def read():
	fp = open("input.txt", "r")
	numCases = int(fp.readline())
	x = range(numCases)

	for f in range(numCases):
		numEngines = int(fp.readline())
		x[f] = {"engines":range(int(numEngines)),"queries":[], "revEng":{}}
		x[f]['engines'] = range(numEngines)
		for engineNum in range(numEngines):
			engine = fp.readline()
			x[f]['engines'][engineNum] = engine
			x[f]['revEng'][engine] = engineNum
		numQueries = int(fp.readline())
		x[f]['queries'] = range(numQueries)
		for queryNum in range(numQueries):
			x[f]['queries'][queryNum] = x[f]['revEng'][fp.readline()]
	fp.close()
	return x

def solve(engines, queries):
	if len(queries) == 0:
		return 0
	# matrix of engines*engines dimension
	numEngines = len(engines)
	answer = split(0, len(queries), queries, numEngines)
	return min(answer)
	
def split(start, finish, queries, numEngines):
	spread = finish - start
	if spread <= 1:
		return baseResult(start, queries, numEngines)
	half = spread/2
	result1 = split(start, start + half, queries, numEngines)
	result2 = split(start + half, finish, queries, numEngines)
	return combine(result1, result2, numEngines)

def baseResult(start, queries, numEngines):
	"""Assumes results is filled with numQueries values at start"""
	r = [len(queries)] * numEngines * numEngines
	for i in range(numEngines):
		if i != queries[start]:
			r[i*numEngines + i] = 0
	return r
	

def combine(result1, result2, numEngines):
	r = range(len(result1))
	for i in range(len(result1)):
		row = i / numEngines
		col = i % numEngines
		r[i] = combineHelper(row,col,numEngines,result1, result2)
	return r
	

def combineHelper(row,col,numEngines,result1, result2):
	values = ["x"] *(numEngines*numEngines)
	for i in range(numEngines*numEngines):
		r = i / numEngines
		s = i % numEngines
		if r != s:
			switch = 1
		else:
			switch = 0
		values[i] = result1[row*numEngines + r] + result2[s*numEngines + col] + switch

	return min(values)


if __name__ == "__main__":
	x = read()
	for i in range(len(x)):
		y = solve(x[i]['engines'],x[i]['queries'])
		print "Case #%d: %d" % (i+1, y)
