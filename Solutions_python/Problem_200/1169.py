def fallback(n_array, choice, i, delta):
	if i == 0:
		if choice[i] == 1:
			return False
		else:
			choice[i] = choice[i] - 1
			return True
	
	if choice[i-1] <= choice[i] - delta:
		choice[i] = choice[i] - delta
		return True
	else:
		choice[i] = 9
		return fallback(n_array, choice, i-1, 1)
		

def solve(n):
	n_array = map(lambda x: int(x), str(n))
	# single digit
	if len(n_array) == 1:
		return n
	# first digit effective
	choice = n_array
	found_ans_flag = False
	i = 1
	falled = False
	while i < len(n_array):
		if (choice[i-1] > n_array[i]) and not(falled):
			if not(fallback(n_array, choice, i-1, 1)):
				break
			else:
				falled = True
		else:
			choice[i] = n_array[i] if not(falled) else 9
			i = i + 1
			if i == len(n_array):
				found_ans_flag = True
	if not(found_ans_flag):
		# other wise 9999999999...
		choice[0] = 0
		for i in range(1, len(choice)):
			choice[i]=9
	choice = map(lambda x: str(x), choice)
	ans = "".join(choice)
	return int(ans)

if __name__=='__main__':
	t = int(raw_input())
	for i in range(t):
		n = int(raw_input())
		num = solve(n)
		print "Case #"+str(i+1)+": " + str(num)
