import sys


T = raw_input()

for i in range(int(T)):
	s = raw_input()
	A = int(s.split()[0])
	B = int(s.split()[1])

	l = len(s.split()[0])

	count = 0
	dict = {}
	for j in range(A, B):
		s = str(j)
		for k in range(l):
			s = s[-1] + s[:-1]
			if int(s) == j:
				break

			if int(s) > j and int(s) <= B:
				#print j, int(s)
				count = count + 1

	sys.stdout.write("Case #%d: %d\n" % ((i + 1), count))			


