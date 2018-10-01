fp_r = open('a.in', 'r')
fp_w = open('a.out', 'w')
t = int(fp_r.readline())

dx = [0, 1, -1, 0, 1, 1, -1, -1]
dy = [1, 0, 0, -1, 1, -1, 1, -1]

for i in range(0, t, 1):
	data = fp_r.readline()
	arr = data.split()

	n = int(arr[0])
	m = int(arr[1])

	board = []
	rotate = []
	for j in range(0, n, 1):
		row = fp_r.readline()
		arr = []
		for k in range(0, n, 1):			
			arr.append(row[k:k+1])
		board.append(arr)
		arr2 = arr[:]
		rotate.append(arr2)

	for j in range(0, n, 1):
		for k in range(0, n, 1):
			if board[j][k] == ".":
				rotate[k][n-j-1] = "."
			if board[j][k] == "R":
				rotate[k][n-j-1] = "R"
			if board[j][k] == "B":
				rotate[k][n-j-1] = "B"

	for l in range(0, n, 1):
		for j in range(n - 1, 0, -1):
			for k in range(0, n, 1):
				if rotate[j][k] == ".":
					rotate[j][k] = rotate[j-1][k]
					rotate[j-1][k] = "."

	rr = 0
	bb = 0
	for j in range(0, n, 1):
		for k in range(0, n, 1):
			if rotate[j][k] != ".":
				for a in range(0, 8, 1):
					f = 1
					for b in range(0, m, 1):						
						if j + dx[a] * b < 0 or k + dy[a] * b < 0 or j + dx[a] * b >= n or k + dy[a] * b >= n or rotate[j + dx[a] * b][k + dy[a] * b] != rotate[j][k]:
							f = 0
							break

					if f == 1 and rotate[j][k] == "R":
						rr = 1
					if f == 1 and rotate[j][k] == "B":
						bb = 1
			
	if rr == 1 and bb == 1:
		fp_w.write("Case #" + str(i+1)+ ": Both\n")
	elif rr == 1:
		fp_w.write("Case #" + str(i+1)+ ": Red\n")
	elif bb == 1:
		fp_w.write("Case #" + str(i+1)+ ": Blue\n")
	else:
		fp_w.write("Case #" + str(i+1)+ ": Neither\n")