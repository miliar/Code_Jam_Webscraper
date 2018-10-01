def rec(l):
	if len(l) <= 1:
		return [l]
	r = []
	for i in range(len(l)):
		r.append(l [i:] + l [:i])
	return r

def isRec(a, b):
	recs = rec(a)
	if b in recs:
		return True
	else:
		return False
	
f = open("C-small-attempt0.in", "r")
w = open("out.txt", "w")

inp = f.readline()
T = int(inp)

for i in range(T):
	
	ans = 0
	inp = f.readline().split()
	A = int(inp [0])
	B = int(inp [1])
	numbers = []
	for j in range(A, B + 1):
		numbers.append(str(j))
	
	for n in numbers:
		for m in numbers:
			if n [0] != '0' and m [0] != '0' and int(n) < int(m) and isRec(n, m):
				ans += 1
	
	w.write("Case #" + str(i + 1) + ": " + str(ans) + "\n")