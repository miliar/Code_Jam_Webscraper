#!/usr/bin/python3

import sys
import copy

numcase = 0
totalcases = int(sys.stdin.readline().strip())

def getallparents(parents, c):
	if not c in parents:
		return []
	allparents = []
	for p in parents[c]:
		allparents.append(p)
		allparents += getallparents(parents, p)
	return allparents
	

while totalcases>0:
	line = sys.stdin.readline()
	if line == "": break

	numcase += 1
	totalcases -= 1

	numclasses = int(line.strip())

	parents = {}

	for c in range(1, numclasses+1):
		classinfo = sys.stdin.readline().strip().split(' ')
		numparents = classinfo[0]
		parents[c] = []
		for p in classinfo[1:]:
			parents[c].append(int(p))

	hasdiamonds = False

	for c in range(1, numclasses+1):
		if len(parents[c]) < 2: continue
		allparents = getallparents(parents, c)
		reachableparents = {}
		for p in allparents:
			if p in reachableparents:
				hasdiamonds = True
				break
			reachableparents[p] = True

	if hasdiamonds:
		print("Case #%d: Yes" % numcase)
	else:
		print("Case #%d: No" % numcase)
