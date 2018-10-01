# Prepare input
input_file = open ('A-small-attempt1.in')
lines = input_file.read().splitlines()
input_file.close()

lines = filter(None, lines)

# Cases
if len(lines) > 0:
	lines.pop(0)

	for case, line in enumerate(lines):
		line = map(int, list(line.split()[1]))
		invites = 0
		totals = line[0]
		line.pop(0)

		for index, people in enumerate(line):
			if (people) > 0:
				if totals < (index + 1):
					invites += (index + 1) - totals
					totals += invites + people
				else:
					totals += people

		print 'Case #' + str(case + 1) + ': ' + str(invites)

