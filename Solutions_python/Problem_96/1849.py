import string, copy
DEBUG = False
outstanding = {}
r03 = range(0, 3)
r04 = range(0, 4)
r25 = range(2, 5)
mxx = map(lambda t:lambda x:3 * x + t, range(0, 5))
#maxgetter = map(lambda t:lambda coefficient, reminder, x:(x - reminder) / 3 - 3 * t + coefficient, [0, 1])
def sx(coefficient, x, reminder, t):
	xreminder = x - reminder
	if DEBUG:
		print 'sx t {0} x {1} reminder {2} xreminder {3}'.format(t, x, reminder, xreminder)
	_3a = (xreminder) / 3
	if _3a > 0:
		_3a -= 3 * t
	elif reminder == 0:
		return 0
	assert((xreminder) % 9 == 0)
	if DEBUG:
		print 'debug {0}/3 -3*{1}+{2}={3}'.format(xreminder, t, coefficient, _3a + coefficient)
	return _3a + coefficient
maxgetter = map(lambda t:lambda coefficient, reminder, x:sx(coefficient, x, reminder, t), [0, 1])
_01set = set([0, 1])
for outstandingiter in r25:
	for aiter in r03:
		reminder = (3 * (outstandingiter - 2) + aiter + 2) % 9
		if reminder in _01set:
			idx = 1
		else: 
			idx = 0
		reminderlambda = map(lambda preparr:(lambda x:apply(maxgetter[preparr[2]], [preparr[0], preparr[1], x])), [[outstandingiter, reminder, idx]])[0]
		outstanding[reminder] = [reminderlambda , map(mxx[outstandingiter], r03)]
		#print outstanding[reminder][0](20)
notstanding = {}
s23 = set([2, 3])
for notstandingiter in r25:
	notstanding[3 * (notstandingiter - 2) + 0] = [map(lambda notstandingiter:lambda x:apply(maxgetter[0], [(notstandingiter - 2) + 0, 3 * (notstandingiter - 2) + 0, x]), [notstandingiter])[0], filter(lambda x:x >= 0 and x <= 10, map(mxx[(notstandingiter - 2)], r04))]
	notstanding[3 * (notstandingiter - 2) + 1] = [map(lambda notstandingiter:lambda x:apply(maxgetter[0], [(notstandingiter - 2) + 1, 3 * (notstandingiter - 2) + 1, x]), [notstandingiter])[0], filter(lambda x:x >= 0 and x <= 10, map(mxx[(notstandingiter - 2) + 1], r04))]
	notstanding[3 * (notstandingiter - 2) + 2] = [map(lambda notstandingiter:lambda x:apply(maxgetter[0], [(notstandingiter - 2) + 1, 3 * (notstandingiter - 2) + 2, x]), [notstandingiter])[0], filter(lambda x:x >= 0 and x <= 10, map(mxx[(notstandingiter - 2) + 1], r04))]
if DEBUG:
	print outstanding
	print notstanding
#print outstanding[2][0](20)
def getquery(n, s, p, tarr):
	if DEBUG:
		print 'start query n s p tarr', n, s, p, tarr
	# and (x[0] not in map(lambda x:x[0], notstandings))
	notstandings = filter(lambda x:(x[2] in notstanding[x[1]][1]) and (x[2] >= p), map(lambda x:[x[0], x[1] % 9, notstanding[x[1] % 9][0](x[1]), 'n'], [[t, tarr[t]] for t in range(0, len(tarr))]))
	outstandings = filter(lambda x:(x[2] in outstanding[x[1]][1]) and (x[2] >= p)and (x[0] not in map(lambda x:x[0], notstandings)), map(lambda x:[x[0], x[1] % 9, outstanding[x[1] % 9][0](x[1]), 'o'], [[t, tarr[t]] for t in range(0, len(tarr))]))
	notstandings=sorted(notstandings, key=lambda x:x[2], reverse=True)
	outstandings=sorted(outstandings, key=lambda x:x[2], reverse=True)
	"""
	merged = []
	merged.extend(notstandings)
	merged.extend(outstandings)
	merged = sorted(merged, key=lambda x:x[2], reverse=True)
	"""
	#print merged
	#assert(len(outstandings) >= s)
	#print len(outstandings)
	"""
	print notstandings and outstandings
	if DEBUG:
		print 'lenout', len(outstandings)
	if DEBUG:
		print 'notstanding'
	"""
	if len(outstandings) > s:
		outstandings = outstandings[0:s]
		assert(len(outstandings) == s)
	if DEBUG:
		print 'outstandings', outstandings
		print 'notstandings', notstandings
	return len(outstandings) + len(notstandings)

lines=int(raw_input().strip())
for i in range(0,lines):
	params=map(int,raw_input().strip().split(' '))
	prep=params[0:3]
	prep.append(params[3:])
	#print prep
	print 'Case #{0}: {1}'.format(i+1,apply(getquery,prep))

#print getquery(3, 1 , 5, map(int, '15 13 11'.split(' ')))
#print getquery(3, 0, 8, map(int, '23 22 21'.split(' ')))
#print getquery(2, 1, 1, map(int, '8 0'.split(' ')))
#print getquery(6, 2, 8, map(int, '29 20 8 18 18 21'.split(' ')))

#niter=n
#selectedoutstandings
"""
lines=int(raw_input().strip())
def sanemap(x):
	if x not in pdict.keys():
		return x 
	return pdict[x]
for i in range(0,lines):
	print 'Case #{0}: {1}'.format(i+1,''.join(map(sanemap,raw_input())))
"""
