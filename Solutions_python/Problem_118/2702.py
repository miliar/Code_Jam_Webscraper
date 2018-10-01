
from math import *

def reverseNum(n, p=0):
    if n == 0:
        return p
    return reverseNum(n/10, p*10 + n%10)

def isPalindrome(n):
	return n == reverseNum(n)

r = open("C-small-attempt1.in", 'r')
w = open("C-small.out", 'w')

n = int(r.readline()) # num cases

for tc in range(n):
	args = r.readline().strip().split()
	low = int(args[0])
	high = int(args[1])

	if low > high:
		temp = low
		low = high
		high = temp

	numSquares = 0

	lowSquare = int(ceil(sqrt(low)))
	highSquare = int(sqrt(high))

	for sq in range(highSquare, lowSquare-1, -1):
		if isPalindrome(sq*sq) and isPalindrome(sq):
			#print("sq: "+str(sq)+" "+str(sq*sq))
			numSquares += 1

	w.write("Case #"+str(tc+1)+": "+str(numSquares)+"\n")

w.close()
r.close()

