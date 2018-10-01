
import sys

lines = list(sys.stdin.readlines())

for index, line in enumerate(lines[1:]):
	values = [int(x) for x in line.split(' ')[1][:-1]]
	total, added = 0, 0
	for j, value in enumerate(values):
		if value > 0 and total < j:
			added += (j - total)
			total += (j - total)
		total += value
	
	print('Case #%d: %d' % (index+1, added))
