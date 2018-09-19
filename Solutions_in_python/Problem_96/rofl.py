f = open("B-large.in", "r")
w = open("out.txt", "w")

inp = f.readline()
T = int(inp)

for i in range(T):
	
	ans = 0
	totalScores = []
	inp = f.readline().split()
	N = int(inp [0])
	S = int(inp [1])
	p = int(inp [2])
	for j in range(N):
		totalScores.append(int(inp [3 + j]));
	totalScores.sort()
	totalScores.reverse()
	
	for j in range(N):
		Score = totalScores [j]
		if 2 * (p - 2) + p > Score or p > Score:
			break
		elif 2 * (p - 1) + p <= Score:
			ans += 1
		elif  S > 0 and 2 * (p - 2) <= Score:
			ans += 1
			S -= 1
			
	w.write("Case #" + str(i + 1) + ": " + str(ans) + "\n")