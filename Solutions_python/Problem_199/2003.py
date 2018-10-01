import sys

def main(argv):
	input_file = open(argv[1], 'r')
	output_file = open(argv[2], 'w')
	lines = [line.rstrip('\n') for line in input_file]
	for x in range(1, len(lines)):
		cookies = lines[x].split(' ')[0]
		size = int(lines[x].split(' ')[1])
		cookies_list = list(cookies)
		iteration = 0
		while True:
			i = cookies.find('-')
			if i == -1:
				output_file.write("Case #" + str(x) + ": " + str(iteration) + "\n")
				break
			else:
				if (i + size + 1) > len(cookies):
					for w in range(1 , size+1):
						cookies_list[len(cookies)-w] = flip(cookies_list[len(cookies)-w])
				else:
					for w in range(i, i+size):
						cookies_list[w] = flip(cookies_list[w])
				cookies = ''.join(cookies_list)
				iteration = iteration + 1
				if iteration > len(cookies):
					output_file.write("Case #" + str(x) + ": " + "IMPOSSIBLE" + "\n")
					break

		
	input_file.close()
	output_file.close()

def flip(x):
	if x == '+':
		return '-'
	else:
		return '+'


main(sys.argv)