#!/usr/bin/python
#coding=utf-8
import sys

mega_dict = {}

def is_recycled(x, y):
	num1 = str(x)
	num2 = str(y)
	if len(num1) == len(num2):
		if sorted(num1) == sorted(num2):
			for start in range(1, len(num1)):
				length = len(num1)-start+1
				#for length in range(1, len(num1)-start+1):
					#print num1, num2, "\t", start, length, "\t", (num1[start:start+length] + num1[:start] + num1[start+length:])
				if num2 == num1[start:start+length] + num1[:start] + num1[start+length:]:
					mega_dict[(x, y)] = True
					return True
	mega_dict[(x, y)] = False
	return False

def solve(a, b):
	count = 0
	for i in range(a, b+1):
		for j in range(i+1, b+1):
			if not mega_dict.has_key((i,j)):
				val = is_recycled(i, j)
				if val:
					#print (i, j)
					count += 1
			elif mega_dict[(i,j)]:
				#print (i, j)
				count += 1
			
	return count

if len(sys.argv) < 3:
	print "Uso: %s <input filename> <output filename>" % sys.argv[0]
	sys.exit()
input_filename = sys.argv[1]
output_filename = sys.argv[2]
file = open(input_filename, "r")
output_file = open(output_filename, "w")
cases = int(file.readline())

for case in range(0,cases):
	whole_line = file.readline().split()
	a = int(whole_line[0])
	b = int(whole_line[1])
	match_count = solve(a, b)
	output_file.write('Case #%d: %d\n' % (case+1, match_count))

file.close()
output_file.close()

