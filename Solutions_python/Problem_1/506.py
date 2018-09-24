""" GCJ 2008
"""

def greedy(search_engines, queries):
	dest = search_engines[:]
	switch_cnt = 0

	for q in queries:
		if q in dest:
			dest.remove(q)

		if len(dest) == 0:
			dest = search_engines[:]
			dest.remove(q)
			switch_cnt += 1

	return switch_cnt

def input():

	search_engines = []
	queries = []
	n = int(raw_input())

	for i in range(n):
		engines = []
		case_queries = []

		s_cnt = int(raw_input())
		for j in range(s_cnt):
			engine = raw_input()
			engines.append(engine)

		q_cnt = int(raw_input())
		for k in range(q_cnt):
			query = raw_input()
			case_queries.append(query)

		search_engines.append(engines)
		queries.append(case_queries)

	return search_engines, queries
def input_fromfile(fin):
	search_engines = []
	queries = []
	f = open(fin, "rU")
	n = int(f.readline())

	for i in range(n):
		engines = []
		case_queries = []

		s_cnt = int(f.readline())
		for j in range(s_cnt):
			engine = f.readline()
			engines.append(engine)

		q_cnt = int(f.readline())
		for k in range(q_cnt):
			query = f.readline()
			case_queries.append(query)

		search_engines.append(engines)
		queries.append(case_queries)
	
	return search_engines, queries

if __name__ == '__main__':
	s = ["Yeehaw", "NSM", "Dont Ask", "B9", "Googol"]
	q = ["Googol", "Dont Ask", "NSM", "NSM", "Yeehaw", "Yeehaw", "Googol"]
	print greedy(s, q)

	search_engines, queries = input_fromfile("D:\\proj\\googlecodejam\\gcj08\\A-large.in")
	fout = open("D:\\proj\\googlecodejam\\gcj08\\A-large.out", "w")
	for i in range(len(search_engines)):
		cnt = greedy(search_engines[i], queries[i])
		#print "Case #"+str(i+1)+": "+str(cnt) 
		fout.write("Case #"+str(i+1)+": "+str(cnt)+"\n")
	fout.close()
