#! /usr/bin/python

import sys

def convert(hm):
	h, m = map(int, hm.split(":"))
	return h*60 + m

def readCase():
	line = sys.stdin.readline()
	turnaround = int(line.strip())
	na, nb = map(int, sys.stdin.readline().strip().split())
	trips = []
	nt = 0
	while nt < na:
		tleave, tarrive = sys.stdin.readline().strip().split()
		trips.append([convert(tleave), convert(tarrive), "AB"])
		nt += 1
	nt = 0
	while nt < nb:
		tleave, tarrive = sys.stdin.readline().strip().split()
		trips.append([convert(tleave), convert(tarrive), "BA"])
		nt += 1
	def cmp(a, b):
		if a[0] < b[0]:
			return -1
		elif a[0] == b[0]:
			return 0
		else:
			return 1
	trips.sort(cmp)
	return turnaround, trips

def solveCase(turnaround, trips):
	na = 0
	nb = 0
	traina = []
	trainb = []

	def getTrain(candidates, tleave):
		for c in candidates:
			if c <= tleave:
				candidates.remove(c)
				return True
		return False

	for t in trips:
		if t[2] == "AB":
			if not getTrain(traina, t[0]):
				na += 1
			trainb.append(t[1] + turnaround)
			trainb.sort()
		else:
			if not getTrain(trainb, t[0]):
				nb += 1			
			traina.append(t[1] + turnaround)
			traina.sort()
	return na, nb

if __name__ == "__main__":
	line = sys.stdin.readline()
	ncases = int(line.strip())
	nc = 0
	while nc < ncases:
		turnaround, trips = readCase()
		na, nb = solveCase(turnaround, trips)
		print "Case #%d: %d %d" % (nc + 1, na, nb)
		nc += 1
