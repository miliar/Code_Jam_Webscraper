def one_test():
	def one_table():
		row = int(input()) - 1
		rows = [map(int, input().split()) for i in range(4)]
		return set(rows[row])
	set1 = one_table()
	set2 = one_table()
	res = set1 & set2
	if not res:
		return "Volunteer cheated!"
	elif len(res) > 1:
		return "Bad magician!"
	else:
		return res.pop()

t = int(input())

for i in range(1, t + 1):
	print("Case #{}: {}".format(i, one_test()))
