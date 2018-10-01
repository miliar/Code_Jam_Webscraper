# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def getOutput(n):

	num_n = int(n)
	if len(n) == 1:
		return num_n
	value_one = int('1'*len(n))
	value_nine = int('9'*(len(n)-1))
	if num_n < value_one:
		return value_nine
	else:
		pos = 0
		for i in range(len(n)-1):
			if int(n[i]) < int(n[i+1]):
				pos = i + 1
			if int(n[i]) > int(n[i+1]):
				return n[:pos] + str(int(n[pos])-1) + '9'*(len(n)-pos-1)
	return num_n

if __name__ == '__main__':
	t = int(input())  # read a line with a single integer
	for i in range(1, t + 1):
		n = input()
		print("Case #{}: {}".format(i, getOutput(n)))
	  # check out .format's specification for more formatting options