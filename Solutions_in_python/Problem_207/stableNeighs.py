f = open("stableNeighsSmall.in", "r")
new_file = open("stableNeighsSmallSol", "w")
t = int(f.readline())

def stable_arrangement(N, R, O, Y, G, B, V):
	if O == G and G == V and V == 0:
		return brute_force_easy_case(N, R, Y, B)

def brute_force_easy_case(N, R, Y, B):
	if N % 2 == 0:
		half = N/2 + 1
	else:
		half = (N-1)/2 + 1
	if R >= half or Y >= half or B >= half:
		return "IMPOSSIBLE"
	mapping = {0:"R", 1:"Y", 2:"B"}
	answer = []
	currents = [R, Y, B]
	pos_max = currents.index(max(currents))
	answer.append(mapping[pos_max])
	currents[pos_max] -= 1
	old_max_position = pos_max
	next_max_position = pos_max
	for i in range(N-1):
		next_max = -1
		old_max_position = next_max_position
		for j in range(len(currents)):
			if j == old_max_position:
				pass
			else:
				if next_max < currents[j]:
					next_max = currents[j]
					next_max_position = j
		answer.append(mapping[next_max_position])
		currents[next_max_position] -= 1
	return fix_answer("".join(answer))

def test(answer):
	for i in range(len(answer)):
		if not incompatible(answer[i], answer[(i+1) % len(answer)]):
			return False
	return True

def incompatible(i, j):
	incompatible_list = [('B','B'),('R','R'),('Y','Y'),('O','O'),('V','V'),('G','G'),('R','O'),('O','R'), ('R','V'),('V','R'),('Y','O'),('O','Y'),('Y','G'),('G','Y'),('B','G'),('G','B'),('B','V'),('V','B'),('O','G'),('G','O'),('O','V'),('V','O'),('V','G'),('G','V')]
	if (i,j) in incompatible_list:
		return False
	else:
		return True

def fix_answer(answer):
	if test(answer):
		return answer
	print "fixing"
	all_possible_endings = [(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,2,1),(3,1,2)]
	for i,j,k in all_possible_endings:
		if test(answer[:len(answer)-3] + answer[-i] + answer[-j] + answer[-k]):
			return answer[:len(answer)-3] + answer[-i] + answer[-j] + answer[-k]
	return "WTF"
	

for i in range(1,t+1):
	N, R, O, Y, G, B, V = [int(x) for x in f.readline().split(' ')]
	new_file.write("Case #"+str(i)+ ": "+str(stable_arrangement(N, R, O, Y, G, B, V))+"\n")