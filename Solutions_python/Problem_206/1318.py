#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(inp):
	D, N = inp.split()
	D, N = int(D), int(N)
	horses = []
	for i in range(N):
		K, S = input().split()
		K, S = int(K), int(S)
		horses.append((K, S))
	slowest_time = 0
	for horse in horses:
		time = (D - horse[0]) / horse[1]
		if time > slowest_time:
			slowest_time = time
	return "{0:.6f}".format(D / slowest_time)  

				
if __name__ == '__main__':
	testcases = int(input())

	for case in range(testcases):
		inp = input()
		print("Case #{}: {}".format(case+1, main(inp))) 
