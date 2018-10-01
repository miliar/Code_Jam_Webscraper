#f = file("problem2test.in", "r")
#f = file("/Users/finn/Downloads/B-small-attempt0.in", "r")
#f = file("/Users/finn/Downloads/B-small-attempt1.in", "r")
#f = file("/Users/finn/Downloads/B-small-attempt2.in", "r")
f = file("/Users/finn/Downloads/B-large.in", "r")
#of = file("B-small.out", "w")
of = file("B-large.out", "w")
lines = f.readlines()

cases = int(lines[0])
line = 1
for case in range(cases):
	elements = lines[line].split()
	
	c = int(elements[0])
	idx = 1
	combine = {}
	for i in range(c):
		e1 = elements[idx][0]
		e2 = elements[idx][1]
		combine[e1 + e2] = elements[idx][2]
		combine[e2 + e1] = elements[idx][2]
		idx += 1
		
	d = int(elements[idx])
	idx += 1
	opposed = {}
	for i in range(d):
		e1 = elements[idx][0]
		e2 = elements[idx][1]
		if not opposed.has_key(e1):
			opposed[e1] = set()
		opposed[e1].add(e2)
		if not opposed.has_key(e2):
			opposed[e2] = set()
		opposed[e2].add(e1)
		
		idx += 1
	
	n = int(elements[idx])
	s = elements[idx + 1]
	present = set()
	
	result = []
	for e in s:
		if len(result) >= 1:
			k = e + result[-1]
			if combine.has_key(k):
				result = result[:-1]
				result.append(combine[k])
				continue
			
		if opposed.has_key(e):
			op = opposed[e]
			found = False
			for a in result:
				if a in op:
					found = True
			
			if found:
				result = []
				continue
				
		result.append(e)
		
	res = '['
	for r in result:
		if len(res) == 01:
			res += r
		else:
			res += ', ' + r
			
	res += ']'
	of.write("Case #%d: %s\n" % (case + 1, res))
	
	line += 1