#!/usr/bin/python
import sys

target="welcome to code jam$"

def ranges(string):
	res = []
	used = []
	total = len(string)
	for tp in range(len(target)-1):
		TC = target[tp]
		if TC in used: continue
		ini = string.find(TC)
		if ini < 0: return []
		while ini >= 0:
			c = 1
			end = ini +1
			while end < total and string[end] == TC:
				c+=1
				end += 1
			res.append((ini,TC,c))
			ini = string.find(TC,end)
		used.append(TC)
	return sorted(res)

def count(r,ini = 0,TC = 0,level=0):
	if target[TC]== '$': return 1
	if ini >= len(r) : return 0 
	total = 0L
	for i in range(ini,len(r)):
		if r[i][1] == target[TC]:
			subproblem = count(r,i+1,TC+1,level+1)
			total += r[i][2]*subproblem
	return total

def process(string):
	r = ranges(string)
	return count(r)
			

number = int(sys.stdin.next())
case = 1
for line in sys.stdin:
	linput = line.strip()
	total = process(linput)
	print "Case #%d: %04d"%(case,total)
	case+=1

