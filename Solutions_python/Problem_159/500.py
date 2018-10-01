def mush(mushroms, case_num):
	# first start
	first = 0
	prev = -1
	for i, v in enumerate(mushroms):
		if prev > v:	
			first += prev - v
		prev = v
	# second start
	second = 0
	rate = 0
	l = len(mushroms)
	for i in range(1, l):
		rate = max(rate, mushroms[i-1]-mushroms[i])
	for i, v in enumerate(mushroms):
		if i != l - 1:
			second += min(v, rate)
	return "Case #{}: {} {}".format(case_num, first, second)


if __name__ == '__main__':
	case_num = 1
	f = open('input.txt', 'r')
	for i, line in enumerate(f):
		if i == 0 or i % 2 == 1:
			continue
		print mush([int(i) for i in line.split(" ")], case_num)
		case_num += 1
	f.close()