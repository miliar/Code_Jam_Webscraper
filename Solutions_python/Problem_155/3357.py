#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

input_path = sys.argv[1]
output_path = sys.argv[2]

def do_algorithm(test_idx, input_file, output_file):
	aud_dic = dict()	# key: shyness, value: audience

	# fill aud_dic	
	line = input_file.readline()
	arr = line.split()

	aud_cnt = int(arr[0]) + 1
	aud_defs = arr[1]
	for i in range(aud_cnt):
		aud_dic[i] = int(aud_defs[i])

	shyness_aud_cnt = 0
	add_aud_cnt = 0

	for i in range(aud_cnt):
		cur_aud_cnt = shyness_aud_cnt + add_aud_cnt
		if cur_aud_cnt < i:
			add_aud_cnt += (i - cur_aud_cnt)

		shyness_aud_cnt += aud_dic[i]

	output_file.write('Case #%d: %d\n' % (test_idx, add_aud_cnt))

try:
	input_file = open(input_path, 'r')
	output_file = open(output_path, 'w')

	test_num  = int(input_file.readline())
	for i in range(test_num):
		do_algorithm(i+1, input_file, output_file)

	input_file.close()
	output_file.close()
except Exception as e:
	print str(e)
	sys.exit(-1)
