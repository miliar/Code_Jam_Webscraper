# String number to list of its integers
def divNum(l):
	num_list = []
	for n in l:
		num_list.append(int(n))
	return num_list

def main(l):
	num_list = divNum(l)
	check = 0
	if check == len(num_list)-1:
		answer = l
	while check != len(num_list)-1:
		check = 0
		for n in range(len(num_list)-1)[::-1]:
			if num_list[n+1] >= num_list[n]:
				check = check + 1
			else:
				place = n
				#print(place)
				break
		if check == len(num_list)-1:
			answer = ''
			for a in num_list:
				answer = answer + str(a)
			break
		else:
			for x in range(len(num_list)):
				if x == place or x == place + 1:
					num_list[x] = num_list[x] - 1
				if x > place:
					num_list[x] = 9
	return answer

if __name__ == "__main__":
	with open('B-large.in', 'r') as f:
		lines = f.readlines()

	case = 1
	answers = []
	string_answers = []
	for l in lines[1:len(lines)]:
		l = l.strip()
		answer = main(l)
		answers.append(answer)
		string = "Case #" + str(case) + ": " + str(answer).strip('0') + '\n'
		string_answers.append(string)
		print(string)
		case = case + 1

	with open('result1.txt', 'w') as k:
		for ans in string_answers:
			k.write(ans)