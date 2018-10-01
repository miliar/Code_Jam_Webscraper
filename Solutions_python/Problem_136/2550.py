import string, sys

sourceName = sys.argv[1]
outputName = sys.argv[2]
source = open(sourceName)
output = open(outputName, 'w')

def solve(i, c, f, x):
	t = 0.0
	speed = 2.0
	cookies = 0.0
	while(True):
		if (cookies == x):
			result = "Case #%d: %.7f" % (i+1, t)
			print result
			output.write(result + '\n')
			break

		if (x <= c):
			t += x / float(speed)
			cookies += x
		elif (cookies < c):
			t += c / float(speed)
			cookies += c

		if float(x - cookies)/float(speed) >= float(x) / float(speed+f):
			cookies = 0.0
			speed += f
		else:
			t += float(x-cookies)/float(speed)
			cookies = x

testcase = int(source.readline())
for i in range(testcase):
	line = [float(n) for n in source.readline().split()]
	c = line[0]
	f = line[1]
	x = line[2]
	solve(i, c, f, x)