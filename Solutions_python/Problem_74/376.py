#!/usr/bin/env python
from sys import stdin
from itertools import *

def answer(data):
	time = 0
	pos = { 'O':1, 'B':1 }
	lastTime = { 'O':0, 'B':0 }

	for robot,newPos in data:
		arriveTime = lastTime[robot] + abs(pos[robot]-newPos)
		time = max(time, arriveTime) + 1

		pos[robot] = newPos
		lastTime[robot] = time

	return time

def cases(s):
	while 1:
		pc = stdin.next().split()[1:]
		yield zip(pc[::2], map(int, pc[1::2]))

if __name__ == '__main__':
	stdin.next()
	for n,case in enumerate(cases(stdin)):
		print "Case #%d: %s" % (n+1, answer(case))
