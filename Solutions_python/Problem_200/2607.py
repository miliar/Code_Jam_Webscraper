T = int(input(""))
case = 1

for cases in range(T):
	j = 0
	cnt = 0
	number = input("")
	numbers = list(number)
	if(len(number) == 1):
		print('Case #{}: {}'.format(case, number))
	else:
		for i in range(len(numbers) - 1, 0, -1):
			if(int(numbers[i]) > int(numbers[i-1])):
				continue
			elif(int(numbers[i]) == int(numbers[i-1])):
				continue
			elif(int(numbers[i]) < int(numbers[i-1])):
				numbers[i-1] = int(numbers[i-1]) - 1
				for j in range(i, len(numbers)):
					numbers[j] = 9
		
		print('Case #{}: {}'.format(case, (''.join(map(str, numbers))).lstrip("0")))
	case += 1