import sys

input_file = sys.stdin
output_file = sys.stdout

t = int(input_file.readline().strip())

for i in range(t):
	n = int(input_file.readline().strip())
	line = input_file.readline().split()

	in_place = 0
	for j in range(n):
		if j + 1 == int(line[j]):
			in_place += 1

	output_file.write("Case #" + str(i + 1) + ": " + str(n - in_place) + ".000000\n")
