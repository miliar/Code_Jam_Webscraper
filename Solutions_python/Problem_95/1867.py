def create_alphabet():
	l = []
	for i in xrange(ord('a'), ord('z') + 1):
		l.append(chr(i))
	return l

def is_letter(c):
	return ord(c) >= ord('a') and ord(c) <= ord('z')

def create_trans_map():
	m = {}
	t = """
	our language is impossible to understand
	there are twenty six factorial possibilities
	so it is okay if you want to just give up
	"""
	f = """
	ejp mysljylc kd kxveddknmc re jsicpdrysi
	rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
	de kr kd eoya kw aej tysr re ujdr lkgc jv
	"""
	f = filter(is_letter, f)
	t = filter(is_letter, t)
	tm = create_alphabet()
	fm = create_alphabet()
	for i in xrange(len(f)):
		m[f[i]] = t[i]
		try:
			tm.remove(t[i])
			fm.remove(f[i])
		except ValueError:
			#print 'ValueError:', tm, fm, f[i], t[i]
			pass
	#print tm, fm
	assert len(tm) == len(fm) and len(fm) == 2, 'len tm fm: %i %i' % (len(tm), len(fm))
	m[fm[0]] = fm[1]
	m[fm[1]] = fm[0]
	return m

m = create_trans_map()
#print map(lambda x: m[x], create_alphabet())
T = int(raw_input())
for i in xrange(T):
	s = raw_input()
	print 'Case #%i: %s' % (i + 1, ''.join(map(lambda c: m[c] if c in m else c, s)))

