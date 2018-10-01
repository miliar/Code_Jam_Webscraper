def isTidy(input_num, length):
    for i in xrange(1, length):
        if input_num[i - 1] > input_num[i]:
            return False
    return True

def propogate_nines(num_list, index):
    for i in xrange(index, len(num_list)):
        num_list[i] = 9

def getNearestTidy(input_num):
    current_num = map(int, list(input_num))
    length = len(current_num)
    while not isTidy(current_num, length):
        for i in xrange(length - 1):
            if current_num[i] > current_num[i + 1]:
                current_num[i] = max(0, current_num[i] - 1)
                propogate_nines(current_num, i + 1)
    return int(''.join(map(str, current_num)))

if __name__ == "__main__":
	n = int(raw_input())
	for i in xrange(1, n + 1):
		num = raw_input()
		print "Case #%s: %d" % (i, getNearestTidy(num))
