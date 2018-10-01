in_file = open("input.txt", "r")
out_file = open("output.txt", "w")


def solve():
	n = int(in_file.readline())
	for t in range(1, n + 1):
		out_file.write("Case #" + str(t) + ": ")
		(s, k) = in_file.readline().split()
		k = int(k)
		a = []
		for x in s:
			if x == '-':
				a.append(0)
			else:
				a.append(1)
		x = 0
		st = []
		l = 0
		for i in range(len(a) - k + 1):
			if l < len(st) and st[l] == i:
				x -= 1
				l += 1
			if (a[i] + x) % 2 == 1:
				continue
			st.append(i + k)
			x += 1
		fail = False
		for i in range(len(a) - k + 1, len(a)):
			if l < len(st) and st[l] == i:
				x -= 1
				l += 1
			if (a[i] + x) % 2 == 0:
				fail = True
				break
		if fail:
			out_file.write("IMPOSSIBLE")
		else:
			out_file.write(str(len(st)))
		out_file.write("\n")


solve()

in_file.close()
out_file.close()
