#!/usr/bin/env python2.7


import sys
import math


MAX_M = 200
CASE_NUM = 0

def read_data(filename = ''):
	global CASE_NUM

	input_f = sys.stdin
	if filename != '':
		input_f = open(filename,'r')

	#data which used by handle_data()
	input_fun1_l = []
	
	CASE_NUM = int(input_f.readline())
	
	#case init data
	for case in range(0,CASE_NUM):
		#case data sets init
		# data_count = int(input_f.readline())
		matrix = []
		#case depends

		matrix.append(int(input_f.readline()))
		
		for i in range(4):
			line = input_f.readline()
			parts = line.strip().split()
			matrix.append(parts)

		matrix.append(int(input_f.readline()))
		
		for i in range(4):
			line = input_f.readline()
			parts = line.split()
			matrix.append(parts)

		#for every case if there are few datas
		
		#add to result set
		input_fun1_l.append(matrix)

	input_f.close()
	return input_fun1_l


def write_data(result_l,filename = ''):
	global CASE_NUM
	output_f = sys.stdout
	if filename != '':
		output_f = open(filename,'w')
	for i in range(0,CASE_NUM):
		output_f.write(('Case #%d: ' % (i+1) )+ str(result_l[i])+ '\n')
	
	output_f.close()
	return


def handle_data(matrix_arr):
	result_l = []
	for matrix in matrix_arr:
		result_l.append(magic_trick(matrix))
	return result_l


def magic_trick(datas):
	row1 = datas[0]
	row2 = datas[5] + 5
	num = []
	for num1 in datas[row1]:
		for num2 in datas[row2]:
			if num1 == num2:
				num.append(num1)
	if len(num) == 1:
		return num[0]
	elif len(num) == 0:
		return "Volunteer cheated!"
	else:
		return "Bad magician!"



if __name__ == '__main__':
	matrix_arr = read_data('A-small-attempt1.in')
	result_l = handle_data(matrix_arr)
	write_data(result_l,'A-small-attempt1.out')