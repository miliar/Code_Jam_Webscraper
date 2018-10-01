def count1(case):
	maxS = int(case.split()[0])
	string = case.split()[1]
	standing = 0
	count = 0
	bank = 0
	for i in range(len(string)):
		if string[i] == '0':
			if bank > 0:
				bank -= 1
			else:
				count += 1
			continue
		if int(string[i]) > 1:
			bank += int(string[i]) - 1
	return count



def main():
	file1 = open('A-large.in','r')
	file2 = open('outfile.txt','w')
	caseNumber = int(file1.readline())
	cases = file1.read().split('\n')
	for x in range(caseNumber):
		file2.write("Case #" + str(x+1) + ": " + str(count1(cases[x])) + "\n")
main()