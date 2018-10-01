def numofdigits(a):
	count = 0
	while(a>0):
		a=a/10
		count = count+1
	return count

def next_rotation(n,num):
	flag = 0
	for i in range(1,num):
		ten = pow(10,num-i)
		if n%ten == 0:
			flag = 1
			x = n%(ten*10)
			n = n/(ten*10)
			n = x*pow(10,i-1) + n
			return n
	if flag==0:
		x = n%10
		n = n/10
		n = x*pow(10,num-1) + n
		return n

'''
def recycled_pairs(m,n,num):
	# print m,n
	for i in range(0,num-1):
		n = next_rotation(n,num)
		if m==n:
			return True
	return False
'''

def belongsto(n,a,m):
	if n>=m:
		return False
	elif n<a:
		return False
	else:
		return True

def uniq(l):
	output = []
	for x in l:
		if x not in output:
			output.append(x)
	return output

import string

f = open("C-small-attempt1.in",'r')
g = open("output.txt",'w')

lines = f.readlines()

t = lines[0]
t = int(t)
# print t

for i in range(0,t):
	line = lines[i+1]
	line = line.split(" ")
	a = int(line[0])
	b = int(line[1])
	num = numofdigits(a)
	# print a,b,num
	count = 0
	for m in range(a,b+1):
		l = []
		n = m
		for j in range(0,num-1):
			n = next_rotation(n,num)
			if belongsto(n,a,m):
				l.append(n)
		l = uniq(l)
		count = len(l) + count
	string = "Case #" + str(i+1) + ": " + str(count) + "\n"
	g.write(string)
g.close()
f.close()
