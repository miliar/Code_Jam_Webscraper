import sys
import math

sys.stdout = open('out', 'w')
with open(sys.argv[1], 'r') as f:
	l = f.readline().split(' ')
	for i in range(int(l[0])):
		l = f.readline().split(' ')
		aux = int(math.pow(2,int(math.log(int(l[1]),2)) + 1))
		div = int(l[0]) / aux 
		mod = int(l[0]) % aux + 1
		num1 = div - 1
		num2 = div - 1
		if mod >= (int(l[1]) - aux/2 + 1):
			num1 += 1
		if mod - aux/2 >= (int(l[1]) - aux/2 + 1):
                        num2 += 1
		print "Case #" + str(i + 1) + ":", num1, num2

