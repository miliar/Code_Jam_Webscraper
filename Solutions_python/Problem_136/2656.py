# problem 2   #
# sayf_piratos#
###############
import sys
sys.stdin, sys.stdout = map(open, "B-large.in B-large.out".split(" "), "r w+".split(" "))
number_cases = int(sys.stdin.readline())

def time_tofinish(target, coockies, gen_rate):
	return (target-coockies)/gen_rate

def isbought(f, gen_rate, coockies, x):
	if (time_tofinish(x, coockies, gen_rate) <= time_tofinish(x, 0, gen_rate+f)):
		return False
	else:
		return True
for i in range(number_cases):
	line_input = sys.stdin.readline().strip().split(" ")
	c,f,x = float(line_input[0]), float(line_input[1]), float(line_input[2])
	cond = True
	t=0
	coockies = 0
	gen_rate = 2.0
	while (cond):
		if x > c:
			t += time_tofinish(c, coockies, gen_rate)
			coockies += c
			if (isbought(f, gen_rate, coockies, x)):
				coockies -= c
				gen_rate += f
			else:
				t += time_tofinish(x, coockies, gen_rate)
				cond = False
		else:
			t += time_tofinish(x, coockies, gen_rate)
			cond = False
	sys.stdout.write("Case #%d: %f\n" %((i+1), t))
