

with open('input') as f:
	lines = f.read().split('\n')

items = int(lines[0])

for i in xrange(1, items+1):
	cookies = 0
	rate = 2
	time_elapsed = 0
	factories = 0
	fcost, frate, goal = [float(x) for x in lines[i].split()]
	options = []
	while True:
		time_to_finish = time_elapsed + (goal / rate)
		options.append(time_to_finish)
		time_elapsed += fcost / rate
		rate += frate
		if len(options) > 1 and options[-1] > options[-2]:
			break
	print 'Case #{0}: {1}'.format(i, round(min(options), 7))