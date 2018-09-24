import sys

def parseArgv():
	input = sys.argv[1]
	output = sys.argv[2]
	return (input, output)

def parseCase(cases):
	# List engines
	S = int(cases[0]) # number of search engines
	engines = [e.rstrip('\n') for e in cases[1:S+1]] # list of search engines
	del cases[:S+1]
	# List queries
	Q = int(cases[0]) # number of queries
	queries = [q.rstrip('\n') for q in cases[1:Q+1]] # list of queries
	del cases[:Q+1]
	return (engines, queries)
	
def processQueries(e, q):
	engines = {}
	switches = 0
	for engine in e:
		engines[engine] = False
	while len(q) > 0:
		found = 0
		while found < len(engines) and len(q) > 0:
			if engines[q[0]] == False:
				engines[q[0]] = True
				found += 1
			if found < len(engines):
				q.pop(0)
		if len(q) > 0:
			for k in engines.iterkeys(): #reset dict
				engines[k] = False
			switches += 1
	return switches
	
# Main program starts here
filenames = parseArgv()
input = open(filenames[0], 'r')
output = open(filenames[1], 'w')

cases = input.readlines()
n_cases = int(cases[0]) #number of cases
del cases[0]
for i in range(n_cases):
	engines, queries = parseCase(cases)
	n = processQueries(engines, queries)
	output.write('Case #%d: %d\n' % (i+1, n))
print('Output processed! Now closing...')
input.close()
output.close()
