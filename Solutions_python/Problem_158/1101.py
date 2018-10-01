import fileinput
import pdb

def omino(x,r,c):
	if x > 7:
		return "RICHARD"
	if x > max(r,c):
		return "RICHARD"
	if (x + 1) / 2 > min(r,c):
		return "RICHARD"
	if (r*c) % x != 0:
		return "RICHARD"
	if x == 1 or x == 2:
		return "GABRIEL"
	if x == 3:
		return "GABRIEL"
	if x == 4:
		if min(r,c) == 2:
			return "RICHARD"
		else:
			return "GABRIEL"



T = 0
for line in fileinput.input():
	if T == 0:
		T += 1
		continue

	xrc = [int(x) for x in line.split()]
	ans = omino(xrc[0],xrc[1],xrc[2])	
	print "Case #{}: {}".format(T,ans)
	T += 1