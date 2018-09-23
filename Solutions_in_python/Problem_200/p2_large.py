#! /usr/bin/python
import sys, random
def is_tidy(n):
	while n >0:
		x = n%10
		n = n/10
		y = n%10
		if x<y:
			return 0
	else:
		return 1

def make_problem(n):
	ch = str(n)
	l = len(ch) - 1
	for i in range(0, l):
		x = ch[i]
		y = ch[i+1]
		if int(x) > int(y):
			p = l-i
			break
	x = n/(10**p)-1
	y = 0
	for i in range(p):
		y += 9*(10**i)
	while not is_tidy(x):
		l = make_problem(x)
		x = l[0]
		y = int(str(l[1])+str(y))
	return x, y

f_i = open(sys.argv[1], "r")
f_o = open("output.out", "w")
T = int(f_i.readline())
for i in range(T):	
	x = int(f_i.readline())
	if is_tidy(x):
		print "Case #"+str(i+1)+": "+str(x)
		f_o.write("Case #"+str(i+1)+": "+str(x)+"\n")
		continue
	y = make_problem(x)
	y = int(str(y[0])+str(y[1]))
	print "Case #"+str(i+1)+": "+str(y)
	f_o.write("Case #"+str(i+1)+": "+str(y)+"\n")