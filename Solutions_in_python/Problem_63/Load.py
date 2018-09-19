import re
import math

def self():
	t = int(sys.stdin.readline())
	i = 0
	while i<t:
		i = i+1
		print "Case #"+str(i)+":",

		line = sys.stdin.readline()
		L = int(line.split()[0])
		P = int(line.split()[1])
		C = int(line.split()[2])
		div = float(P)
		count = 0
		while True:
			if div/C > L:
				div = div/C
				count = count + 1
			else:
				break
		if count > 0:		
			value = int(math.log(count, 2))+1
		else:
			value = 0
		print value

	

if __name__ == "__main__":
	import sys
	self()
