def problemC(inputFile,outputFile):
	f = open(inputFile,"r")
	input = f.readlines()
	output = ""
	for i, line in enumerate(input[1:]):
		[a,b] = line.split()
		output += "Case #" + str(i+1) + ": " + str(recycled(int(a),int(b))) + "\n"
	g = open(outputFile,"w")
	g.write(output)
	g.close()
	f.close()

def recycled(a,b):
	count = 0
	ls = [0]*(b+1)
	for i in range(a,b+1):
		if ls[i] == 0:
			permutedNumbers = permute(i,a,b)
			for n in permutedNumbers:
				ls[n] = 1
			add = nChoose2(len(permutedNumbers))	
			count += add
	return count

def permute(num,a,b):
	s = set([])
	n = str(num)
	for i in range(0,len(n)):
		x = int(n[i:]+n[:i])
		if x >= a and x <= b:
			s.add(x)
	return s

def nChoose2(num):
	x = num
	return num*(num-1)//2

problemC("p3-input.txt","p3-output.txt")
