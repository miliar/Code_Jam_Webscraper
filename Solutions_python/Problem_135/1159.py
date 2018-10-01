#!/usr/bin/env python

input = "A-small-attempt0.in"
with open(input) as f:
	lines = f.read().splitlines();

count = int(lines[0]);
index = 1

f = open('A-small-attempt0.out','w')

for i in range(count):
	first = int(lines[index]);
	first_line = lines[index + first].split(" ");
	index += 5;
	second = int(lines[index]);
	second_line = lines[index + second].split(" ");
	index += 5;
	result = [item for item in first_line if item in second_line]
	
	output = ""
	if (len(result) > 1): 
		output = "Bad magician!"
	elif (len(result) == 0): 
		output = "Volunteer cheated!"
	else: 
		output = result[0]
	
	f.write("Case #{}: {}\n".format(i + 1, output))

f.close()