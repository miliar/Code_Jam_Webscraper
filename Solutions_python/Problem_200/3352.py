def checkTidy(number):
	for i in xrange(len(number) - 1):
		if (number[i] > number[i + 1]):
			return False;
	return True;


def tidyNumbers(number):
	if (checkTidy(number)):
		return number
	for i in xrange(len(number) - 1, 0, -1):
		if (number[i] < number[i - 1]):
			if (number[i] == "0"):
				temp = int(''.join(number)) - 1*(10**(len(number) - 1 - i))
				number = list(str(temp))
				for j in xrange(len(number) - 1, i - 1, -1):
					number[j] = "9"
			else:
				for j in xrange(len(number) - 1, i - 1, -1):
					number[j] = "9"
				number[i - 1] = str(int(number[i - 1]) - 1)
	return tidyNumbers(number)



fRead = open("B-large.in", "r")
fWrite = open("B-large-output.txt", "w")
t = fRead.readline()
lineCount = 0
for line in fRead.readlines():
    lineCount += 1
    number = line.replace("\n", "")
    tidyNumber = tidyNumbers(list(number))
    tidyNumberFormated = int("".join(tidyNumber))
    fWrite.write('Case #{}: {}\n'.format(lineCount, tidyNumberFormated))
fWrite.close()