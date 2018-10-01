import sys

with open(sys.argv[1]) as f:
	for x, l in enumerate(f.readlines()):
		if x == 0:
			continue
		l = l.split()
		m = int(l[0])
		subs = {''.join(sorted(p[:2])) : p[2] for p in l[1:m+1]}
		n = int(l[m+1])
		opps = l[m+2:m+n+2]
		seq = l[m+n+3]
		elems = []
		for s in seq:
			elems += [s]
			if len(elems) > 1:
				a, b = elems[-1], elems[-2]
				ss = ''.join(sorted(a+b))
				if ss in subs:
					elems.pop()
					elems.pop()
					elems.append(subs[ss])

				a = elems[-1]
				for i in elems:
					if a+i in opps or i+a in opps:
						elems = []
						break

		print('Case #%i: [%s]' % (x, ', '.join(elems)))
