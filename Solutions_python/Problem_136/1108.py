input = open('B-large.in', 'r')
output = open('output.txt', 'w')

test_case_count = int(input.readline())
#process test case one by one
for i in range(test_case_count):
	#store relevant data
	params = str.strip(input.readline()).split(' ')
	C = float(params[0])
	F = float(params[1])
	X = float(params[2])

	#initialize variables
	cookies_count = 0
	r = 2.0 #rate

	#compute optimal time
	t0 = X/r #case: we don't build farms
	n = 1
	A_n = C/r
	t1 = A_n + X/(r + n*F) #case: 1 farm
	if t0 < t1:
		min_t = t0
	else:
		min_t = t1

	continue_condition = True
	while (continue_condition):
		n += 1
		A_n += C/(r + (n-1)*F)
		t1 = A_n + X/(r + n*F)
		if t1 < min_t:
			min_t = t1
		else:
			continue_condition = False

	y = min_t
	#print output
	output.write("Case #%d: %.7f\n" %(i+1, y))