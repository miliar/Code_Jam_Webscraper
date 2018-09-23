def get_last_tidy_number(n):
	s = list(str(n))

	dropFirstDigit = False
	for i in range(len(s) - 1):
		if (s[i] > s[i + 1]):
			if ((i > 0) and (s[i] == '1')):
				for j in range(i, 0, -1):
					s[j] = '9'
				dropFirstDigit = True
			elif ((i > 0) and (s[i] == s[i - 1])):
				s[i] = '9'
				s[i - 1] = chr(ord(s[i - 1]) - 1)
			else:
				s[i] = chr(ord(s[i]) - 1)
				for j in range(i - 1, -1, -1):
					if (s[j] > s[i]):
						s[j] = s[i]

			for j in range(i + 1, len(s)):
				s[j] = '9'

			break

	if (dropFirstDigit):
		s = s[1:]

	last_tidy_number = int(''.join(s))

	return last_tidy_number


t = int(raw_input())

for t_i in range(t):
	n = int(raw_input())
	last_tidy_number = get_last_tidy_number(n)

	print('Case #' + str(t_i + 1) + ': ' + str(last_tidy_number))
