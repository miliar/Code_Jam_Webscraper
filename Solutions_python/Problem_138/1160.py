def unfair_play(log_count, naomi_logs, ken_logs):

	points = 0
	for i in range(int(log_count)):
		if naomi_logs[-1] > ken_logs[-1]:
			# find a log heavier than kens
			for nlog in naomi_logs:
				if nlog > ken_logs[0]: # ken will use his lightest log
					naomi_logs.remove(nlog)
					break
			ken_logs.pop(0)
			points += 1
		else:
			naomi_logs.pop(0)
			ken_logs.pop(-1)
	return points


def fair_play(log_count, naomi_logs, ken_logs):

	k_logs = list(ken_logs) # keep a copy
	points = 0
	for nlog in naomi_logs:
		naomi_win = True
		for klog in k_logs:
			if klog > nlog:
				k_logs.remove(klog)
				naomi_win = False
				break
		if naomi_win:
			points += 1
	return points


def get_best_points(log_count, naomi_logs, ken_logs):

	naomi_logs = sorted([float(log) for log in naomi_logs.split()])
	ken_logs = sorted([float(log) for log in ken_logs.split()])

	return [
		fair_play(log_count, naomi_logs, ken_logs),
		unfair_play(log_count, naomi_logs, ken_logs)
	]


# Get data
file = open('in','r')
data = file.read().splitlines()
file.close()


# Start solving
results = []
test_cases = int(data[0])
for i in range(1, len(data), 3):
	results.append(
		get_best_points(
			data[i],
			data[i + 1],
			data[i + 2]
		)
	)

# print results
file = open('out', 'w')
for i in range(test_cases):
	file.write('Case #' + str(i + 1) + ': ' +
		str(results[i][1]) + ' ' +
		str(results[i][0]) + '\n')
file.close()
