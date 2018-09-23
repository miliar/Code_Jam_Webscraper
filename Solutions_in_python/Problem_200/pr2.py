def is_tidy(num):
	return all([1 if (idx == 0 or char >= num[idx-1]) else 0 for idx, char in enumerate(num)])

def index_of_disorder(str_num):
	index = -1

	if len(str_num) <= 1:
		return index

	for idx, char in enumerate(str_num[:-1]):
		if char > str_num[idx+1]:
			return idx

	return index

def find_largest_tidy(end):
	# while not is_tidy(end):
	# 	digits = [d if d < N[-1] for d in string_digits]
	# 	for suffix in digits:
	# 		N = N[:-1] + suffix
	# 		if is_tidy(N):
	# 			return N
	while not is_tidy(end):
		index = index_of_disorder(end)
		if index > -1:
			end = end[:index] + str(int(end[index]) - 1) + (len(end) - index - 1) * '9' 


	return int(end)

def main():
	n_test_cases = int(raw_input())
	string_digits = ['0','1','2','3','4','5','6','7','8','9','0']
	for idx in xrange(n_test_cases):
		N = raw_input()
		
		if is_tidy(str(N)):
			print 'Case #{0}: {1}'.format(idx+1, N)
			continue
		else:
			print 'Case #{0}: {1}'.format(idx+1, find_largest_tidy(N))
			


if __name__ == "__main__":
	main()