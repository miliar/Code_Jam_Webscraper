def inputvars():
	f = open('B-large.in')
	num = int(f.readline())
	numlist = f.read().splitlines()
	return num, numlist

def outputvars(num, output):
	f = open('output.txt', 'w')
	for x in range(num):
		f.write('Case #' + str(x + 1) + ": " + str(output[x]))
		f.write("\n")
	f.close()

def main():
	num, numlist = inputvars()
	output = []
	for x in numlist:
		n = [0] + list(x)
		n = list(map(int, n))
		highestNonTidy = checkTidy(n)
		while(highestNonTidy > 0):
			n[highestNonTidy - 1] -= 1
			if(n[highestNonTidy - 1] < 0):
				carryOver = highestNonTidy - 1
				while(n[carryOver] < 0):
					n[carryOver] += 10
					carryover -= 1
					n[carryOver] -= 1
			for y in range(highestNonTidy, len(n)):
				n[y] = 9
			highestNonTidy = checkTidy(n)
		output.append(int(''.join(map(str, n))))
	outputvars(num, output)

def checkTidy(num):
	prev = 0
	for x in range(len(num)):
		if(prev > int(num[x])):
			return x
		prev = int(num[x])
	return 0
main()