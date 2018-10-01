#! /usr/bin/python

import sys

def print_output(case, answer):
	print("Case #%d: %s"%(case,answer))

def get_case(fd):
	data = []

	for val in range(2):
		number = int(input())
		for x in range(1,5):
			line = input()
			if(x == number):
				data.append(line.split())
	return data

def solve_case(data):
	card = []
	for num in data[0]:
		if num in data[1]:
			card.append(num)

	if(not card):
		return	"Volunteer cheated!"

	if len(card) == 1:
		return card[0]

	return "Bad magician!"
	
fdin = open("input")
T = int(input())
for case in range(1,T+1):
	data = get_case(fdin)
	print_output(case,solve_case(data))