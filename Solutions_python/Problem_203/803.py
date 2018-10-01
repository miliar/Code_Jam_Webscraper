#!/usr/bin/python

R = 0
C = 0
cakes = []

def check_clear(lt_x, lt_y, rb_x, rb_y, initial):
	if lt_x < 0 or lt_y < 0 or rb_x >= R or rb_y >= C:
		return False

	for i in range(lt_x, rb_x + 1):
		for j in range(lt_y, rb_y + 1):
			if cakes[i][j] != '?' and cakes[i][j] != initial:
				return False
	return True

def fill_cake(lt_x, lt_y, rb_x, rb_y, initial):
	for i in range(lt_x, rb_x + 1):
		for j in range(lt_y, rb_y + 1):
			cakes[i][j] = initial

def infection(r, c):
	initial = cakes[r][c]
	lt_x, lt_y = r, c
	rb_x, rb_y = r, c
	# top
	while True:
		if check_clear(lt_x - 1, lt_y, rb_x, rb_y, initial):
			lt_x -= 1
		else:
			break
	# right
	while True:
		if check_clear(lt_x, lt_y, rb_x, rb_y + 1, initial):
			rb_y += 1
		else:
			break
	# bottom
	while True:
		if check_clear(lt_x, lt_y, rb_x + 1, rb_y, initial):
			rb_x += 1
		else:
			break
	# left
	while True:
		if check_clear(lt_x, lt_y - 1, rb_x, rb_y, initial):
			lt_y -= 1
		else:
			break
	fill_cake(lt_x, lt_y, rb_x, rb_y, initial)

def print_cake():
	for row in cakes:
		print ''.join(row)

for tc in xrange(1, int(raw_input()) + 1):
	R, C = map(int, raw_input().split())
	cakes = []
	initials = []
	locations = {}
	for i in range(R):
		pieces = list(raw_input())
		for j, initial in enumerate(pieces):
			if initial != '?' and initial not in initials:
				initials.append(initial)
				locations[initial] = (i, j)
		cakes.append(pieces)
	for initial in initials:
		infection(locations[initial][0], locations[initial][1])
	
	print 'Case #%d:' % (tc)
	print_cake()
