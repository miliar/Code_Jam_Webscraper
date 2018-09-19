# Javier Fernandez Google Code Jam 2013
# Google Code Jam 2013
# javierfdr@gmail.com - javierfdr
# Fair and Square - Generator

import sys
import time
import math

def generate_fair_palindromes(n):
	l=[]
	for i in range(n):
		if is_palindrome(i):
			sqrt = math.sqrt(i)
			if is_int(sqrt) and is_palindrome(int(sqrt)):				
				#l.add(int(sqrt))
				l.append(i)
	l.remove(0)
	return l

def generate_int_sqrt(n):
	l = []
	c = 0
	imp = 1 
	while c<=n:
		c = c+imp
		imp = imp+2

		if c<=n:
			l.append(c)
	
	return l


def is_palindrome(n):
	i = str(n)
	init = 0
	end = len(i)-1

	while(init<end):
		if(i[init]!=i[end]):
			return False
		init = init+1
		end = end-1
	return True

def is_int(n):
	if math.floor(n) == n:
		return True
	return False

def palindromes_bet(n,a,b):
	c = 0
	for i in n:
		if i>=a and i<=b:
			c = c+1
		if i>b:
			break
	return c

out_file = open('output.out','w+')
in_file = sys.stdin
num_cases = int(in_file.readline())
#g = generate_fair_palindromes(1001)
fairpal=[1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004,100000020000001,100220141022001,102012040210201,102234363432201,121000242000121,121242363242121,123212464212321,123456787654321,400000080000004]

for c in range(1,num_cases+1):
	case = 'Case #'+str(c)+': '
	ab= in_file.readline().strip('\n').split()
	r = palindromes_bet(fairpal,int(ab[0]),int(ab[1]))

	result = case+str(r)+'\n'
	out_file.write(result)
	




