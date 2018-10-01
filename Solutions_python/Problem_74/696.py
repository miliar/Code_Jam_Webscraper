#!/usr/bin/env python

import sys

def compute_time(cur_pos, next_pos):
	return abs(int(cur_pos) - int(next_pos)) + 1

def solve(c):
	words = c.split()
	n = words[0]
	l = []
	for i in range(1, len(words), 2):
		l.append((words[i], words[i+1]))

	o_pos = 1
	b_pos = 1
	cur_o_time = 0
	cur_b_time = 0

	for i in range(0, len(l)):
		next, next_pos = l[i]
		if next == 'O':
			t = compute_time(o_pos, next_pos)
			o_pos = next_pos
			cur_o_time += t
			if cur_o_time <= cur_b_time:
				cur_o_time = cur_b_time + 1
			#print 'O cur_pos: %s, cur_o_time: %d' % (o_pos, cur_o_time)
		else:
			t = compute_time(b_pos, next_pos)
			b_pos = next_pos
			cur_b_time += t
			if cur_b_time <= cur_o_time:
				cur_b_time = cur_o_time + 1
			#print 'B cur_pos: %s, cur_b_time: %d' % (b_pos, cur_b_time)
	
	return max(cur_o_time, cur_b_time)

if __name__ == '__main__':
	lines = open(sys.argv[1]).readlines()
	tests = int(lines[0].strip())
	start = 1
	idx = start
	for i in range(start, tests+start):
		tc = lines[i].strip()
		n = solve(tc)
		print 'Case #%d: %d' % (i, n)
