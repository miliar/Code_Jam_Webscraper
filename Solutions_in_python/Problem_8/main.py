f = file("B-small-attempt3.in")
#f = file("A-large.in")
#f = file("test.in")
of = file("B-small-attempt3.out", "w")
#of = file("A-large.out")
#of = file("test.out", "w")

from prime import Prime

def calc(a, b, p):
	sets = []
	for i in range(a, b + 1):
		factors = Prime().factorize(i)
		s = set()
		for f in factors:
			if f >= p:
				s.add(f)
				
		sets.append(s)
		print i, "Factors", (i, s)

	pruned = True
	while pruned:
		pruned = False
		result = []
		print "Pruning of", len(sets)
		for s in sets:
			j = 0
			while j < len(result):
				if len(s.intersection(result[j])) > 0:
					print "Pruned", s, "with", result[j]
					pruned = True
					result[j] = result[j].union(s)
					break
				
				j += 1
			
			if j >= len(result):
				result.append(s.copy())
					
		sets = result
		
		
	return len(sets)

cases = int(f.readline().strip())
for case in range(cases):
	v = f.readline().strip().split()
	a = int(v[0])
	b = int(v[1])
	p = int(v[2])
	print "Processing case", case + 1
	result = calc(a, b, p)
	print "Result:", result
	of.write("Case #" + str(case + 1) + ": " + str(result) + "\n");
	
