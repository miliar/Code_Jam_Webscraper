#! /usr/bin/python

from Queue import *

slots = {}
def updateSlot(slotPos, value):
	if slots.has_key(slotPos):
		slots[slotPos] += value
	else:
		slots[slotPos] = value

T = int(raw_input())

for t in range(1, T+1):

	N, K = [int(inp) for inp in raw_input().split()]
	slots = {}
	slots[N] = 1
	q = Queue()
	q.put(N)
	qMin = N

	while K > 0:
		curSlot = q.get()
		nextSlot = (curSlot - 1)/2
		nextSlotP = curSlot - 1 - nextSlot
		if nextSlotP < qMin:
			q.put(nextSlotP)
			qMin = nextSlotP
		if nextSlot < qMin:
			q.put(nextSlot)
			qMin = nextSlot

		updateSlot(nextSlotP, slots[curSlot])
		updateSlot(nextSlot, slots[curSlot])
		K -= slots[curSlot]

	print 'Case #' + str(t) + ': ' + str(nextSlotP) + ' ' + str(nextSlot)