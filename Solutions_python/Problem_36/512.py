input = open('./C-small.in','r')
output = open('./output.out','w')
w = 'welcome to code jam'

def codejam(list, chr):
	temp = []
	for a in list:
		while chr in a:
			ind = a.index(chr)
			temp.append(a[(ind + 1):])
			a = a[(ind + 1):]
	return temp		

def nicefy(result):
	result = str(result)
	zero_num = 4 - len(result)
	result = (zero_num * '0') + result
	return result


case_num = int(input.readline())
for i in range(1, case_num + 1):
	case = [input.readline().strip()]
	for chr in w:
		case = codejam(case, chr)
	result = len(case) % 10000
	result = nicefy(result)
	written = 'Case #' + str(i) + ': ' + result
	if i != case_num:
		written = written[:] + '\n'
	output.write(written)