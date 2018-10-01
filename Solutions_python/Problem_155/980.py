#MAM, Google Code Jam - Qualification Round, Problem 1

def solve(c):
	smax, audience = c.split(" ")
	smax = int(smax)
	current = 0

	audience = list(audience.rstrip())
	audience = [int(i) for i in audience]
	answer = 0

	while (current < smax):

		#print current, audience
		if (audience[current] == 0):
			answer += 1
		else:
			audience[current + 1] = audience[current + 1] + audience[current] - 1
		current += 1

	return answer

def main():
	with open('A-large.in', 'r') as infile, open('output.txt', 'w') as outfile:
		
		T = int(infile.readline())
		for x in xrange(T):
			line = infile.readline()
			outfile.write("Case #" + str(x + 1) + ": " + str(solve(line)) + "\n")

if __name__ == "__main__":
	main()