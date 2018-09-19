from sys import argv

conv = [('q', 'z'), ('z', 'q'), ('o', 'e'),  ('u', 'j'), ('r', 'p'), ('l', 'm'), ('a', 'y'), ('n', 's'), ('g', 'l'), ('e', 'c'), ('i', 'k'), ('s', 'd'), ('m', 'x'), ('p', 'v'), ('b', 'n'), ('t', 'r'), ('d', 'i'), ('h', 'b'), ('w', 't'), ('y', 'a'), ('x', 'h'), ('f', 'w'), ('c', 'f'), ('k', 'o'), ('j', 'u'), ('v', 'g')]


def replace(cad, conv):
	nueva=""
	for c in cad:
		ok=False
		for cv in conv:
			if cv[1]==c:
				nueva+=cv[0]
				ok=True
		if not ok:
			nueva+=c
	return nueva
	

f=open(argv[1])

l=f.read().split("\n")[:-1]

i=1

while i<len(l):
	print "Case #%i: %s" %(i, replace(l[i], conv))
	i+=1
