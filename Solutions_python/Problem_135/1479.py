import sys
import math
T = int(sys.stdin.readline())

def main():
	for case in range(1,T+1):
		res = solve(case)
		sys.stdout.write("Case #{}: {}\n".format(case, res));

def solve(case):
	row1 =  int(sys.stdin.readline())-1
	grid1 = []
	for row in range(0,4):
		grid1.append(map(int, sys.stdin.readline().split()))
	row2 =  int(sys.stdin.readline())-1
	grid2 = []
	for row in range(0,4):
		grid2.append(map(int, sys.stdin.readline().split()))

	cards = list(set(grid1[row1]).intersection(grid2[row2]))

	if len(cards) == 1:
		return cards[0]
	elif len(cards) == 0:
		return "Volunteer cheated!"
	else: 
		return "Bad magician!"


main()


