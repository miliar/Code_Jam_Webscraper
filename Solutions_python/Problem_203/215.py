#debug 
def pr(*a):
	#return
	for x in a: print x,
	print
	
def firstLetter(s):
	for i in range(len(s)):
		if s[i] != "?":
			return s[i]
	return None

def solve(R, C, rows):
	g = [["?"]*C for i in range(R)]
	for i in range(R):
		s = rows[i]
		letter = firstLetter(s)
		if not letter:
			g[i] = None
			continue
		g[i][0] = letter
		for j in range(1, C):
			if s[j]=="?":
				g[i][j] = g[i][j-1]
			else:
				g[i][j] = s[j]
	firstRow = -1
	for i in range(R):
		if g[i]:
			if i != 0:
				g[0] = g[i]
			break
	for i in range(1,R):
		if not g[i]:
			g[i] = g[i-1]
	ret = []
	for row in g:
		ret.append("".join(row))
	return "\n" + "\n".join(ret)
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	R, C = f.readline().strip().split()
	R, C = int(R), int(C)
	rows = []
	for i in range(R):
		rows.append(f.readline().strip())
	rt = solve(R,C,rows)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()