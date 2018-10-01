#!/usr/bin/python

import sys

answer = 0
welcome_text = 'welcome to code jam'

def convert_answer(answer):
	answer = str(answer)
	zero_to_add = 4 - len(answer)
	answer = answer[-4:]
	for x in range(0, zero_to_add):
		answer = '0' + answer
	return answer

def find_text(entry, to_found):
	global answer

	# optimization
	if (len(entry) < len(to_found)):
		return

	found_at = []
	for i in range(len(entry)):
		if entry[i] == to_found[0]:
			found_at.append(i)

	# nothing, stop here
	if len(found_at) == 0:
		return

	# we found something and there was only one letter
	# so it's done
	if len(to_found) == 1:
		answer += len(found_at)
		return

	for x in found_at:
		find_text(entry[x+1:], to_found[1:])

# main function
# write code from here
def process(input, output):
	global answer
	nb = int(input.readline())

	for x in range(1, nb+1):
		answer = 0
		text = input.readline().rstrip()
		find_text(text, welcome_text)
		output.write('Case #%d: %s\n' %(x, convert_answer(answer)))

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "Need file as argument"
		sys.exit(1)

	input_file = sys.argv[1]

	# open files
	input_handler = open(input_file, 'r')
	output_handler = open(input_file + '.out', 'w+')

	process(input_handler, output_handler)

	# close files
	input_handler.close()
	output_handler.close()	
