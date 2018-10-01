def epilogue(result, num):
	out_file.write("Case #" + str(num+1) + ": " + result + '\n')

in_file, out_file = open('A-large.in', 'r'), open('A-large.out', 'w')

invert = {'+' : '-', '-': '+'}
def flip(i, pancake_stack, K):
	for j in range(K):
		pancake_stack[i+j] = invert[pancake_stack[i + j]]

num_cases = int(in_file.readline())
for case_num in range(num_cases):
	unprocessed, K = in_file.readline().split()
	K = int(K)
	pancake_stack = [c for c in unprocessed if c == '+' or c == '-']
	num_flips = 0
	for i in range(len(pancake_stack) - K + 1):
		if pancake_stack[i] == '-':
			flip(i, pancake_stack, K)
			num_flips = num_flips + 1

	possible = True
	for i in range(len(pancake_stack)):
		if pancake_stack[i] == '-':
			epilogue("IMPOSSIBLE", case_num)
			possible = False
			break
	if possible:
		epilogue(str(num_flips), case_num)