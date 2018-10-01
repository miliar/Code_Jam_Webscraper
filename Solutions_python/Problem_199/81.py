import random
import sys
import time

import itertools
from collections import defaultdict
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import math

from nose.tools import assert_set_equal

import plotting
import primes
from geometry import polygon_area, is_point_left_of_line
from util import read_int_table_file

res_path = "../../../../downloads/"

def solve_line(line):
	s,K = line.split(" ")
	K = int(K)
	x = list(map(lambda it: it == '+', s))
	x = np.array(x)
	a = 0
	counter = 0
	for a in range(len(x)-K+1):
		if x[a] == False:
			x[a:a+K] = np.logical_not(x[a:a+K])
			counter += 1
	if np.all(x):
		return str(counter)
	return "IMPOSSIBLE"

def mymain():
	input_name = "A-large"
	# input_name = "C-large-practice"
	output = open(res_path + input_name + ".out", "w")
	input_lines = open(res_path + input_name + ".in").readlines()
	input_lines = input_lines[1:]
	for i, line in enumerate(input_lines):
		solution = solve_line(line)
		output_line = "Case #{}: {}\n".format(i+1, solution)
		output.writelines(output_line)
		print(output_line, end="")
	
	


if __name__ == "__main__":
	print("starting...")
	start = time.time()
	random.seed(0)
	np.random.seed(0)
	mymain()
	end = time.time()
	print("elapsed time: {:.5f}s".format(end - start))
