#!/bin/sh

fname = 'A-small-attempt0'

def tokreader(filename):
	for line in open(filename):
		for item in line.strip().split():
			yield item

def readn(n):
    r = []
    for i in xrange(n):
        r.append(read)
    return r

def solve():
	inp = tokreader(fname+'.in')
	read = lambda: inp.next()
	readn = lambda x:[read() for i in xrange(x)]
	outp = open(fname+'.out','w')

	N = int(read())
	for i in range(1,N+1):
		a1 = int(read())
		t1 = map(int,readn(16))
		a2 = int(read())
		t2 = map(int,readn(16))
		s1 = set(t1[a1*4-4:a1*4])
		s2 = set(t2[a2*4-4:a2*4])
		sol = []
		for n in range(1,17):
			if (n in s1) and (n in s2):
				sol += [n]
		print t1,t2
		print a1,s1,a2,s2,sol
		if len(sol) == 0:
			res = "Volunteer cheated!"
		if len(sol) > 1:
			res = "Bad magician!"
		if len(sol) == 1:
			res = str(sol[0])

		res = 'Case #%d: %s\n'%(i,res)
		print res
		outp.write(res)

	outp.close()
	print 'finished'