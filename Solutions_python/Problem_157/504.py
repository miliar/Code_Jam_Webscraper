
muls = {\
	 'i' : { 'i' : -1, 'j' : 'k', 'k' : '-j', -1 : '-i', '-i' : 1, '-j' : '-k', '-k' : 'j' },
     '-i' : { 'i' : 1, 'j' : '-k', 'k' : 'j', -1 : 'i', '-i' : -1, '-j' : 'k', '-k' : '-j' },
     'j' : { 'i' : '-k', 'j' : -1, 'k' : 'i', -1 : '-j', '-i' : 'k', '-j' : 1, '-k' : '-i' },
     '-j' : { 'i' : 'k', 'j' : 1, 'k' : '-i', -1 : 'j', '-i' : '-k', '-j' : -1, '-k' : 'i' },
     'k' : { 'i' : 'j', 'j' : '-i', 'k' : -1, -1 : '-k', '-i' : '-j', '-j' : 'i', '-k' : 1 },
     '-k' : { 'i' : '-j', 'j' : 'i', 'k' : 1, -1 : 'k', '-i' : 'j', '-j' : '-i', '-k' : -1 },
     -1 : { 'i' : '-i', 'j' : '-j', 'k' : '-k', -1 : 1, '-i' : 'i', '-j' : 'j', '-k' : 'k' },
}

def mul_q(x, y):
	if x == 1:
		return y
	if y == 1:
		return x

	return muls[x][y]

def mul_str(s):
	val = 1
	for c in s:
		val = mul_q(val, c)

	return val

def calc_dij(s, l, x):
	# each 4 repetitions of the string just evaluate to 1
	# but we need at least 12 for enough degrees of freedom
	x = min(x, 12 + (x % 4))

	# get the full string
	s = s * x
	l = l * x

	# 'ijk' = -1
	if mul_str(s) != -1:
		return False

	# now find 'i' in the beginning
	idx_i = -1
	val = 1
	for i in xrange(l):
		val = mul_q(val, s[i])
		if val == 'i':
			idx_i = i
			break

	if idx_i == -1:
		return False

	# find 'k' in the end, going back to the index of i.
	# if we found it, it means there's 'j' in the middle
	# because of the shared truth val
	val = 1
	for i in xrange(l - 1, idx_i, -1):
		val = mul_q(s[i], val)
		if val == 'k':
			return True

	return False

if __name__ == '__main__':
	import sys
	import time

	start_time = time.time()

	data = file(sys.argv[1], "rb").read()
	lines = data.split('\n')
	out = file(sys.argv[1] + "-sol.dat", "wb")

	for i in xrange(int(lines[0])):
		l, x = lines[2*i + 1].strip().split(' ')
		s = lines[2*i + 2].strip()
		if int(l) != len(s):
			raise Exception("wrong length..")

		out.write("Case #%d: %s\n" % (i + 1, "YES" if calc_dij(s, int(l), int(x)) else "NO"))

	out.close()
	print "--- %s seconds ---" % (time.time() - start_time)
