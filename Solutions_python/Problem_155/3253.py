#!/usr/bin/env python

def algo(input_list):
	result_list = input_list[:len(input_list) - 1]
	total = result = pos = 0
	for x in input_list:
		if total < pos:
			result += 1
			total += 1
		total += x
		pos += 1
	return result

input_size = int(raw_input())
f = open('result.out', 'w')
for x in range(input_size):
	case = raw_input()
	case = case.split()
	size = int(case[0])
	items = map(lambda x: int(x), list(case[1]))
	
	if size != len(case):
		pass
	
	result = algo(items)
	status = "Case #" + str(x+1) +  ": " + str(result) + "\n"
	f.write(status)
f.close()
