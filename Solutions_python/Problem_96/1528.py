import sys
import string


def solver(S, p, G):
	n = 0
	for g in G:
		average = g/3
		rest = g % 3
		if (average >= p) or (average + rest > p):
			n = n + 1
		elif average + rest == p:
			if rest < 2:
				n = n + 1
			elif rest == 2 and S > 0:
				n = n + 1
				S = S - 1	
		elif (average + rest == p - 1) and (rest == 0) and (average > 0) and S > 0:
			n = n + 1
			S = S - 1
	return n	

f = open("test.out", 'w')
cases = open("test.in", 'r').readlines()
T = int(cases[0])
for i in xrange(T):
	case = cases[i+1]
	case = map(int, cases[i+1].split())
	result = solver(case[1], case[2], case[3:])
	line = "Case #" + str(i+1) + ": " + str(result)
	print line
	i = i + 1
	f.write(line + "\n")
f.close()