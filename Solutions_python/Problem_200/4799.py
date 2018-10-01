def isTidy(number):
	number = str(number)
	l = list(number)
	return l == sorted(l)

def runTidy(s, k):
	for i in range(int(s), 0, -1):
		if isTidy(i):
			print "Case #"+str(k)+": "+str(i)
			return

def run(filename):
	f= open(filename).read().splitlines()

	T = int(f[0])
	for i in range(1, T+1):
		runTidy(f[i], i)



run("B-small-attempt3.in")