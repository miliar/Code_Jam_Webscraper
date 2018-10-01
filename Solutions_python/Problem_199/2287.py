def numFlips(pancakes, k):
	flipsRequired = 0

	for i in xrange(0, len(pancakes)+1-k):
		if pancakes[i] == '-':
			flipsRequired += 1
			flipper = pancakes[i:i+k]
			pancakes = pancakes[:i] + flipPancakes(flipper) + pancakes[i+k:]

	for i in xrange(len(pancakes)-k, len(pancakes)):
		if pancakes[i] == '-':
			flipsRequired = "IMPOSSIBLE"

	return flipsRequired


def flipPancakes(pancakes):
	flippedPancakes = ""
	for i in xrange(0,len(pancakes)):
		if pancakes[i] == '-':
			flippedPancakes += '+'
		else:
			flippedPancakes += '-'

	return flippedPancakes


def main():
	# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
	# This is all you need for most Google Code Jam problems.
	t = int(raw_input())  # test cases
	for i in xrange(1, t+1):
	  	pancakes, k = raw_input().split(" ")
	  	print "Case #{}: {}".format(i,numFlips(pancakes,int(k)))
	  	#n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
	  	#print "Case #{}: {} {}".format(i, n + m, n * m)
	  	# check out .format's specification for more formatting options


if __name__=='__main__':
	main()
