#!/usr/bin/python

def precompute(capacity, groups, people):
	packing = [[0, 0],]*groups
	pointer = 0
	for i in range(groups):
		pointer = i
		total = 0
		while (total + people[i]) <= capacity:
			total += people[i]
			i += 1
			if i >= groups:
				i = 0
			if i == pointer:
				break
		packing[pointer] = [total, i]
	return packing

def coaster(rides, capacity, groups, people):
	pointer = 0
	income = 0
	if groups < 1:
		return income
	packing = precompute(capacity, groups, people)
	while rides > 0:
		if packing[pointer][0] == 0:
			return income
		income += packing[pointer][0]
		pointer = packing[pointer][1]
		rides -= 1
	return income

def rl():
	return sys.stdin.readline().strip()

import sys
cases = int(rl())
for case in range(1, cases+1):
	rides, cap, groups = [int(x) for x in rl().split(' ')]
	people = [int(x) for x in rl().split(' ')]
	if len(people) != groups:
		raise Exception('Wrong input')
	print 'Case #%s: %s' % (case, coaster(rides, cap, groups, people))
	
