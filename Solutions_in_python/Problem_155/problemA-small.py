#!/usr/bin/python

def main():
	input_filename = 'A-small-attempt0.in'
	output_filename = 'A-small-attempt0.out'

	inputLines = open(input_filename).readlines()
	output_file = open(output_filename,'w+')
	N = int(inputLines[0])

	for i in range(1,N+1):
		testcase_string = inputLines[i].strip()
		testcase = testcase_string.split()
		min_friends_added = friends_added(int(testcase[0]), testcase[1])
		output_file.write("Case #" + str(i) + ": " + str(min_friends_added) + "\n")

	output_file.close()

def friends_added(max_shyness, audience):
    standing = int(audience[0])
    added = 0
    
    for k in range(1,max_shyness+1):
        if int(audience[k]) > 0:
        	if k > standing:
        		added += k - standing
        		standing += added
        	standing += int(audience[k])

    return added

if __name__ == '__main__':
	main()
