import math

f = open('/Users/lhespanha/Documents/projects/personal/gcj2013/problemC.in','r')

def palindrome(L):
    return L == L[::-1]

cases = int(f.readline())
n = 0
while (n < cases):
	line = f.readline().split()
	count = 0
	for x in range(int(line[0]), int(line[1])+1 ):
		val = math.sqrt(x)
		if (val % 1 == 0) and palindrome(str(x)) and palindrome(str(int(val))):
			count = count + 1
	print "Case #%s: %s" % (str(n+1), count)
	n = n + 1