

def compute(inputs):
	outputs = []
	for i, line in enumerate(inputs):
		guyssofar = 0
		friends = 0
		for shylevel, people in enumerate(line):
			if shylevel > guyssofar:
				friends += shylevel - guyssofar
				guyssofar += shylevel - guyssofar
			guyssofar += int(people)

		outputs.append(friends)
	return outputs

def main():
	inputfile = "A-large.in"
	outputfile = "01-testoutput.txt"
	inputs = []
	with open(inputfile) as f:
		for line in f.readlines()[1:]:
			inputs.append(line.strip().split(' ')[-1])
	print inputs
	outputs = compute(inputs)
	print len(inputs)
	print len(outputs)
	with open(outputfile, "w") as f:
		for i, line in enumerate(outputs):
			f.write("Case #{}: {}\n".format(i+1, line))


main()