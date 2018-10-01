import math
T = int(raw_input())
for case in xrange(T):
	D = int(raw_input())
	P = [int(i) for i in raw_input().split()]
	best_moves = -1
	for target in xrange(1,max(P)+1):
		biggest = 0
		moves = 0
		for p_i in P:
			current_move = int(math.ceil(float(p_i) / target)) - 1
			biggest = max(biggest, math.ceil(float(p_i) / (current_move + 1)))
			moves += current_move
		moves += biggest
		if best_moves == -1 or best_moves > moves:
			best_moves = moves
	print "Case #%d: %d" % (case+1, best_moves)