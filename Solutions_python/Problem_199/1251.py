from __future__ import print_function

def get_swaps(l,k):
	length = len(l)
	result = 0
	for i in xrange(length):
		if(l[i] == '+'):
			continue
		else:
			result += 1
			if(i+k <= length):
				for j in xrange(i,i+k):
					if l[j] == '-':
						l[j] = '+'
					else:
						l[j] = '-'
	for i in l:
		if i == '-':
			return None
	return result

testcases = int(raw_input().strip())
for i in xrange(1,testcases+1):
	inp = raw_input().strip().split()
	l = list(inp[0])
	k = int(inp[1])
	case_str = 'Case #' + str(i) + ': '
	print(case_str, end='')
	result = get_swaps(l,k)
	if result is None:
		print('IMPOSSIBLE')
	else:
		print(result)
