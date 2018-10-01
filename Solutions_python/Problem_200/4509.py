# Google Code Jam: Assignment B

def processNumber(number, row):
	number_string = str(number);
	position = 0;
	newNumber = [];

	if((len(number_string) - 1) >  position):

		for i in number_string:
			nextNumber = number_string[position + 1];

			if(nextNumber >= i):
				nextNumber = i;
				newNumber.append(i);
			else:

				if(int(nextNumber) == 0 and int(i) == 1):
					#print "Nu hebben we een probleem"
					newNumber = []
					for y in range(0, len(number_string) - 1):
						newNumber.append(str(9))

					anwser = ''.join(newNumber)
					#print "Case #" + str(a) + ": " + str(anwser);
					processNumber(anwser, row)

					break;

				if((int(i) - 1) > 0):
					newNumber.append(str(int(i) - 1))

				numbersLeft = len(number_string) - position

				for y in range (1, numbersLeft):

					newNumber.append(str(9))

				anwser = ''.join(newNumber)

				#print "Case #" + str(a) + ": " + str(anwser);
				processNumber(anwser, row)
				break;

			if((position + 2) < len(number_string)):

				position = position + 1;

			else:
				#print "Dit is de oplossing!"
				print "Case #" + str(row) + ": " + str(number);
				break

	else:
		print "Case #" + str(row) + ": " + str(number);

t = int(raw_input())  # read a line with a single integer

for a in xrange(1, t + 1):

	assignment  = raw_input()

	processNumber(assignment, a)