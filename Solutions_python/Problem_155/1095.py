def ovation(s, shyness):
	needed = 0
	standing = 0
	k = 0

	while k < len(shyness):
		if k <= standing:
			standing += int(shyness[k])
			k += 1
		else:
			needed += k - standing
			standing = k

	return needed

def main():
	from sys import stdin
	input = stdin.read().split('\n')
	T = int(input[0])

	for t in range(T):
		line = input[t + 1].split()
		s = int(line[0])
		shyness = line[1]

		print "Case #{0}: {1}".format(t + 1, ovation(s, shyness))

if __name__ == '__main__':
	main()