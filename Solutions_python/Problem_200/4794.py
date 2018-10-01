with open("input.in") as f:
	content = f.readlines()

content = [x.strip() for x in content]

cases = content[0]
content = content[1:]

indCases = []

for test in content:
	indCases.append(int(test))

output = open("output.out", "w")

i = 1
for case in indCases:

	for j in range(0, case):

		number = case - j
		numberList = [int(x) for x in str(number)]

		if numberList == sorted(numberList):

			output.write("Case #" + str(i) + ": " + str(number) + "\n")
			break

	i+=1