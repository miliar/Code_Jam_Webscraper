#skleton
T = int(input())
for t in range(T):
	len_num = 0
	num = int(input())
	num_list = list(map(int, str(num)))
	num_cpy = num
	i = 0
	
	while(num_cpy / 10 != 0):
		len_num += 1
		num_cpy //= 10

	for i in range(len_num-1, 0, -1):
		if(num_list[i] < num_list[i-1]):
			tmp = num % (10**(len_num - i))
			num -= (tmp+1)
			num_list = list(map(int, str(num)))

		else:
			continue


	print("Case #{0}: {1}".format(t+1, num))