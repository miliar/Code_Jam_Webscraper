from re import split, compile
import re
from random import randint
from string import ljust,rjust
from sys import argv

def run_file():
	if len(argv)>1:
		filename = argv[1]
	else:
		filename = 'A-large.in'
		filename = 'A-small.in'
	f=file(filename)
	program = f.readlines()
	f.close()
	line_no = 0
	case_no = 0
	word_no = 0
	program_len = len(program)
	first_line = str(program[0]).rstrip().split(' ')
	letters_no = int(first_line[0])
	words_no = int(first_line[1])
	cases_no = int(first_line[2])

	line_no += 1
	words = []
	patterns = []
	while word_no < words_no:
		word = program[line_no].rstrip()
		words.append(word)
		line_no += 1
		word_no += 1
	while case_no < cases_no:
		case = program[line_no].rstrip()
		patterns.append(case)
		line_no += 1
		case_no += 1
	
	case_no = 1
	for pattern in patterns:
		print "Case #" + str(case_no) + ": " + str(analyze(pattern, words))
		case_no +=1
				
def analyze(pattern, words):
	count = 0 
	internal_pattern = re.compile(str(pattern).replace('(', '[').replace(')', ']'))
	for word in words:
		if internal_pattern.match(word):
			count+=1
	
	return count

run_file()