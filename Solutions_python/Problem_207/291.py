import sys
sys.setrecursionlimit(100000)

fin = open("b.in")
fout = open("b.out", "w")
nt = int(fin.readline())

def gen(colors, res):
	colors = sorted(colors, key=lambda x: x[0], reverse=True)
	if sum([color[0] for color in colors]) < 1:
		return res
	if res[-1] != colors[0][1]:
		colors[0][0] -= 1
		res += colors[0][1]
	else:
		if colors[1][0] >= 1:
			colors[1][0] -= 1
			res += colors[1][1]
		else:
			return []
	return gen(colors, res)
	

for tn in xrange(nt):
	fout.write("Case #" + str(tn + 1) + ": ")

	n, r, o, y, g, b, w = (int(i) for i in fin.readline().split())

	colors = [[r, "R"], [y, "Y"], [b, "B"]]
	colors = sorted(colors, key=lambda x: x[0], reverse=True)
	colors[0][0] -= 1
	colors[0][0] += 0.1
	res = gen(colors, [colors[0][1]])

	if (len(res) < n) or ((n > 1) and (res[0] == res[-1])):
		res = "IMPOSSIBLE"
	else:
		res = "".join(res) 

	fout.write(res)
	fout.write("\n")
