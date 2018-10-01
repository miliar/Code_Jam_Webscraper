#!/usr/bin/python


def readfile():
    nrs = []
    with open('nrs.in', 'r') as f:
        f.readline()
        for line in f:
			nr = int(line)
			nrs.append(nr)
    return nrs


def solve(n):
	nlist = map(int, list(str(n)))
	k = 0
	for i in xrange(len(nlist)-1):
		if nlist[i] == nlist[i+1] and nlist[k] != nlist[i]:
			k = i
		if nlist[i] > nlist[i+1]:
			if nlist[k] == nlist[i]:
				nlist[k] -= 1
				for j in xrange(k+1, i+1):
					nlist[j] = 9
			else:
				nlist[i] -= 1
			for j in xrange(i+1, len(nlist)):
				nlist[j] = 9
			break
	return int(''.join(map(str, nlist)))


nrs = readfile()
with open('nrs.out', 'w') as f:
    for i, nr in enumerate(nrs):
        sol = solve(nr)
        newline = '\n' if i < len(nrs)-1 else ''
        f.write('Case #%d: %d%s' % (i+1, sol, newline))	
