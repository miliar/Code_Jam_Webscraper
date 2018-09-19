import sys

def is_palin(x):
	tmp = 0
	exp = x
	while(exp != 0):
		tmp = tmp*10 + exp%10 
		exp = exp/10
	if tmp == x:
		return True
	return False

T = int(raw_input())
for i in xrange(T):
	[low,high] = map(int, raw_input().strip().split())
	root = 1
	test = 1
	count = 0
	while(True):
		if is_palin(root) == True:
			test = root*root
			if is_palin(test) == True and test >= low and test <= high:
				count += 1
			if test > high:
				break
		root += 1
	print "Case #%d: %d" %(i+1, count)
