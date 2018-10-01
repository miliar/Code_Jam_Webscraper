import math
import sys

def main():
	inputFile = sys.argv[1]
	f = open(inputFile, "r")
	o = open("output.txt", "w")
	numOfTestCases = int(f.readline()[:-1])
	r = 0
	t = 0
	count = 0
	for i in range(numOfTestCases):
		count = 0
		if i == numOfTestCases - 1:
			line = f.readline()
		else:
			line = f.readline()[:-1]
		# print line
		r = int(line.split(' ')[0])
		t = int(line.split(' ')[1])
		while t > 0:
			t = t - ((r + 1) * (r + 1) - r * r)
			r = r + 2
			if t >= 0:
				count = count + 1
		print "count is" + str(count)
		o.write("Case #" + str(i + 1) + ": " + str(count) + "\n")



















if __name__ == "__main__":
    main()