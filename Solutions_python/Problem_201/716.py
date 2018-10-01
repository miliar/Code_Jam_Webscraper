
input = open("C-large.in", "r")
output = open("C-large.out", "w")


T = int(input.readline().strip())

for j in range(1, T+1):
	output.write("case #{}: ".format(j))
	input_line = input.readline().strip()
	stalls = int(input_line.split()[0])
	people = int(input_line.split()[1])

	while True:
		if people == 1:
			if stalls % 2 != 0:
				max = (stalls -1) /2
				min = (stalls -1) /2
			else:
				max = stalls / 2
				min = stalls / 2 -1
			break
		if stalls % 2 != 0:
			stalls = (stalls - 1) / 2
		else:
			if people % 2 == 0:
				stalls = stalls / 2
			else:
				stalls = stalls / 2 -1
		people /= 2


	output.write("{} {}".format(max, min))
	output.write("\n")

input.close()
output.close()

