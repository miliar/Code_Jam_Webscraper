inputData = open("A.in", "r")
outputData = open("A.out", "w")
outputLines = []

def output (string):
	string = str(string)
	print(string)
	outputLines.append(string)

def case (x, y):
	output("Case #" + str(x) + ": " + str(y))


for (number, line) in enumerate(inputData.read().splitlines()[1:]):
	i = 1
	n = int(line)
	x = 1
	b = n
	if b % 10 == 0:
		b = n - 1
	while i < n:
		if i < b:
			if len(str(i)) < len(str(b)):
				# Aim for abc999
				v = str(i)[-len(str(i)) // 2:]
				if v == "9" * len(v) and str(i) != "9" * len(str(i)):
					i = int(str(i)[::-1])
				else:
					i += 1
			else:
				if i < int(str(i)[::-1]) <= b:
					if str(i)[-len(str(i)) // 2:] == (str(b)[::-1])[-len(str(b)) // 2:]:
						i = int(str(i)[::-1])
					else:
						i += 1
				else:
					i += 1
		else:
			i += 1
		# print(i, n)
		x += 1
	case(number + 1, x)


outputData.write("\n".join(outputLines))
inputData.close()
outputData.close()