#!/usr/bin/python
# -*- coding: utf-8 -*-

H = 0
W = 0

map = []
work = []

def doit():
	global H
	global W
	global map
	global work
	
	input = open("B.in", 'r')
	output = open("B.out", 'w')
	T = int( input.readline().strip() )
	
	i = 1
	
	while i <= T:
		dims = input.readline().split()
		H = int( dims[0] )
		W = int( dims[1] )
		
		map = []
		out = []
		work = []
		
		l=0
		
		while l < H:
			line = input.readline().split()
			tmp1 = []
			tmp2 = []
			
			for alt in line:
				tmp1.append(  int( alt )  )
				tmp2.append(  0  )
			
			map.append( tmp1 )
			out.append( tmp2 )
			work.append( tmp2 )
			
			l = l+1
		
		
		pathfinder()
		output.write("Case #" + str(i) + ":\n" + outputify() )
		
		
		i = i+1
	
	output.close()
	input.close()



def pathfinder():
	global H
	global W
	global map
	global work
	
	i = 0
	val = 1
	
	while i < W*H:
		if work[ i/W ][ i%W ] == 0:
			if step( i/W, i%W, val ) >= val:
				val = val+1
		
		i = i+1



def step( y, x, val ):
	global H
	global W
	global map
	global work
	
	if work[y][x] != 0:		#Already taken sink or fall
		return work[y][x]
	
	next = [ -1, -1, -1, -1 ]
	minimal = 10000
	alt = map[y][x]
	
	if y-1 >= 0:
		next[0] = map[y-1][x]
		minimal = min( minimal, next[0] )
	
	if x-1 >= 0:
		next[1] = map[y][x-1]
		minimal = min( minimal, next[1] )
	
	if x+1 < W:
		next[2] = map[y][x+1]
		minimal = min( minimal, next[2] )
	
	if y+1 < H:
		next[3] = map[y+1][x]
		minimal = min( minimal, next[3] )
	
	if minimal >= alt:	#sink
		work[y][x] = val
		return val
	
	if next[0] == minimal:
		val = step( y-1, x, val )
		work[y][x] = val
		return val
	
	if next[1] == minimal:
		val = step( y, x-1, val )
		work[y][x] = val
		return val
	
	if next[2] == minimal:
		val = step( y, x+1, val )
		work[y][x] = val
		return val
	
	if next[3] == minimal:
		val = step( y+1, x, val )
		work[y][x] = val
		return val



def outputify():
	global H
	global W
	global work
	
	str = ""
	
	for line in work:
		for val in line:
			str = str + chr( val+96 ) + " "
		
		str = str + "\n"
	
	return str


doit()
