#!/usr/bin/env python

def main():
	size = "small"

	in_file = "in_{}.txt".format(size)
	out_file = "out_{}.txt".format(size)

	f = open(in_file, 'r')
	o = open(out_file, 'w')

	cases = int(f.readline().rstrip())

	for c in range(cases):
		row_number = int(f.readline().rstrip())
		layout = []
		for i in range(4):
			r = map(int, f.readline().rstrip().split())
			layout.append(r)

		row_1 = layout[row_number-1]

		row_number = int(f.readline().rstrip())
		layout = []
		for i in range(4):
			r = map(int, f.readline().rstrip().split())
			layout.append(r)

		row_2 = layout[row_number-1]

		result = None
		card_list = [i for i in row_1 if i in row_2]
		if len(card_list) == 0:
			result = "Volunteer cheated!"
		elif len(card_list) == 1:
			result = card_list[0]
		else:
			result = "Bad magician!"

		o.write("Case #{0}: {1}\n".format(c+1, result))

main()
