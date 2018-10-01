>>> from fractions import gcd
>>> def f():
	cin = open('input.in')
	out = open('output.txt', 'w')
	for i in range(int(cin.readline())):
		s = cin.readline()
		ar = s.split(' ')
		res = abs(int(ar[2]) - int(ar[1]))
		for j in range(3, int(ar[0]) + 1):
			res = gcd(res, abs(int(ar[j]) - int(ar[j - 1])))
		maximum = int(ar[1])
		for j in range(2, int(ar[0]) + 1):
			if (int(ar[j]) > maximum):
				maximum = int(ar[j])
		result = res
		while result < maximum:
			result += res
		out.write('Case #' + str(i + 1) + ': ' + str(result - maximum) + '\n')
	out.close()
	cin.close()

>>> f()