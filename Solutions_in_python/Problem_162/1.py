import sys,math

cases = int(raw_input())

def reverse(n):
	rn = str(n)[::-1]
	return int(rn)

def checkIfToBeReversed(n,fn):

	if len(str(n)) == 1: return False

	for i in range(len(str(n))/2):
		tenpow = 10**i


		rn0 = reverse(n)
		rn1 = reverse(n+tenpow)
		#print " n: " + str(n) + " rn0: " + str(rn0)

		#print "rn0: " + str(rn0) + " rn1: " + str(rn1)

		if rn0 > n and rn0 <= fn:
			if rn1 > rn0 and rn1 <= fn:
				return False
		else:
			return False

	return True


for i in range(cases):
	fn = int(raw_input())
	steps = 1
	n = 1

	while n < fn:
		if checkIfToBeReversed(n,fn):
			n = reverse(n)
			#print "reverse! " + str(reverse(n)) + " -> " + str(n)
		else:
			n+=1


		#print n

		steps += 1


	print "Case #" + str(i+1) + ": " + str(steps)


