#!python2.7
import fileinput

START_RATE = 2

input_text = []

for line in fileinput.input():
	input_text.append(line.strip())

T = int(input_text[0])

for t in xrange(1, T + 1):
	time = 0.0
	cookie_rate = 2.0
	C, F, X = map(float, input_text[t].split())
	while X / cookie_rate > X / (cookie_rate + F) + C / cookie_rate:
		time += C / cookie_rate
		cookie_rate += F

	print "Case #" + str(t) + ":",
	print '{0:.7f}'.format(round(time + X / cookie_rate, 7))
