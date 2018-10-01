def flip_all(pancakes, k):
 	i = 0
 	count = 0
 	while i < len(pancakes):
 		if pancakes[i] == '-':
 			if len(pancakes) - i < k:
 				return -1
 			count = count + 1
 			for j in xrange(k):
 				pancakes[i+j] = flip(pancakes[i+j])
 		i = i+1
 	return count

def flip(p):
 	if p=='+':
 		return '-'
 	else:
 		return '+'

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  pancakes, k = raw_input().split(" ")  # read a list of integers, 2 in this case
  result = flip_all(list(pancakes), int(k))
  if result==-1:
  	result = 'IMPOSSIBLE'
  print "Case #{}: {}".format(i, result)
  # check out .format's specification for more formatting options

