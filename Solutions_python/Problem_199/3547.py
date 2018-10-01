import sys
import pdb

infput_file = sys.argv[1]
output_file = "output.txt"

def create_result_line(num, row, count):
	if "-" not in row:
		return "Case #{0}: {1}\n".format(num, count)
	else:
		return "Case #{0}: IMPOSSIBLE\n".format(num)

def turn(string):
	string = string.replace("-", "|")
	string = string.replace("+", "-")
	string = string.replace("|", "+")
	return string

def solve(row, K):
	result = ""
	counter = 0
	print ("Solving input: ", row, K)
	for i in range(len(row)-K+1):
		#print (i)
		part = row[i:i+K]
		#print ("Part: " + part)
		if (part == K*"+"):
			#print("A")
			row = row[:i] + part + row[i+K:]
		elif (part[0]=="-"):
			#print("B")
			result = turn(part)
			row = row[:i] + result + row[i+K:]
			counter = counter + 1
		elif (part[0]=="+"):
			#print("C")
			pass
		#print (row)

	print ("Result: " + row, counter)
	return row, counter


with open(infput_file) as in_file:
	with open('output_file', 'w') as out_file:

	    file_lines = in_file.readlines()
	    T = (int)(file_lines[0])
	    for i in range(1,len(file_lines)):
	    	row, K = file_lines[i].split(" ")
	    	new_row, count = solve(row, int(K))
	    	line = create_result_line(i, new_row, count)
	    	out_file.write(line)



#print (turn("++--+"))
#Case #1: 3
#Case #2: 0
#Case #3: IMPOSSIBLE