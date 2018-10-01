import sys

def test(test_num, in_file):
	c,f,x = (float(i) for i in in_file.readline().split(' '))
	speed = 2.0
	time = 0
	while x > c:
		make_sense = c / speed + x / (speed + f) < x / speed
		if not make_sense:
			break
		time += c / speed
		speed += f
	time += x / speed
	print("Case #%d: %.7f" % (test_num,time))

def tests(f):
	n = int(f.readline())
	for i in range(n):
		test(i + 1, f)

#with open("input.txt") as f:
#	tests(f)
tests(sys.stdin)
