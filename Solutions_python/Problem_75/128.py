#!/usr/bin/python

import sys

def initdata():
	compat = []
	for i in range(26):
		compat.append([])
		for j in range(26):
			compat[i].append(-1)


	collide = []
	for i in range(26):
		collide.append([])

	return (compat,collide,[])
	

def solve(cases):
	sols = []

	for case in cases:
		compat = case[0]
		collide = case[1]
		text = case[2]

		ctext = [text[0]]
		was = []
		for i in range(26):
			was.append(0)
		was[text[0]] = 1

		for i in range(1,len(text)):
			cchar = text[i]
			while(len(ctext) != 0 and compat[ctext[-1]][cchar] != -1): 	# Checking for compatibility
				cchar = compat[ctext[-1]][cchar]
				was[ctext[-1]] -= 1
				ctext.pop()
			ctext.append(cchar)
			was[cchar] += 1


			for i in collide[cchar]:				# Checking for collisions
				if was[i] != 0:
					ctext = []
					for i in range(26):
						was[i] = 0
					break

		if len(ctext) == 0:
			sols.append("[]")
		else:
			sol = "[" + chr(ctext[0] + 65)
			for i in range(1,len(ctext)):
				sol += ", " + chr(ctext[i] + 65)
			sol += "]"
			sols.append(sol)

	return sols


f = open(sys.argv[1],'r')
testCount = int(f.readline().strip('\n'))
#print testCount
cases = []
for i in range(testCount):
	case = initdata()
	line = f.readline().strip('\n').split(' ')
#	print "line",line
	p = 0;
	if int(line[p]) != 0:
		compats = int(line[p])
		p += 1
		for i in range(compats):
			a = ord(line[p][0]) - 65
			b = ord(line[p][1]) - 65
			c = ord (line[p][2]) - 65
			case[0][a][b] = c
			case[0][b][a] = c
			p += 1
	else:
		p += 1
	
	
	if int(line[p]) != 0:
		collides = int(line[p])
		p += 1
		for i in range(collides):
			a = ord(line[p][0]) - 65
			b = ord(line[p][1]) - 65
			case[1][a].append(b)
			case[1][b].append(a)
			p += 1
	else:
		p += 1

	
	for i in range(int(line[p])):
		case[2].append(ord(line[p + 1][i]) - 65)

	
#	print "compat",case[0]
#	print "collide",case[1]
#	print "input",case[2]
	cases.append(case)


solution = solve(cases)

for i in range(len(solution)):
	print "Case #" + str(i + 1) + ": " + solution[i]	

	
