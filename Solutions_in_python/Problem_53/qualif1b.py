def switch(n, k):
	l = [1] #First virtual snapper : the power. always on.
	x = xrange(0, n)

	for i in x:
		l.append((k/2**i)%2) #Well, that's "maths". Writing the sequence helps to understand, the alternance is logical so it's not needed to make an iterative algorithm in fact.

	for i in x:
		if not l[i+1]: #If a snapper is off in the chain, light is off.
			return False
	return True

if __name__ == '__main__':
	N = int(raw_input())
	for i in range(1, N+1):
		n, k = (int(j) for j in raw_input().split())
		print "Case #%d: %s" % (i, switch(n, k) and "ON" or "OFF")
