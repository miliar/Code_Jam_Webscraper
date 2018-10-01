



def check(num):

	ans = ""
	num_string = str(num)

	for i in range(len(num_string)-1):

		if int(num_string[i]) > int(num_string[i+1]):
			sub = int(num_string)%(10**(len(num_string)-i-1))
			num -= sub + 1
			break

	return num

def convert(num):

	flag = True

	while flag:
		num = check(num)
		string = str(num)
		flag = False
		for i in range(len(string)-1):
			if string[i] > string[i+1]:
				flag = True

		if flag == False:
			return num

file = open("B-large.in.txt", "r")
file2 = open("output_file.txt", "w")
input = file.readlines()

for i in range(1,len(input)):
	output = "Case #" + str(i) + ":  " + str(convert(int(input[i]))) + "\n"
	file2.writelines(output)

file.close()
file2.close()

