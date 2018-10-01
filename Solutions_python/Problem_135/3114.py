import sys

def solve():
	l1 = int(raw_input()) - 1
	inp1 = [ raw_input() for x in range(4) ][l1].split(' ')
	l2 = int(raw_input()) - 1
	inp2 = [ raw_input() for x in range(4) ][l2].split(' ')
	pos = [x for x in inp1 if x in inp2]
	if len(pos) == 1:
		return pos[0]
	if len(pos) == 0:
		return "Volunteer cheated!"
	return "Bad magician!"

probs = int(raw_input())
for i in range(probs):
	result = solve()
	print ("Case #%d: " % (i+1)) + result