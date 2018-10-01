import math
import sys

def foo(s):
	n  = len(s)
	k = 0
	m = 0
	for i in range(n):
		if s[i] == "0":
			continue
		if  k >= i:
			k += int(s[i])
		else:
			m += (i-k)
			k += int(s[i])
			k += m
	return m;

def main():
	f = open(sys.argv[1], 'r')
	l = f.readlines()	
	n = int(l[0])
	for k in range(n):			
		s = (l[k+1].split())[1]
		m = foo(s)
		print "Case #" + str(k+1) + ": " + str(m)

if __name__ == '__main__':
	main()