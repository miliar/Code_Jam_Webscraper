def magic_trick(ans1, ans2, grid1, grid2):
	possibleAns = set(grid1[ans1-1])
	solution = possibleAns & set(grid2[ans2-1])


	if len(solution) == 1:
		return str(list(solution)[0])
	elif len(solution) < 1:
		return "Volunteer cheated!"
	return "Bad magician!"


if __name__ == '__main__':
	T = int(input()) # 1 <= T <= 4

	for x in range(T):
		ans1 = int(input())	# 1 <= first row <= 4
		grid1 = []
		grid2 = []
		for i in range(4):
			grid1.append([int(i) for i in input().split()])

		ans2 = int(input())# 1 <= second row <= 4
		for i in range(4):
			grid2.append([int(i) for i in input().split()])

		print("Case #" + str(x+1) + ": " + magic_trick(ans1, ans2, grid1, grid2))
