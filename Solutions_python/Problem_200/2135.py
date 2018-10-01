import re
def array(a):
	b = str(a)

	cut = 0
	for index in range(len(b)-1):
		if int(b[index]) == 0:
			cut+=1
		else:
			break
	b = b[cut:]
	for index in range(len(b)-1):
		#print "b[index] is : " + str(b[index]) + " and b[index+1] is : " + str(b[index+1])
		if (int(str(b[index])) > int(str(b[index+1]))):
			rem = len(b) - index - 1
			s = ""
			for i in range(rem):
			    s+=str(9)
			b = b[:index] + str(int(b[index]) - 1) + s

	#print "the initial number is " + str(a) + " and final number is: " + b
	return int(b)





t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  #n= [int(s) for s in raw_input()]  # read a list of integers, 2 in this case
  n = int(raw_input())
  ans = array(n)
  acc = 0
  while acc < 20:
	ans = array(ans)
	acc+=1
  print "Case #{}: {}".format(i, ans)

		