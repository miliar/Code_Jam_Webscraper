import sys

def GCD(a, b):
	while b > 0:
		c = a
		a = b
		b = c % b
	return a


def AllGCD(numbers):
	n = len(numbers)
	if n == 1:
		return numbers[0]

	g = GCD(numbers[0], numbers[1])
	for i in range(1, n):
		g = GCD(g, numbers[i])
	return g

def getT(numbers):
	ret = []
	numbers = sorted(numbers)
	n = len(numbers)
	for i in range(1, n):
		tmp = numbers[i] - numbers[i-1]
		ret.append(tmp)
	return AllGCD(ret)

def solve(numbers):
	t = getT(numbers)
	if numbers[0] % t == 0:
		return 0
	else:
		return t - numbers[0] % t
	n = len(numbers)
	for i in range(0, t):
		y = i
		hena = 1
		for j in range(0, n):
			if (numbers[j] + i) % t != 0:
				hena = 0
		if hena == 1:
			return y
	return -1


outfile = open('C:\\Users\\Asami\\Desktop\\boutput.txt', 'r')
infile = open('C:\\Users\\Asami\\Desktop\\binput.txt', 'r')
inp = infile.readline()
c = int(inp)
for i in range(0, c):
	inp = infile.readline()
	splitted = inp.split(' ')
	n = int(splitted[0])
	numbers = []
	for j in range(0, n):
		numbers.append(int(splitted[j+1]))

	sys.stdout.write('Case #')
	sys.stdout.write(i+1)
	sys.stdout.write(': ')
	sys.stdout.write(solve(numbers))
	sys.stdout.write('\n')
	#print ('Case #', (i+1), ': ', solve(numbers), sep='')
	#outfile.write('Case #')
	#outfile.write(i+1)
	#outfile.write(': ')
	#outfile.write(solve(numbers))
	#outfile.write('\n')
	
#infile.close()
#outfile.close()
