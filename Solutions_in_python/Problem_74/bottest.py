#!/usr/bin/python

import sys

def do_case(case, nstep, steps):
	botpos = { 'O': 1, 'B': 1 }
	total_time = 0

	last_bot = None
	last_time = 0

	while len(steps):
		bot = steps.pop()
		pos = long(steps.pop())
#		print "%s %s" % (bot, pos)
		this_time = 0

		if last_bot is None:
			this_time = abs(pos-botpos[bot]) + 1
			last_bot = bot
#			print this_time
		else:
			this_time = abs(pos-botpos[bot]) + 1
			if last_bot != bot:
				this_time -= last_time
				if this_time < 1:
					this_time = 1
#			print this_time

		if last_bot == bot:
			last_time += this_time
		else:
			last_time = this_time

		botpos[bot] = pos
		total_time += this_time
		last_bot = bot

	print 'Case #%d: %d' % (case, total_time)

data_lines = sys.stdin.read().splitlines()
data_lines.reverse()
data_lines.pop()

case = 1
while len(data_lines):
#	print data_lines[len(data_lines)-1]
	line_data = data_lines.pop().split(' ')
	line_data.reverse()
	nstep = long(line_data.pop())
	do_case(case, nstep, line_data)
	case += 1
#	break
