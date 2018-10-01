import random
import time

import networkx as nx
import numpy as np

res_path = "../../../../downloads/"

def solve(N,M,lines):
	towers = np.zeros((N,N), dtype=np.bool)
	bishops = np.zeros((N, N), dtype=np.bool)
	changed = np.zeros((N, N), dtype=np.bool)
	free_tower_xs = set(range(N))
	free_tower_ys = set(range(N))
	bishop_vertices1 = set(range(2*N-1))
	bishop_vertices2 = set(range(-2*N+1, 0))
	for line in lines:
		c,y,x = line.split()
		x,y = int(x)-1, int(y)-1
		if c == "+" or c=="o":
			bishops[y,x] = True
			bishop_vertices1.remove(y+x)
			bishop_vertices2.remove(x-y-N)
		if c == "x" or c == "o":
			towers[y, x] = True
			free_tower_xs.remove(x)
			free_tower_ys.remove(y)
	for x,y in zip(free_tower_xs, free_tower_ys):
		towers[y,x] = True
		changed[y,x] = True
	G = nx.Graph()
	G.add_nodes_from(sorted(bishop_vertices1), bipartite=0)
	G.add_nodes_from(sorted(bishop_vertices2), bipartite=1)
	for x in range(N):
		for y in range(N):
			a = x+y
			b = x-y-N
			if a in bishop_vertices1 and b in bishop_vertices2:
				G.add_edge(a,b)
	matching = nx.algorithms.bipartite.matching.maximum_matching(G)
	for a,b in matching.items():
		if a < 0:
			continue
		x = (a+b+N)//2
		y = a-x
		bishops[y,x] = True
		changed[y,x] = True
	# grid = [["."] * N for _ in range(N)]
	# for x in range(N):
	# 	for y in range(N):
	# 		if bishops[y,x] and towers[y,x]:
	# 			grid[y][x] = "o"
	# 		elif bishops[y, x]:
	# 			grid[y][x] = "+"
	# 		elif towers[y, x]:
	# 			grid[y][x] = "x"
	# for line in grid:
	# 	print("".join(line))
	change_count = np.sum(changed)
	style_points = np.sum(towers) + np.sum(bishops)
	total = towers*2 + bishops
	output = "{} {}".format(style_points, change_count)
	for x in range(N):
		for y in range(N):
			i = total[y,x]
			if i > 0 and changed[y,x]:
				output = output + "\n{} {} {}".format(["+","x","o"][i-1], y+1, x+1)
	return output
	
	
	
	

def mymain():
	input_name = "D-large"
	output = open(res_path + input_name + ".out", "w")
	input_lines = open(res_path + input_name + ".in").readlines()
	input_lines = [line.strip() for line in input_lines]
	T = int(input_lines[0])
	input_lines = input_lines[1:]
	for test_case in range(1,T+1):
		N,M = map(int, input_lines[0].split())
		solution = solve(N,M, input_lines[1:M+1])
		input_lines = input_lines[M+1:]
		output_line = "Case #{}: {}\n".format(test_case, solution)
		output.writelines(output_line)
		print(output_line.splitlines()[0], end="\n", flush=True)
	
	


if __name__ == "__main__":
	print("starting...")
	start = time.time()
	random.seed(0)
	np.random.seed(0)
	mymain()
	end = time.time()
	print("elapsed time: {:.5f}s".format(end - start))
