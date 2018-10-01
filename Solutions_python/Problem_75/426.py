def solve_test_case(line):
	tokens = line.split(' ')
	place = 0
	C = int(tokens[place])
	place += 1
	base_elements = {}
	for i in xrange(place, place+C):
		base1, base2, base_result = tokens[place]
		base_elements[(base1, base2)] = base_result
		base_elements[(base2, base1)] = base_result
		place += 1
		
	D = int(tokens[place])
	place += 1
	resisting_elements = []
	for i in xrange(place, place+D):
		resisting_element = tokens[place]
		resisting_elements.append((resisting_element[0],resisting_element[1]))
		resisting_elements.append((resisting_element[1],resisting_element[0]))
		place += 1
		
	N = int(tokens[place])
	place += 1
	invoke_list = tokens[place]
	result = ""
	for invoke in invoke_list:
		result += invoke
		combined = False
		while len(result)>1 and (result[-2], result[-1]) in base_elements:
			result = result[:-2] + base_elements[(result[-2], result[-1])]
			combined = True
		if not combined:
			for c in result:
				if (c, invoke) in resisting_elements:
					result = ""
					break
	assert N == len(invoke_list)
	return result

def solve(filename):
	infile = open(filename, 'rb')
	T = infile.readline()
	for i in xrange(int(T)):
		result = solve_test_case(infile.readline().rstrip())
		print "Case #%d: %s" % (i+1, '[' + ', '.join(result) + ']')

if __name__ == "__main__":
	import sys
	solve(sys.argv[1])