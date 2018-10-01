#!/usr/bin/python
import sys
sys.setrecursionlimit(10000)
def cookies(C, F, X, nb_cookies, t, f):
	if (X-C)/f >= X/(f+F):
		return cookies(C, F, X, 0, t+C/f, f+F)
	else:	
		return "%7f"%(t+(X-nb_cookies)/f)

if __name__=="__main__":
	lines = open(sys.argv[1]).read().splitlines()
	nb_case = lines[0]
	i=1
	for l in lines[1:]:
		(C,F,X)=l.split(" ")
		print "Case #%i: %s"%(i, cookies(float(C), float(F), float(X), 0, 0, 2))
		i+=1
