#!/usr/bin/env python3

import sys
from math import sqrt

def shortest_path(graph, start, target):
	""" Extracted from
http://code.activestate.com/recipes/119466-dijkstras-algorithm-for-shortest-paths/#c1
	Runs in O(m * log(m)) time and takes O(n+m) space.
	"""
	def flatten(l): # Flatten list of the form [0, [1,[2,...]]]
		while len(l):
			yield l[0]
			l = l[1]

	q = [(0, start, ())] # (cost, path_head, path_rest)
	visited = set()
	while True:
		cost, u, path = heapq.heappop(q)
		if u not in visited:
			visited.add(u)
			if u == target:
				return reversed(list(flatten(path))) + [u]
			path = (u, path)
			for v, cost2 in graph[u].iteritems():
				if v not in visited:
					heapq.heappush(q, (cost + cost2, v, path))

def gcd(num1, num2):
	"""
	Returns the greatest common divisor between two numbers
	"""
	return num1 if num2 == 0 else gcd(num2, num1 % num2)

def is_prime(num):
	"""
	Checks if a number is prime.
	Runs in O(\sqrt{n}) time.
	"""
	# Separated in a function so that we don't check even numbers
	def is_prime_odd(num):
		for i in range(3, int(sqrt(num)), step=2):
			if num % i == 0:
				return True
		return False
	return num % 2 == 0 or is_prime_odd(num)

def is_prime_prob(num):
	"""
	Checks if a number is prime using the Fermat test.
	Runs in O(\log{n}) time.
	"""
	pass

def solve(input_data):
	return max(i - sum(input_data[:i], 0) for i in range(len(input_data)))

def read_input():
	line = sys.stdin.readline().split(' ')
	return list(map(int, line[1][:-1])) # Skip \n

if __name__ == '__main__':
	ncases = int(sys.stdin.readline())
	for case in range(1, ncases + 1):
		result = solve(read_input())
		print('Case #', case, ': ', result, sep='')
