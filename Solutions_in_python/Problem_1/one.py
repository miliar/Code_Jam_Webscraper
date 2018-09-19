import sys;
def main():
	filename = sys.argv[1]
	f=open(filename,'r')
	tcCount=int(f.readline())
	for i in range(tcCount):
		#print 'Test Case ', i
		engineCount = int(f.readline())
		engines = []
		# read the engines
		for j in range(engineCount):
			engine = f.readline()
			engines.append(engine)
		#print 'engines = ',engines
		# read the input queries
		queryCount = int(f.readline())
		queries = []
		for j in range(queryCount):
			query = f.readline()
			queries.append(query)
		#print 'queries = ', queries
		
		# compute the answer
		switches = computeSwitch(engines, queries)
		print 'Case #%d: %d' % (i+1,switches)
		
	f.close()

def computeSwitch(e, q):
	if len(q) == 0:
		return 0
	qset = set(q)
	eset = set(e)
	if len(qset) < len(eset):
		diff = eset - qset
		return 0
	else:
		next = computeFurthest(e, q)
		return 1 + computeSwitch(e, q[next:])
			

def computeFurthest(e, q):
	furthest = 0
	for engine in e:
		position = q.index(engine)
		if position > furthest:
			furthest = position
	return furthest	
			
main()

