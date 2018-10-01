def solve(N, ms):
	count = ms[0]
	eaten1 = 0
	max_eaten = 0
	for i in range(1, len(ms)):
		new_count = ms[i]
		if new_count < count:
			eaten1 += count - new_count
		max_eaten = max(max_eaten, count - new_count)
		count = new_count

	count = ms[0]
	eaten2 = 0
	for i in range(1, len(ms)):
		eaten2 += min(count, max_eaten)
		count = ms[i]
	return str(eaten1) + ' ' + str(eaten2)




from sys import argv, exit

if len(argv) != 3:
	print "Usage: python main.py <input file> <output file>";
	exit(1);

ifile = open(argv[1])
ofile = open(argv[2], "w")

T = int(ifile.readline())

print T

for i in range(1, T+1):
	N = int(ifile.readline().strip());
	ms = [int(s) for s in ifile.readline().strip().split()]

	res = solve(N, ms)

	output = 'Case #' + str(i) + ': ' + res

	print output

	ofile.write(output)
	ofile.write('\n')
