import sys



def longestdist(engines, queries, index):  # returns new index, or len(queries) on end
	arr = []
	for eng in engines:
		i = index
		while (i < len(queries)) and (eng != queries[i]):
			i += 1
		if i == len(queries):
			return i  # the end
		else:
			arr.append(i)
	return max(arr)


def findmain(engines, queries):
	iter = 0
	i = longestdist(engines, queries, 0)
	while i < len(queries):
		iter += 1
		i = longestdist(engines, queries, i)
	return iter


def main():
	try:
		inp = open(sys.argv[1], 'rt')
	except IOError:
		print 'Invalid input file name'
		sys.exit(2)

	out = open(sys.argv[2], 'wt')	

	ncases = int(inp.readline())
	print ncases

	for i in xrange(ncases):
		print i
		nengines = int(inp.readline())
		engines = []
		for j in xrange(nengines):
			engines.append(inp.readline()[:-1])

		nqueries = int(inp.readline())
		queries = []
		for k in xrange(nqueries):
			queries.append(inp.readline()[:-1])

		out.write('Case #%d: %d\n' % (i + 1, findmain(engines, queries)))

	
	inp.close()
	out.close()


if __name__ == '__main__':
	main()
