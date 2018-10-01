#!/usr/bin/python

import string
import re
import sys

DBG = 0

line = raw_input()
T = int(line)

for i in range(0, T):
	(h, w) = raw_input().split(' ', 2)
	h, w = int(h), int(w)
	level = []
	for j in range(0, h):
		level.append([{'v' : int(x), 't' : '*'} for x in raw_input().split(' ', w)])
	
	#RMME
	if DBG > 1:
		print 'level:'
		for lvl in level:
			line = ''
			for pole in lvl:
				line = line + str(pole['v'])
			line += '\t'
			for pole in lvl:
				line = line + pole['t']
			print line

	#na poczatek oznacz pola duza litera a potem zaczynajac od North-West oznaczaj kolejno malymi
	letters = string.letters.upper()
	lind = 0#aktualny indeks litery w letters
	end = False
	while not end:
		if DBG > 1: print '-' * 78
		end = True
		for y in range(0, h):
			for x in range(0, w):
				if DBG > 1: print 'checking: (', y,',', x, ') =', level[y][x], '...'
				if level[y][x]['t'] == '*':
					end = False
					fallto = -1#where water falls from this (x, y)
					smallest = {'v' : 999999}

					yy, xx = y + 1, x
					if yy < h:
						if DBG > 1: print '\tchecking South'
						if level[yy][xx]['v'] < level[y][x]['v'] and level[yy][xx]['v'] <= smallest['v']:
							fallto = 3#fall to South
							smallest = level[yy][xx]
							if DBG > 1: print '\t\tsmallest (', yy,',', xx, ') =', level[yy][xx]

					yy, xx = y, x + 1
					if xx < w:
						if DBG > 1: print '\tchecking East'
						if level[yy][xx]['v'] < level[y][x]['v'] and level[yy][xx]['v'] <= smallest['v']:
							fallto = 2#fall to East
							smallest = level[yy][xx]
							if DBG > 1: print '\t\tsmallest (', yy,',', xx, ') =', level[yy][xx]

					yy, xx = y, x - 1
					if xx >= 0:
						if DBG > 1: print '\tchecking West'
						if level[yy][xx]['v'] < level[y][x]['v'] and level[yy][xx]['v'] <= smallest['v']:
							fallto = 1#fall to West
							smallest = level[yy][xx]
							if DBG > 1: print '\t\tsmallest (', yy,',', xx, ') =', level[yy][xx]

					yy, xx = y - 1, x
					if yy >= 0:
						if DBG > 1: print '\tchecking North'
						if level[yy][xx]['v'] < level[y][x]['v'] and level[yy][xx]['v'] <= smallest['v']:
							fallto = 0#fall to North
							smallest = level[yy][xx]
							if DBG > 1: print '\t\tsmallest (', yy,',', xx, ') =', level[yy][xx]

					if fallto == -1:#sink
						level[y][x]['t'] = letters[lind]
						lind += 1
						if DBG > 1: print '\tis sink : set letter', level[y][x]['t']
					elif smallest['v'] < 999999 and smallest['t'] != '*':
						if DBG > 1: print '\tis not sink : set letter', smallest['t']
						level[y][x]['t'] = smallest['t']

		if DBG > 1:
			print '-' * 78
			print 'level:'
			for lvl in level:
				line = ''
				for pole in lvl:
					line = line + str(pole['v'])
				line += '\t'
				for pole in lvl:
					line = line + pole['t']
				print line

	if DBG:
		print '-' * 78
		print 'level:'
		for lvl in level:
			line = ''
			for pole in lvl:
				line = line + str(pole['v'])
			line += '\t'
			for pole in lvl:
				line = line + pole['t']
			print line


	# oznacz pola malymi literami od North-West
	letters = string.letters
	lind = 0
	conv = {}
	for y in range(0, h):
		for x in range(0, w):
			if not level[y][x]['t'] in conv:
				conv[ level[y][x]['t'] ] = letters[lind]
				level[y][x]['t'] = letters[lind]
				lind += 1
			else:
				level[y][x]['t'] = conv[ level[y][x]['t'] ]


	print 'Case #%d:' % (i + 1, )
	for lvl in level:
		print ' '.join([p['t'] for p in lvl])
