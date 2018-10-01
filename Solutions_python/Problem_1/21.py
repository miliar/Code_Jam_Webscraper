#!/usr/bin/python
fin = open("q1.in","r")
fout = open("q1.out","w")
n = int(fin.readline())

for i in range(n):
	s = int(fin.readline())
	engines = set()
	for j in range(s):
		engines.add(fin.readline().strip())
	
	q = int(fin.readline())
	m = 0
	current = set(engines)
	for j in range(q):
		e = fin.readline().strip()
		
		if e in current:
			current.remove(e)
			
		if len(current) == 0:
			current = set(engines)
			current.remove(e)
			m += 1
			
	print >> fout, "Case #%d: %d" % (i+1, m)