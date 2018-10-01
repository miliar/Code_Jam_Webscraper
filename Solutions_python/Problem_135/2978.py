def main():


	files = ["A-small-attempt0.in","B-small.in","C-small.in","D-small.in"]
	content = file(files[0])
	
	cases = int(content.readline())
	filename = "output.txt"
	File = open(filename,'w')

	for i in range(cases):
		Arr1 = []
		Arr2 = []
		R1 = int(content.readline())
		for j in range(4):
			Arr1.append(map(int,content.readline().strip().split()))
		R2 = int(content.readline())
		for j in range(4):
			Arr2.append(map(int,content.readline().strip().split()))

		step1 = Arr1[R1-1]
		step2 = Arr2[R2-1]

		final = set(step1) & set(step2)

		if(len(final) == 1):
			File.write("Case #%d: %s" % (i+1,list(final)[0]) + "\n")
		elif(len(final) == 0):
			File.write("Case #%d: %s" % (i+1,"Volunteer cheated!") + "\n")
		else:
			File.write("Case #%d: %s" % (i+1,"Bad magician!" ) + "\n")
		


main()
