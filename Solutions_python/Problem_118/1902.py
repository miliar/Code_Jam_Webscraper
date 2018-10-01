import sys,logging 
#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

inputFile = open(sys.argv[1])
outFile   = open("outFile.txt", "w")

def isPalindrome(number):
	if number == int(number):
		number = str(int(number))
	else:
		 return False
	return number == number[::-1]

def isSquare(number):
	number = number ** 0.5
	return int(number) == number



for caseNum in range(int(inputFile.readline())):
	input = inputFile.readline().rstrip().split()
	start = int(input[0])
	end   = int(input[1])		
	
	count = 0
	for number in range(start, end + 1):
		if isPalindrome(number) and isPalindrome(number ** 0.5):
			count += 1	

	outFile.write("Case #" + str(caseNum + 1) + ": " + str(count) + "\n")
	#print("Case #" + str(caseNum+1) + ": " + str(count) + "\n")
			
