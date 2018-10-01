from itertools import islice

in_path = r"C:\Users\Chris\Downloads\A-small-attempt0.in"
out_path = r"C:\Users\Chris\Desktop\A-small-output.out"

def solve(data):
	answer1, answer2 = int(data[0]), int(data[5]) + 5
	row1 = { int(card) for card in data[answer1].split() }
	row2 = { int(card) for card in data[answer2].split() }

	intersect = row1 & row2
	n = len(intersect)

	if n == 0:
		return "Volunteer cheated!"
	elif n == 1:
		return intersect.pop()
	else:
		return "Bad magician!"


with open(in_path) as infile, open(out_path, "w") as outfile:
	cases = int(infile.readline())

	for i in xrange(1, cases + 1):
		data = list(islice(infile, 10))
		outfile.write("Case #{0}: {1}\n".format(i, solve(data)))