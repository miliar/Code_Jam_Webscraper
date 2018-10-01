import sys
import re

if __name__=="__main__":
	fp = sys.stdin
	s = fp.readline()
	times = int (s)
	for loop in range(0, times):
		s = fp.readline()
		n = int (s)
		arr = []
		for i in range(0, n):
			s = fp.readline()
			s = s.split(' ')
			a = int(s[0])
			b = int(s[1])
			arr.append( (a, b) )
			arr.sort()
		ans = 0
		for i in range(0, n):
			for j in range(i+1, n):
				if arr[i][1] > arr[j][1]:
					ans = ans + 1
		print "Case #%d: %d" %(loop+1, ans)