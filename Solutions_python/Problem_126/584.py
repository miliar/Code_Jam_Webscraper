import re

def main():
#	fileIn = "inputsample.txt"
	fileIn = "A-small-attempt0.in"
	fileOut = "output.txt"
	
	fin = open(fileIn, 'r')
	fout = open(fileOut, 'w')
	isFirstLine = True
	
	cases = int(fin.readline())
	for case in range(cases):
		outputStr = "Case #" + str((case+1)) + ": "
		matches = 0
		
		# Read in the input
		tempLineArr = fin.readline().split(" ")
		caseStr = tempLineArr[0]
		n = int(tempLineArr[1])
		
		# Solve the test case
		strLen = len(caseStr)
		for pos in range(strLen):
			# Iterate through each letter as the starting point
			lenToEnd = strLen - pos
			posEnd = pos + 1
			if(lenToEnd < n):
				break
			
			# Incrementally increase the substring size
			# and check the string
			while(posEnd <= strLen):
				strSnippet = caseStr[pos:posEnd]
#				print "strSnippet: " + strSnippet
				
				# Check to see if the snippet is valid
				valid = isValidStr(strSnippet, n)

				# If the snippet is valid, increment appropriately
				if(valid):
					addTo = lenToEnd - len(strSnippet) + 1
#					print "\tAdding " + str(addTo) + " to matches"
					matches = matches + addTo
					break
									
				posEnd = posEnd + 1		# Increment
						
		# Write to the output file
		outputStr = outputStr + str(matches)
#		print "\n\t" + outputStr
		if(isFirstLine):
			fout.write(outputStr)
			isFirstLine = False
		else:
			fout.write("\n" + outputStr)
		
		# Increment the case counter
	
	# Close the files
	fin.close()
	fout.close()
	
def isValidStr(strSnippet, n):
	valid = False
	pattern = re.compile("[aeiou]")
	
	for pos2 in range(len(strSnippet)):
		subSnippet = strSnippet[pos2:(pos2+n)]
		if((pattern.search(subSnippet) == None) \
			and (len(subSnippet) >= n)):
			# Matched!
			valid = True
			break
	return valid
	
if __name__ == '__main__':
	main()