import math
import sys

def is_palindrome(s):
	s=str(s)
	for i in range(0, len(s)//2):
		if (s[i] != s[len(s)-i-1]): 
			return False
	return True

#source: http://stackoverflow.com/questions/2489435/how-could-i-check-if-a-number-is-a-perfect-square
# - "Babylonian algorithm"
def is_square(apositiveint):
	if( apositiveint == 1 or apositiveint == 4 or apositiveint == 9): return True
	x = apositiveint // 2
	seen = set([x])
	while x * x != apositiveint:
		x = (x + (apositiveint // x)) // 2
		if x in seen: return False
		seen.add(x)
	return True

def main():
	numCases = int(sys.stdin.readline())
	for i in range(1, numCases+1):
		counter = 0
		line = sys.stdin.readline()
		#lo = int(line.split( )[0])
		#hi = int(line.split( )[1])
		for j in range(int(line.split( )[0]), int(line.split( )[1])+1):
			if ( is_palindrome(j) and is_square(j) ):
				if( is_palindrome(int(math.sqrt(j)))):
					counter = counter + 1
					#print "found"+str(j)
		print "Case #"+str(i)+": "+str(counter)

if __name__ == '__main__':
	main()
