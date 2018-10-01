#!python
import sys
import string

def googlers(input):
	input = input.split()
	#print input
	N = int(input[0])
	S = int(input[1])
	p = int(input[2])
	scores = map(int, input[3:])
	#print "scores: ", scores
	count = 0
	surprise = 0
	for score in scores:
		if score >= p: #Sum of 3 scores should at least be >= p
			if score >= 3*p-2:
				count += 1
			elif score >= 3*p - 4 and surprise < S:
				count += 1
				surprise += 1
	return count	

def main(*args):
	if len(args) < 2:
		print "Usage:\n", args[0], " <file>\n"
		return
	file = open(args[1])
	text = file.read().split('\n')
	arr = list(text)
	#print arr
	
	cases = int(arr[0])	
	i = 1
	while i <= cases:
		print "Case #%s: %s" % (i, googlers(arr[i]))
		i += 1

if __name__ == '__main__':
    sys.exit(main(*sys.argv))