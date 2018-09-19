input = open("input.txt", "r")
output = open("output3.txt","w")
testcases = int(input.readline())
count = 1

def transposition(num_str):
	last_digit = num_str[-1]
	rest = num_str[0:-1]
	return "".join([last_digit,rest])

while count <= testcases:
	in_line = input.readline()
	data = in_line.split(" ")
	a = int(data[0])
	b = int(data[1])
	total = 0
	all_nums = range(a,b+1)
	for num in all_nums:
		transpositions = []
		t = transposition(repr(num))
		while t != repr(num):
			t_val = int(t)
			if repr(t_val) == t and t_val in all_nums:
				transpositions.append(t_val)
				all_nums.remove(t_val)
			t = transposition(t)
		x = len(transpositions)
		total = total + x*(x+1)/2
		
	out_line = "Case #"+repr(count)+": "+repr(total)
	output.write(out_line+"\n")
	count = count +1