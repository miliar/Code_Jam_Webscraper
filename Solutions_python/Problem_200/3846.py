import sys
import os

input_file_name = "B-large (1).in"

def check_tidyness(num, start_index = -1):
	number = [int(i) for i in str(num)]
	if start_index == -1:
		start_index = len(number)-1
	print("Working with index "+str(start_index))
	for i in range(start_index, 0, -1):
		if number[i] < number[i-1]:
			print("Number on index: "+str(i)+": "+str(number[i]))
			number = [str(n) for n in number]
			print("Subtracting "+str(int("".join(number[i:]))+1))
			num -= int("".join(number[i:]))+1
			print("Got this: "+str(num))
			return check_tidyness(num, i-1)
	print("Returning this: "+str(num))
	return num

sys.stdout = open(os.devnull, "w")
with open(input_file_name, "r") as input_file:
	cases = int(input_file.readline())
	results = []
	for line in input_file:
		num = int(line)
		print("Source number: "+str(num))
		print("Len of num: "+str(len(str(num))))
		results.append(check_tidyness(num))
sys.stdout = sys.__stdout__

with open(input_file_name.split('.')[0]+"_results", "w") as output_file:
	print("")
	print("WRITING RESULTS TO FILE")
	for i in range(len(results)):
		output_string = "Case #"+str(i+1)+": "+str(results[i])
		print(output_string)
		output_file.write(output_string+"\n")

import random
a = random.randint(1000000000, 10000000000)
print(a)
sys.stdout = open(os.devnull, "w")
b = check_tidyness(a)
sys.stdout = sys.__stdout__
print(b)