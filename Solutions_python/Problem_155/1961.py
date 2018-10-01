# Google Code Jam 2015
# Andrew Sung - theAndrewASung
# Problem 1: Standing Ovation

import argparse

def readInput(inputSrc):
	with open(inputSrc,'r') as f:
		num_test_cases = int(f.readline())
		test_cases = []
		for i in range(num_test_cases):
			next_line = f.readline().strip('\n')
			s_max = int(next_line[:str.find(next_line," ")])
			shyness = [int(next_line[i]) for i in range(str.find(next_line," ")+1,len(next_line))]
			test_cases.append({'max':s_max, 'shyness':shyness})
	return test_cases

def writeOutput(outputArr):
	with open('p1-output.txt','w') as f:
		for i in range(len(outputArr)):
			f.write("Case #"+str(i+1)+": "+str(outputArr[i])+"\n")

def standingOvation(case):
	num_people_standing = 0
	num_people_needed = 0
	for i in range(case['max']+1):
		if num_people_standing < i:
			num_people_needed += (i-num_people_standing)
			num_people_standing = i
		num_people_standing += case['shyness'][i]
	return num_people_needed

# Main Function
if __name__ == "__main__":
	
	# Command line argument parser
	argparser = argparse.ArgumentParser(description="Google Code Jam 2015 - Problem 1: Standing Ovation")
	argparser.add_argument("input",help="Input file.")
	argparser.add_argument("ouput",help="Output file.")

	# Get command line arguments
	args = argparser.parse_args()

	test_cases = readInput(args.input)
	output = []
	for test in test_cases:
		output.append(standingOvation(test))
	writeOutput(output)
	