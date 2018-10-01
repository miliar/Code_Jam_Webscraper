#!/usr/bin/env python

def main():
	
	for ii in xrange(int(raw_input())):
		
		[P, K, L] = map(int, raw_input().split(" "))
		
		data = map(int, raw_input().split(" "))
		data.sort()
		data.reverse()
		
#		print data
		
		c = 0
		for i in xrange(len(data)):
			c += data[i] * (i/K + 1)
		
		print "Case #%d: %d" % (ii+1, c)

if __name__ == "__main__":
	main()