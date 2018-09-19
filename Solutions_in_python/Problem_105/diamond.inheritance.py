#!/usr/bin/python

import sys

WHITE = 0
BLACK = 1

class Node:
	def __init__(self, neighbours):
		self.color = WHITE
		self.neighbours = neighbours

def DFS(node, graph):
	if graph[node].color == WHITE:
		result = True

		for i, n in enumerate(graph[node].neighbours):
			result = result and DFS(n, graph)

		graph[node].color = BLACK
	else: # BLACK
		result = False

	return result

for tc in xrange(1, int(sys.stdin.readline()) + 1):
	graph = []
	for nodes in xrange(1, int(sys.stdin.readline()) + 1):
		graph.append(Node([int(n) - 1 for n in sys.stdin.readline().split()[1:]]))

	result = True

	for i in xrange(len(graph)):
		for j in xrange(len(graph)):
			graph[j].color = WHITE;

		result = result and DFS(i, graph)

		if not result:
			break;

	if result:
		print "Case #%d: No" % tc
	else:
		print "Case #%d: Yes" % tc
		
