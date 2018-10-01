# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
	number = [int(s) for s in input()] 
	adjust = 0
	final = 0
	same = 0
	output = ""
			
	for j in range(0, len(number)-1):
		if number[j] > number[j+1]:
			adjust = len(number)- 1 - j + same
			break
			
		elif number[j] == number[j+1]:
			same += 1
	
	for integer in number:
		output += str(integer)
	
	if (adjust > 0):
		adjustment = "1"
		for k in range(adjust):
			adjustment += "0"
			
		final = int(output) - int(output) % int(adjustment) - 1
		output = final
		
	print("Case #{}: {}".format(i, int(output)))
	# check out .format's specification for more formatting options