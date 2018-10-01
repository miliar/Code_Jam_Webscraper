
def compress(s):
	u = []
	m = []
	for c in s:
		if not u or c != u[-1]:
			u.append(c)
			m.append(1)
		else:
			m[-1] += 1
	return ("".join(u), m)

def case(file):
	n = int(file.readline())
	s = []
	for i in range(n):
		s.append(file.readline().strip())
	u, m = [None for i in range(n)], [None for i in range(n)]
	for i in range(n):
		u[i], m[i] = compress(s[i])
	if not all(u[i] == u[i + 1] for i in range(n - 1)):
		return "Fegla Won"
	l = len(u[0])
	total = 0
	for k in range(l):
		avg = round(float(sum(m[i][k] for i in range(n))) / n)
		total += sum(abs(m[i][k] - avg) for i in range(n))
	return str(total)




def cases(in_name, func=None, out_name=None, stdout=None):
	import sys
	if func is None:
		func = case
	if out_name is None:
		ext = in_name.rindex('.')
		out_name = in_name[:ext] + ".out"
	with open(in_name, 'r') as fin:
		if stdout:
			fout = sys.stdout
			ntests = int(fin.readline())
			for i in range(1, ntests + 1):
				fout.write("Case #%i: %s\n" % (i, func(fin)))
		else:
			with open(out_name, 'w') as fout:
				ntests = int(fin.readline())
				for i in range(1, ntests + 1):
					fout.write("Case #%i: %s\n" % (i, func(fin)))

def time(func, *args, **kwargs):
	import time
	start = time.time()
	func(*args, **kwargs)
	end = time.time()
	return end - start

print(time(cases, "A-test.in", stdout=1))
print(time(cases, "A-small-attempt0.in", stdout=0))
print(time(cases, "A-large.in", stdout=0))