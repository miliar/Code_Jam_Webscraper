import sys

inputFile = open(sys.argv[1], "r")
outputFile = open("output.txt", "w")

alphabet = "abcdefghijklmnopqrstuvwxyz"
vals = "yhesocvxduiglbkrztnwjpfmaq"

SWAP = {}
for x in range(26):
	SWAP[alphabet[x]] = vals[x]

SWAP[' '] = ' '

caseNums = int(inputFile.readline())
for case in range(caseNums):
	line = inputFile.readline()
	outputFile.write("Case #%d: "%(case+1))
	for letter in line:
		if letter.isalpha():
			outputFile.write("%s"%(SWAP[letter]))
		else:
			outputFile.write(letter)

inputFile.close()
outputFile.close()
