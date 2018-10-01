#!/usr/bin/python
import psyco
psyco.full()
import string
import re
def read_input():
	file = open("input.in")
	lines = file.readlines()
	file.close()
	return lines

def write_output(lines):
	file = open("output.out", "w")
	file.writelines(lines)
	file.close()

def count_phrase(text, phrase):
	if len(phrase) == 1:
		return text.count(phrase)
	num_found = 0
	while text.find(phrase[0]) >= 0:
		text = text[text.find(phrase[0])+1:]
		num_found += count_phrase(text, phrase[1:])
		num_found %= 10000
	return num_found

if __name__=="__main__":
	#print("reading input")
	input = read_input()
	output = []
	cases = input[1:]
	for (case_num, case) in enumerate(cases):
		text = case[:-1]
		num_found = 0
		print("text: " + text)
		num_found = count_phrase(text, "welcome to code jam")
		output.append("Case #" + str(case_num+1) + ": " + str(num_found).zfill(4) + "\n")
	write_output(output)
