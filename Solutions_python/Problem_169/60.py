#!/usr/bin/python3

import sys
from math import fabs
from concurrent.futures import ProcessPoolExecutor

def ans(inputs):
	V, C, Rs, Cs = inputs

	num = len(Rs)
	if num == 1:
		if Cs[0] == C:
			return V / Rs[0]
		else:
			return "IMPOSSIBLE"
	
	if num == 2:
		if Cs[0] == Cs[1] == C:
			return V / (Rs[0] + Rs[1])
		if Cs[0] == C:
			return V / Rs[0]
		if Cs[1] == C:
			return V / Rs[1]
		if Cs[0] < C < Cs[1] or Cs[1] < C < Cs[0]:
			t = [None] * 2
			rate = [None] * 2
			t[0] = fabs(C - Cs[0])
			t[1] = fabs(C - Cs[1])

			max_temp = min(Rs[0] * t[0], Rs[1] * t[1])
			rate[0] = max_temp / (t[0])
			rate[1] = max_temp / (t[1])

			return V / (rate[0] + rate[1])

	return "IMPOSSIBLE"

if __name__ == "__main__":
	lines = int(sys.stdin.readline())

	inputs = []
	for i in range(lines):
		N, V, C = map(float, sys.stdin.readline().split())
		N = int(N)
		Rs = []
		Cs = []
		for i in range(N):
			r, c = map(float, sys.stdin.readline().split())
			Rs.append(r)
			Cs.append(c)

		inputs.append((V, C, Rs, Cs))

	with ProcessPoolExecutor(max_workers = 6) as executor:
			outputs = executor.map(ans, inputs)

	output = list(outputs)
	for i in range(lines):
		print("Case #{0}: {1}".format(str(i+1), output[i]))
