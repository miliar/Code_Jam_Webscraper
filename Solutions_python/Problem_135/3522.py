
def magic_trick(infile):

	testfile = open(infile,'r')
	outfile = open('outfile.out','w+')

	for test_case in range(int(testfile.readline().rstrip('\n'))):
		print test_case
		
		answer1 = int(testfile.readline().rstrip('\n')) #get row #
		print answer1

		for lines in range(answer1): #get first answer row
			row1 = str.split(testfile.readline().rstrip('\n'),' ')
			print row1

		for i in range(4-answer1): #advance realines to remainder
			print testfile.readline()


		answer2 = int(testfile.readline().rstrip('\n')) #get second row #
		print answer2

		for lines in range(answer2): #get second answer row
			row2 = str.split(testfile.readline().rstrip('\n'),' ')
			print row2

		for i in range(4-answer2): # advance readlines to remainder
			print testfile.readline()

		matches = []
		for card in row1:
			if card in row2:
				matches.append(card)

		if matches:
			if len(matches) > 1:
				outfile.write("Case #{}: {}\n".format((test_case + 1),"Bad magician!"))

			else:
				outfile.write("Case #{}: {}\n".format((test_case + 1),matches[0]))
		else:
			outfile.write("Case #{}: {}\n".format((test_case + 1),"Volunteer cheated!"))



if __name__ == '__main__':
	magic_trick('sample.in')