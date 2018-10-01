 #!/usr/bin/python
"""
fairandsquare.py

google code jam C

Date: April 13, 2013
"""
# Imports
import sys, os, math

__version__ = "0.0"
__copyright__ = "CopyRight (C) 2012-13 by Coding Assassin"
__license__ = "MIT"
__author__ = "Coding Assassin"
__author_email__ = "Coding Assassin, codingassassin@gmail.com"

USAGE = "%prog [options]"
VERSION = "%prog v" + __version__

AGENT = "%s/%s" % (__name__, __version__)

def isPalindrome(x):
	if str(x) == str(x)[::-1]:
		return True
	else:
		return False

def main():
	w = open("output.txt", 'w')
	f = open("workfile.txt", 'r')
	T = int(f.readline())
	
	for case in range(T):
		buff = f.readline().rstrip().split()
		A = float(buff[0])
		B = float(buff[1])
		
		sqrta = math.sqrt(A)
		sqrtb = math.sqrt(B)
		
		if int(sqrta)**2 < A:
			sqrta = int(sqrta)+1
		else:
			sqrta = int(sqrta)
		
			
		if int(sqrtb)**2 > B:
			sqrtb = int(sqrtb)-1
		else:
			sqrtb = int(sqrtb)
		
		numPalins = 0
		for i in range(sqrtb-sqrta+1):
			num = i + sqrta
			fas = False
			if isPalindrome(num) and isPalindrome(num**2):
				fas = True
			if fas:
				numPalins += 1
		w.write("Case #"+str(case+1)+": "+str(numPalins)+"\n")
		print "Case #"+str(case+1)+": "+str(numPalins)
			
	
	f.close()
	w.close()

if __name__ == '__main__':
	main() 