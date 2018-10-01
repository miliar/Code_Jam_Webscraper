from math import floor


def solve(line):
	googlers = 3
	surprising_results = line[1]
	p = line[2]
	scores = []
	for i in range(3,len(line)):
		scores.append(line[i])

	p_threshold = p * googlers - (googlers-1)
	lowest_surprise = 0
	if p > 1:
		lowest_surprise = p + (googlers-1)*(p-2)
	else:
		lowest_surprise = p
	
	winners = 0
	for score in scores:
		if score >= p_threshold:
			winners += 1
		elif score >= lowest_surprise and surprising_results > 0:
			surprising_results -= 1
			winners += 1
	
	return str(winners)


def main():
	t = input()

	i = 0
	while i < t:
		i += 1
		line = [int(x) for x in raw_input().split(' ')]	
		print "Case #%d: %s" % (i,solve(line))


if __name__ == '__main__':
	main()