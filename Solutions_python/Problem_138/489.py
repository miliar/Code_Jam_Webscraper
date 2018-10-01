#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

def parse_input(filename):
	"""
	Parse the input according to the following format

	The first line of the input gives the number of test cases, T. T test cases
	follow. Each test case starts with a line containing a single integer N, the
	number of blocks each player has. Next follows a line containing N
	space-separated real numbers: the masses of Naomi's blocks, in kg. Finally
	there will be a line containing N space-separated real numbers: the masses
	of Ken's blocks, in kg.
	"""
	input_file = open(filename, "r")

	tc_number = int(input_file.readline())
	tc_list = []

	for i in range(tc_number):
		tc = {}
		tc['x'] = i + 1
		tc['weights_number'] = int(input_file.readline())
		tc['naomi_weights'] = [float(x) for x in input_file.readline().split(' ')]
		tc['kenn_weights'] = [float(x) for x in input_file.readline().split(' ')]
		tc_list.append(tc)

	return tc_list

def next_max(v, l):
	"""
	Retrieve the following value that is higher than v in the list l
	"""
	for i in range(len(l)):
		if v < l[i]:
			return l.pop(i)

	return l.pop(0)

def optimal_war(tc):
	"""
	You will loose Naomi
	"""
	weights_number = tc.get('weights_number')
	naomi_weights = tc.get('naomi_weights')
	kenn_weights = tc.get('kenn_weights')

	naomi_weights.sort()
	kenn_weights.sort()

	ow = 0

	while len(naomi_weights):
		naomi_value = naomi_weights.pop(0)
		kenn_value = next_max(naomi_value, kenn_weights)

		if naomi_value > kenn_value:
			ow += 1

	return ow

def deceitful_war(tc):
	"""
	Quite cunny this Naomi
	"""
	weights_number = tc.get('weights_number')
	naomi_weights = tc.get('naomi_weights')[:]
	kenn_weights = tc.get('kenn_weights')[:]

	naomi_weights.sort(reverse=True)
	kenn_weights.sort(reverse=True)

	dw = 0

	while len(naomi_weights):
		kenn_value = kenn_weights.pop(0)

		if naomi_weights[0] > kenn_value:
			dw += 1
			naomi_weights.pop(0)
		else:
			naomi_weights.pop()

	return dw

def main(argv):
	"""
	There is no backstab at war
	"""
	filename = argv[0]
	tc_list = parse_input(filename)

	for tc in tc_list:
		dw = deceitful_war(tc)
		ow = optimal_war(tc)

		print "Case #%i: %i %i" % (tc.get('x'), dw, ow)

if __name__ == "__main__":
	main(sys.argv[1:])
