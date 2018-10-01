import sys

def is_consonant(c):
	return (not ((c == 'a') or (c == 'e') or (c == 'i') or (c == 'o') or (c == 'u')))

def count_consecutive_consonants(s):
	consecutive_consonants = [0 for c in range(len(s))]	
	
	if (is_consonant(s[0])):
		consecutive_consonants[0] = 1
	
	for i in range(1, len(s)):
		if (is_consonant(s[i])):
			consecutive_consonants[i] = consecutive_consonants[i - 1] + 1
	
	return max(consecutive_consonants)

def get_n_value(name, n):
	n_value = 0

	for i in range(0, len(name)):
		for j in range(i + 1, len(name) + 1):
			if (count_consecutive_consonants(name[i:j]) >= n):
				n_value += 1

	return n_value

input = open(sys.argv[1], 'r')

t = input.readline()
t = t[:-1]
t = int(t)

for i in range(0, t):
	line = input.readline()
	tokens = line.split()
	name = tokens[0]
	n = int(tokens[1])
	
	n_value = get_n_value(name, n)

	sys.stdout.write('Case #' + str(i + 1) + ': ' + str(n_value))
			
	if (i + 1 < t):
		print('')

input.close()