#!/usr/bin/pypy
import math

def square_root_bound(limit):
	return int(math.sqrt(limit))
	
def expand(guess_bound):
	origin = list(str(guess_bound))
	reverse = list(str(guess_bound))
	reverse.reverse()
	if len(origin) % 2 == 0:
		origin = origin[:-1]
	origin.extend(reverse)
	return int("".join(origin))

def satisfy(start,candidate):
	power = candidate*candidate
	if start > power:
		return False
	origin = list(str(power))
	reverse = list(str(power))
	reverse.reverse()
	for i in range(0,len(origin)):
		if origin[i] == reverse[i]:
			continue
		else:
			return False
	
	return True

def solve(start,limit):
	limit = square_root_bound(limit)
	
	counter = 0;
	for i in range(1,min(10,limit+1)):
		if satisfy(start,i):
			counter += 1
			
	guess_bound = int(math.ceil(float(len(str(limit)))/2))
	guess_bound=int("".join(list(str(limit))[:guess_bound]))
	for i in range(1,guess_bound+1):
		candidate = expand(i)
		if candidate > limit:
			continue
		if satisfy(start,candidate):
			counter += 1
		
	return counter
	
def T(file):
	return int(file.readline()[:-1])

def LIMIT(file):
	tuple = file.readline()[:-1].split(" ")
	return (int(tuple[0]),int(tuple[1]))
	
def line(file,content):
	file.write("%s\n" % content)
	
if __name__ == '__main__':
	import sys
	#file=open("test3.txt","r")
	#out=sys.stdout
	file = open("C:\Users\Zizon\Downloads\C-small-attempt0.in","r")
	out = open("result","w")
	for case in range(1,T(file)+1):
		start,limit = LIMIT(file)
		line(out,"Case #%s: %s" % (case,solve(start,limit)))
	file.close()
	out.close()